#!/usr/bin/env python3
"""Build site_config.py subject metadata from the built subject-index pages."""
import re, json
from bs4 import BeautifulSoup
REPO = "/home/sandbox/repo"
cfg = {}
for cls in (11, 12):
    for slug in ("physics", "chemistry", "biology", "maths"):
        f = f"{REPO}/class-{cls}/{slug}/index.html"
        soup = BeautifulSoup(open(f, encoding="utf-8").read(), "lxml")
        h1 = soup.select_one(".ch-hero h1").get_text(strip=True)
        m = re.match(r"Class \d+ (.+?)\s*(\S+)\s*$", h1)  # name + trailing emoji
        name_emoji = h1.split(None, 2)[2] if len(h1.split(None,2))>=3 else h1
        # emoji = last token, name = middle
        parts = h1.split()
        emoji = parts[-1]
        subj_en = " ".join(parts[2:-1])
        subtitle = soup.select_one('.ch-hero p[style*="--muted"]').get_text(strip=True)
        title = soup.select_one("title").get_text(strip=True)
        title_name = re.search(r"Class \d+ (.+?) — All Chapters", title).group(1)
        meta = soup.select_one('meta[name="description"]').get("content")
        # unit pill
        pills = [p.get_text(strip=True) for p in soup.select(".ch-tags .pill")]
        unitpill = next((p for p in pills if re.search(r"\d+ (units|chapters)", p)), "")
        nch = len(soup.select("article.card"))
        cfg.setdefault(cls, {})[slug] = {
            "subj_en": subj_en, "emoji": emoji, "title_name": title_name,
            "subtitle": subtitle, "meta": meta, "unitpill": unitpill, "chapters": nch,
        }
json.dump(cfg, open("/home/sandbox/edusite/scraped/subject_config.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(cfg, ensure_ascii=False, indent=1))
