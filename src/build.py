#!/usr/bin/env python3
"""
Maida (मईडा) site builder.
Renders NCERT/CBSE study pages (Class 6-12) from content sources in src/content/.
Reconstructed to match the live template. Default language: Hinglish.
Output: regenerates class-N/... pages + index.html into the repo (site) tree.
"""
import os, sys, json, html, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))          # src/
SITE = os.path.dirname(ROOT)                                # repo root (site output)
CONTENT = os.path.join(ROOT, "content")

FAVICON = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>"
HEAD_LINKS = (
    '<link rel="stylesheet" href="https://cdn.plyr.io/3.7.8/plyr.css">\n'
    '<link rel="stylesheet" href="/assets/css/style.css">\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Poppins:wght@400;500;700&display=swap" rel="stylesheet">'
)
SCRIPTS = '<script src="https://cdn.plyr.io/3.7.8/plyr.js"></script>\n<script src="/assets/js/main.js"></script>'

def nav(active_cls=None):
    cls_link = f'/class-{active_cls}/' if active_cls else '/#classes'
    cls_txt = f'Class {active_cls}' if active_cls else 'Classes'
    return f'''<header class="nav">
  <div class="nav-inner">
    <a href="/" class="logo"><span class="logo-deva">मईडा</span> <span class="logo-en">MAIDA</span></a>
    <nav>
      <a href="/">Home</a>
      <a href="/#classes">Classes</a>
      <a href="{cls_link}">{cls_txt}</a>
      <a href="/#about">About</a>
    </nav>
  </div>
</header>'''

def foot():
    return '''<footer class="foot">
  <div class="foot-inner">
    <div class="logo"><span class="logo-deva">मईडा</span> <span class="logo-en">MAIDA</span></div>
    <p>NCERT / CBSE • Class 6-12 • Video + Long Notes + Short Notes — Hindi, English, Hinglish</p>
    <p class="foot-note">Made with ❤️ for students • Ek-ek chapter karke, concept by concept.</p>
  </div>
</footer>'''

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=False)}">
<link rel="icon" href="{FAVICON}">
{HEAD_LINKS}
</head>
<body>'''

def exam_label(slug):
    return "NEET" if slug == "biology" else "JEE"

def head_page(cls, subj_en, num, title_en, meta_desc):
    t = f"Ch {num} — {title_en} | Class {cls} {subj_en} | मईडा Maida"
    return head(t, meta_desc)

NOTES_HEAD = ('<div class="sec-head"><h2 class="lang-title" data-hinglish="📖 Full Explanation (Long Notes)" data-hi="📖 पूरा Explanation (Long Notes)" data-en="📖 Full Explanation (Long Notes)">📖 Full Explanation (Long Notes)</h2>'
              '<p class="lang-sub" data-hinglish="Concept pakka karne ke liye — aaram se padho" data-hi="Concept pakka karne ke liye — aaram se padho" data-en="Read slowly — this builds the concept solidly">Concept pakka karne ke liye — aaram se padho</p></div>')
SHORT_HEAD = ('<div class="sec-head"><h2 class="lang-title" data-hinglish="⚡ Short Notes — Revision in 5 min" data-hi="⚡ Short Notes — 5 min Revision" data-en="⚡ Short Notes — 5-min Revision">⚡ Short Notes — Revision in 5 min</h2>'
              '<p class="lang-sub" data-hinglish="Exam se pehle sirf yeh dohrao" data-hi="Exam se pehle sirf yeh dohrao" data-en="Revise just this before the exam">Exam se pehle sirf yeh dohrao</p></div>')
LANG_SWITCH = '''<div class="lang-switch" role="group" aria-label="Notes language">
  <span class="lang-label">🌐 Notes language:</span><button class="lang-btn" data-lang="hinglish">Hinglish</button><button class="lang-btn" data-lang="hi">हिंदी</button><button class="lang-btn" data-lang="en">English</button>
</div>'''

def render_chapter(cls, slug, subj_en, CH, prevnext):
    num = CH["num"]; exam = exam_label(slug); wl = CH["jee"].lower()
    # hero pills
    vid = CH.get("video")
    vid_pill = f'🎬 {vid["dur"]} video' if vid else '🎬 Video coming soon'
    pills = (f'<span class="pill weight-{wl}">{exam} Weightage: {CH["jee"]}</span>\n'
             f'    <span class="pill">{vid_pill}</span>\n'
             f'    <span class="pill">📝 Long + Short notes</span>\n'
             f'    <span class="pill">🌐 Hindi • English • Hinglish</span>')
    hero = f'''<section class="ch-hero">
  <p class="crumb"><a href="/">Home</a> / <a href="/class-{cls}/">Class {cls}</a> / <a href="/class-{cls}/{slug}/">{subj_en}</a> / Chapter {num}</p>
  <h1>{CH["title_en"]}</h1>
  <p style="color:var(--violet);margin-top:4px;font-weight:500">{CH["title_hi"]}</p>
  <p style="color:var(--muted);margin-top:6px">{CH["tagline"]}</p>
  <div class="ch-tags">
    {pills}
  </div>
</section>'''
    # featured / video
    if vid and vid.get("youtube"):
        y = vid["youtube"]
        featured = f'''<section class="featured" style="padding-top:10px">
  <div class="player-wrap">
    <iframe id="player" class="yt-embed" src="https://www.youtube.com/embed/{y}" title="Chapter video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  <div class="featured-actions">
    <a class="btn btn-ghost" href="https://www.youtube.com/watch?v={y}" target="_blank" rel="noopener">▶ Watch on YouTube</a>
    <a class="btn btn-ghost" href="#short-notes">⚡ Short Notes</a>
    <a class='btn btn-primary' href='#practice'>🏆 {exam} Practice</a>
  </div>
</section>'''
    else:
        featured = '''<section style="padding-top:14px">
  <div class="video-soon">
    <div class="video-soon-icon">🎬</div>
    <b>Video ban raha hai</b>
    <p>Is chapter ka board-style video jaldi aa raha hai. Tab tak neeche ke notes se padho — woh bhi video-feel mein likhe hain. 👇</p>
  </div>
</section>'''
    tstrip = CH.get("topic_strip")
    ts_html = ""
    if tstrip:
        rows = "\n".join(f'    <div class="topic"><b>{it["time"]}</b>{it["desc"]}</div>' for it in tstrip["items"])
        ts_html = f'<section>\n  <div class="sec-head"><h2>{tstrip["title"]}</h2></div>\n  <div class="topic-strip">\n{rows}\n  </div>\n</section>\n'
    # long notes
    def langblocks(kind):
        out = []
        for lang in ("hinglish", "hi", "en"):
            items = CH[kind].get(lang, [])
            if kind == "long":
                body = "\n".join(f'  <div class="note-sec">\n    <h3>{it["h"]}</h3>\n    {it["body"]}\n  </div>' for it in items)
            else:
                cards = []
                for it in items:
                    lis = "".join(f"<li>{x}</li>" for x in it["items"])
                    cards.append(f'    <div class="shorts-card"><h4>{it["h"]}</h4>\n      <ul>{lis}</ul>\n    </div>')
                body = '<div class="shorts-grid">\n' + "\n".join(cards) + '\n    </div>'
            out.append(f'  <div class="lang-block" data-lang="{lang}" hidden>\n{body}\n  </div>')
        return "\n".join(out)
    notes = f'<section id="notes">\n  {NOTES_HEAD}\n  {LANG_SWITCH}\n{langblocks("long")}\n</section>'
    shorts = f'<section id="short-notes">\n  {SHORT_HEAD}\n  {LANG_SWITCH}\n{langblocks("short")}\n</section>'
    # practice
    qs = []
    for i, (q, a) in enumerate(CH["practice"], 1):
        qs.append(f'    <div class="jee-q"><span class="qn">Q{i}.</span> {q}<br>\n      <details class="jee-sol"><summary>Answer dekho</summary><p>{a}</p></details></div>')
    practice = (f'<section id="practice">\n  <div class="sec-head"><h2>🏆 {exam} Practice — {len(CH["practice"])} Questions</h2><p>Pehle khud solve karo, phir answer dekho.</p></div>\n'
                f'  <div class="note-sec">\n' + "\n".join(qs) + '\n  </div>\n</section>')
    # roadmap
    nxt = prevnext.get("next")
    if nxt:
        road = f'<section class="roadmap">\n  <div class="tip-box">🚀 <b>Agla chapter:</b> <a href="/class-{cls}/{slug}/ch-{nxt["num"]}/">{nxt["title"]}</a> — notes ready hain, abhi padho!</div>\n</section>'
    else:
        road = f'<section class="roadmap">\n  <div class="tip-box">🏆 <b>Class {cls} {subj_en} complete!</b> Revision ke liye short notes + practice dohrao.</div>\n</section>'
    return (head_page(cls, subj_en, num, CH["title_en"], CH["meta_desc"]) + "\n" + nav(cls) + "\n\n" +
            hero + "\n" + featured + "\n" + ts_html + "\n" + notes + "\n" + shorts + "\n" + practice + "\n" + road + "\n" +
            foot() + "\n" + SCRIPTS + "\n</body>\n</html>\n")


# ---------------- index / class / home renderers ----------------

def chapter_card(cls, slug, CH, exam):
    num = CH["num"]; wl = CH["jee"].lower(); vid = CH.get("video")
    topics = "".join(f"<li>{t}</li>" for t in CH.get("card_topics", []))
    if vid and vid.get("youtube"):
        badge = '<span class="badge ok">✅ Video + Notes</span>'
        vidpill = f'<span class="pill">🎬 {vid["dur"]}</span>'
    else:
        badge = '<span class="badge ok">✅ Notes live</span>'
        vidpill = ''
    return f'''    <article class="card done">
      <div class="card-top"><span class="ch-num">{num:02d}</span>{badge}</div>
      <h3>{CH["title_en"]}</h3>
      <p class="card-tag">{CH.get("card_tag", CH["tagline"])}</p>
      <ul class="card-topics">{topics}</ul>
      <div class="card-meta"><span class="pill weight-{wl}">{exam}: {CH["jee"]}</span><span class="pill">🌐 3 languages</span>{vidpill}</div>
      <div class="card-links"><a class="btn btn-primary sm" href="/class-{cls}/{slug}/ch-{num}/">▶ Open Chapter</a></div>
    </article>'''

def render_subject_index(cls, slug, meta, chapters):
    exam = exam_label(slug)
    cards = "\n".join(chapter_card(cls, slug, CH, exam) for CH in chapters)
    n = meta["chapters"]
    title = f'Class {cls} {meta["title_name"]} — All Chapters | मईडा Maida'
    return (head(title, meta["meta"]) + "\n" + nav(cls) + "\n\n" + f'''<section class="ch-hero">
  <p class="crumb"><a href="/">Home</a> / <a href="/class-{cls}/">Class {cls}</a> / {meta["en"]}</p>
  <h1>Class {cls} {meta["en"]} {meta["emoji"]}</h1>
  <p style="color:var(--muted);margin-top:6px">{meta["subtitle"]}</p>
  <div class="ch-tags">
    <span class="pill weight-high">NCERT 2023+ rationalized</span>
    <span class="pill">{meta["unitpill"]}</span>
    <span class="pill">🌐 3 languages</span>
  </div>
</section>
<section style="padding-top:26px">
  <div class="sec-head"><h2>📚 Chapters</h2><p>Sequence mat todo — har chapter agle ki foundation hai</p></div>
  <div class="cards">
{cards}
  </div>
</section>
''' + foot() + "\n" + SCRIPTS + "\n</body>\n</html>\n")

def render_class_page(cls, cfg):
    from site_config import SUBJECT_HI, SUBJECT_LETTER, PLANNED_SUBJECTS
    cards = []
    if cls in cfg.SUBJECTS:
        for slug, m in cfg.SUBJECTS[cls].items():
            topics = (f'<li>📚 {m["chapters"]} chapters (rationalized NCERT)</li><li>🎬 Video + 📝 Long/Short notes</li><li>🌐 Hindi • English • Hinglish</li>')
            cards.append(f'''    <article class="card done">
      <div class="card-top"><span class="ch-num">{SUBJECT_LETTER[slug]}</span><span class="badge ok">✅ Live</span></div>
      <h3>{m["en"]}</h3>
      <p class="card-tag">{SUBJECT_HI[slug]}</p>
      <ul class="card-topics">{topics}</ul>
      <div class="card-links"><a class="btn btn-primary sm" href="/class-{cls}/{slug}/">Open {m["en"]} →</a></div>
    </article>''')
    else:
        for slug, en, hi, letter in PLANNED_SUBJECTS[cls]:
            topics = '<li>📚 Full NCERT chapter list</li><li>🎬 Video + 📝 Long/Short notes</li><li>🌐 Hindi • English • Hinglish</li>'
            cards.append(f'''    <article class="card">
      <div class="card-top"><span class="ch-num">{letter}</span><span class="badge wait">📅 Planned</span></div>
      <h3>{en}</h3>
      <p class="card-tag">{hi}</p>
      <ul class="card-topics">{topics}</ul>
      <div class="card-links"><span class="soon-note">Coming soon 📅</span></div>
    </article>''')
    cards = "\n".join(cards)
    return (head(f'Class {cls} — Subjects | मईडा Maida', f'Class {cls} (NCERT/CBSE) — subjects with video, long + short notes in Hindi, English, Hinglish.') + "\n" + nav(cls) + "\n\n" + f'''<section class="ch-hero">
  <p class="crumb"><a href="/">Home</a> / Class {cls}</p>
  <h1>Class {cls} — Subjects</h1>
  <p style="color:var(--muted);margin-top:6px">NCERT / CBSE • Har subject me video + long notes + short notes (Hindi, English, Hinglish)</p>
</section>
<section style="padding-top:20px">
  <div class="cards">
{cards}
  </div>
</section>
''' + foot() + "\n" + SCRIPTS + "\n</body>\n</html>\n")

def render_home(cfg):
    from site_config import LIVE_CLASSES, CLASS_CARD_TOPICS, PLANNED_CARD_TOPIC
    cards = []
    for cls in (6, 7, 8, 9, 10, 11, 12):
        if cls in LIVE_CLASSES:
            topics = f'<li>{CLASS_CARD_TOPICS[cls]}</li><li>🎬 Video + 📝 Long/Short notes</li><li>🌐 Hindi • English • Hinglish</li>'
            cards.append(f'''    <article class="card class-card done">
      <div class="card-top"><span class="ch-num">{cls}</span><span class="badge ok">✅ Live</span></div>
      <h3>Class {cls}</h3>
      <p class="card-tag">NCERT / CBSE syllabus</p>
      <ul class="card-topics">{topics}</ul>
      <div class="card-links"><a class="btn btn-primary sm" href="/class-{cls}/">Open Class {cls} →</a></div>
    </article>''')
        else:
            topics = f'<li>{PLANNED_CARD_TOPIC}</li><li>🎬 Video + 📝 Long/Short notes</li><li>🌐 Hindi • English • Hinglish</li>'
            cards.append(f'''    <article class="card class-card">
      <div class="card-top"><span class="ch-num">{cls}</span><span class="badge wait">📅 Planned</span></div>
      <h3>Class {cls}</h3>
      <p class="card-tag">NCERT / CBSE syllabus</p>
      <ul class="card-topics">{topics}</ul>
      <div class="card-links"><span class="soon-note">Coming soon 🚀</span></div>
    </article>''')
    cards = "\n".join(cards)
    body = f'''<section class="hero">
  <div class="hero-badge">NCERT / CBSE • CLASS 6-12 • FREE</div>
  <h1>Padhai ab hogi <span class="grad">asaan</span> — video, notes, sab ek jagah</h1>
  <p class="hero-sub">Maida (मईडा) — har class, har subject, har chapter ke liye <b>video + long notes + short notes</b>, woh bhi <b>Hindi, English aur Hinglish</b> mein. Class 11 aur 12 ke <b>saare subjects live</b> — Physics, Chemistry, Maths, Biology.</p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="/class-11/chemistry/ch-1/">▶ Watch Chapter 1 Video</a>
    <a class="btn btn-ghost" href="/class-11/">📚 Explore Class 11</a>
  </div>
  <div class="hero-stats">
    <div class="stat"><b>6-12</b><span>Classes planned</span></div>
    <div class="stat"><b>106</b><span>Chapters live (11+12)</span></div>
    <div class="stat"><b>4</b><span>Subjects (PCM+B)</span></div>
    <div class="stat"><b>100%</b><span>Free, forever</span></div>
  </div>
</section>

<section class="featured" id="featured">
  <div class="sec-head">
    <h2>🎬 Latest Lecture — Class 11 Chemistry, Ch 1</h2>
    <p>Some Basic Concepts of Chemistry • Mole Concept • Board-style magical writing</p>
  </div>
  <div class="player-wrap">
    <iframe id="player" class="yt-embed" src="https://www.youtube.com/embed/h7ie8AHUtDU" title="Class 11 Chemistry Ch 1 video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  <div class="featured-actions">
    <a class="btn btn-primary" href="/class-11/chemistry/ch-1/">Open Chapter Page →</a>
    <a class="btn btn-ghost" href="https://www.youtube.com/watch?v=h7ie8AHUtDU" target="_blank" rel="noopener">▶ Watch on YouTube</a>
  </div>
</section>

<section class="chapters" id="classes">
  <div class="sec-head">
    <h2>🏫 Classes 6-12</h2>
    <p>Ek-ek class, ek-ek subject, ek-ek chapter — systematic tarike se. Class 11 aur 12 live hain, aage aur classes aa rahi hain.</p>
  </div>
  <div class="cards">
{cards}
  </div>
</section>

<section class="about" id="about">
  <div class="sec-head"><h2>Why मईडा?</h2></div>
  <div class="why-grid">
    <div class="why"><b>🌐 3 Languages</b><p>Har chapter ke notes Hindi, English aur Hinglish — teeno mein. Jo bhasha suit kare, usme padho.</p></div>
    <div class="why"><b>🖐️ Board + Hand Cursor</b><p>Teacher ungli rakh ke jaise samjhata hai — waise hi screen par likhate hain.</p></div>
    <div class="why"><b>✨ Magical Writing</b><p>Awaaz ke saath-saath text khud likhta jaata hai — dekh ke samajh aata hai.</p></div>
    <div class="why"><b>🧠 Basics pehle</b><p>Har chapter pichli class ke recap se start hota hai — zero knowledge par bhi chalega.</p></div>
    <div class="why"><b>⚡ Shortcuts + Tricks</b><p>JEE/board tricks, funny examples, aur exam traps — sab marked.</p></div>
    <div class="why"><b>📝 Long + Short Notes</b><p>Long notes concept pakka karne ke liye, short notes 5-min revision ke liye.</p></div>
  </div>
</section>'''
    return (head('मईडा | Maida — Free NCERT/CBSE Study Site (Class 6-12)',
                 'Maida (मईडा) — free NCERT/CBSE study website. Video lectures, long + short notes in Hindi, English, Hinglish. Class 11 & 12 (all subjects) live — Physics, Chemistry, Maths, Biology.')
            + "\n" + nav() + "\n\n" + body + "\n" + foot() + "\n" + SCRIPTS + "\n</body>\n</html>\n")

# ---------------- build orchestration ----------------

def load_chapter(path):
    spec = importlib.util.spec_from_file_location("ch_mod", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CH

def build(out_dir):
    import site_config as cfg
    for cls, subjects in cfg.SUBJECTS.items():
        for slug, meta in subjects.items():
            cdir = os.path.join(CONTENT, f"class-{cls}", slug)
            nums = sorted(int(f[2:-3]) for f in os.listdir(cdir) if f.startswith("ch") and f.endswith(".py"))
            chapters = [load_chapter(os.path.join(cdir, f"ch{n}.py")) for n in nums]
            # chapter pages
            for i, CH in enumerate(chapters):
                nxt = None
                if i + 1 < len(chapters):
                    nxt = {"num": chapters[i+1]["num"], "title": chapters[i+1]["title_en"]}
                page = render_chapter(cls, slug, meta["en"], CH, {"next": nxt})
                p = os.path.join(out_dir, f"class-{cls}", slug, f"ch-{CH['num']}", "index.html")
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p, "w", encoding="utf-8").write(page)
            # subject index
            idx = render_subject_index(cls, slug, meta, chapters)
            p = os.path.join(out_dir, f"class-{cls}", slug, "index.html")
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(idx)
        # class page
        cp = render_class_page(cls, cfg)
        open(os.path.join(out_dir, f"class-{cls}", "index.html"), "w", encoding="utf-8").write(cp)
    # planned class pages
    for cls in cfg.PLANNED_SUBJECTS:
        cp = render_class_page(cls, cfg)
        os.makedirs(os.path.join(out_dir, f"class-{cls}"), exist_ok=True)
        open(os.path.join(out_dir, f"class-{cls}", "index.html"), "w", encoding="utf-8").write(cp)
    # homepage
    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(render_home(cfg))
    print("build complete ->", out_dir)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "site")
    os.makedirs(out, exist_ok=True)
    sys.path.insert(0, ROOT)
    build(out)
