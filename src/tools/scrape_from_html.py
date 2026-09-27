#!/usr/bin/env python3
"""Reverse-engineer a built chapter page back into a content source dict.
Bootstrap tool: built HTML (already in repo) -> content module data."""
import sys, json, re
from bs4 import BeautifulSoup

TAGS = ("p","b","ul","ol","li","table","thead","tbody","tr","th","td","div","h1","h2","h3","h4","h5","h6",
       "sub","sup","span","br","details","summary","section","article","a","img","iframe","nav","header",
       "footer","script","link","meta","title","head","body","html","button","strong","em","hr","blockquote")
import re as _re
_TAG_RE = _re.compile(r"<(?!/?(?:%s)\b|!)" % "|".join(TAGS))
def pre_clean(text):
    return _TAG_RE.sub("&lt;", text)

def inner(el):
    return "".join(str(c) for c in el.children).strip()

def fix(s):
    return s.replace("\xa0", "&nbsp;")

def scrape(path):
    soup = BeautifulSoup(pre_clean(open(path, encoding="utf-8").read()), "lxml")
    d = {}
    # hero
    d["title_en"] = soup.select_one(".ch-hero h1").get_text(strip=True)
    viol = soup.select_one('.ch-hero p[style*="--violet"]')
    d["title_hi"] = viol.get_text(strip=True) if viol else ""
    mut = soup.select_one('.ch-hero p[style*="--muted"]')
    d["tagline"] = mut.get_text(strip=True) if mut else ""
    # jee weightage + video dur pills
    d["jee"] = ""
    d["video_dur"] = ""
    for p in soup.select(".ch-tags .pill"):
        t = p.get_text(strip=True)
        m = re.search(r"(?:JEE|NEET) Weightage:\s*(\w+)", t)
        if m: d["jee"] = m.group(1)
        m2 = re.search(r"🎬\s*(.+?)\s*video", t)
        if m2: d["video_dur"] = m2.group(1)
    # video
    ifr = soup.select_one("iframe.yt-embed")
    if ifr:
        m = re.search(r"embed/([A-Za-z0-9_-]+)", ifr.get("src",""))
        d["video"] = {"youtube": m.group(1) if m else "", "dur": d["video_dur"]}
    else:
        d["video"] = None
    d["meta_desc"] = (soup.select_one('meta[name="description"]') or {}).get("content","") if soup.select_one('meta[name="description"]') else ""
    # long notes
    def blocks(section_sel, kind):
        out = {}
        sec = soup.select_one(section_sel)
        if not sec: return out
        for lb in sec.select(".lang-block"):
            lang = lb.get("data-lang")
            if kind == "long":
                items = [{"h": fix("".join(str(c) for c in ns.select_one("h3").children).strip()),
                          "body": fix(inner(ns).split("</h3>",1)[1].strip()) if "</h3>" in inner(ns) else ""}
                         for ns in lb.select(".note-sec")]
            else:  # short
                items = [{"h": fix("".join(str(c) for c in sc.select_one("h4").children).strip()),
                          "items": [fix(inner(li)) for li in sc.select("ul li")]}
                         for sc in lb.select(".shorts-card")]
            out[lang] = items
        return out
    d["long"] = blocks("section#notes", "long")
    d["short"] = blocks("section#short-notes", "short")
    # practice
    pr = []
    sec = soup.select_one("section#practice")
    if sec:
        for q in sec.select(".jee-q"):
            qn = q.select_one(".qn")
            if qn: qn.extract()
            det = q.select_one("details.jee-sol")
            ans = fix(inner(det.select_one("p"))) if det and det.select_one("p") else ""
            if det: det.extract()
            qtext = re.sub(r"(<br\s*/?>\s*)+$", "", inner(q).strip()).strip()
            pr.append([qtext, ans])
    d["practice"] = pr
    # topic strip (video breakdown, e.g. ch-1)
    ts = soup.select_one(".topic-strip")
    if ts:
        hd = ts.find_previous("div", class_="sec-head")
        ttl = hd.select_one("h2").get_text(strip=True) if hd and hd.select_one("h2") else "🗂️ Video me kya milega"
        items = []
        for t in ts.select(".topic"):
            b = t.select_one("b"); tm = b.get_text(strip=True) if b else ""
            if b: b.extract()
            items.append({"time": tm, "desc": fix(inner(t))})
        d["topic_strip"] = {"title": ttl, "items": items}
    else:
        d["topic_strip"] = None
    # next chapter
    nxt = soup.select_one(".roadmap a")
    d["next"] = {"href": nxt.get("href"), "title": nxt.get_text(strip=True)} if nxt else None
    return d

if __name__ == "__main__":
    d = scrape(sys.argv[1])
    json.dump(d, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("title_en:", d["title_en"])
    print("title_hi:", d["title_hi"])
    print("jee:", d["jee"], "| video:", d["video"])
    print("long langs:", {k: len(v) for k,v in d["long"].items()})
    print("short langs:", {k: len(v) for k,v in d["short"].items()})
    print("practice:", len(d["practice"]))
    print("next:", d["next"])
