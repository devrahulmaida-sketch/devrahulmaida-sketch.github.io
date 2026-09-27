#!/usr/bin/env python3
"""Scrape a whole subject (class-N/<slug>/) into content modules under src/content/."""
import os, sys, json, re
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrape_from_html import scrape

REPO = sys.argv[1]; CLS = int(sys.argv[2]); SLUG = sys.argv[3]; OUTROOT = sys.argv[4]

idx = BeautifulSoup(open(f"{REPO}/class-{CLS}/{SLUG}/index.html", encoding="utf-8").read(), "lxml")
cards = {}
for c in idx.select("article.card"):
    a = c.select_one('.card-links a[href*="/ch-"]')
    if not a: continue
    m = re.search(r"/ch-(\d+)/", a.get("href",""))
    if not m: continue
    n = int(m.group(1))
    topics = [li.get_text(strip=True) for li in c.select(".card-topics li")]
    tag = c.select_one(".card-tag")
    cards[n] = {"card_topics": topics, "card_tag": tag.get_text(strip=True) if tag else ""}

outdir = f"{OUTROOT}/class-{CLS}/{SLUG}"
os.makedirs(outdir, exist_ok=True)
done = 0
for n in sorted(cards):
    chpath = f"{REPO}/class-{CLS}/{SLUG}/ch-{n}/index.html"
    if not os.path.exists(chpath):
        print(f"  ch-{n}: SKIP (no page, planned)"); continue
    d = scrape(chpath)
    d["num"] = n
    d["card_tag"] = cards[n]["card_tag"] or d.get("tagline","")
    d["card_topics"] = cards[n]["card_topics"]
    # order keys
    CH = {k: d.get(k) for k in ["num","title_en","title_hi","tagline","jee","meta_desc","video","card_tag","card_topics","long","short","practice","topic_strip","next"]}
    js = json.dumps(CH, ensure_ascii=False, indent=1).replace(": null", ": None")
    title = CH["title_en"]
    header = f"# Class {CLS} {SLUG.title()}, Chapter {n} - {title}\n# Reconstructed from built HTML by tools/scrape_subject.py\n"
    open(f"{outdir}/ch{n}.py", "w", encoding="utf-8").write(header + "CH = " + js + "\n")
    done += 1
    print(f"  ch-{n}: OK ({title})  long={ {k:len(v) for k,v in d['long'].items()} } short={ {k:len(v) for k,v in d['short'].items()} } prac={len(d['practice'])} topics={len(CH['card_topics'])}")
print(f"{SLUG}: {done} chapters scraped -> {outdir}")
