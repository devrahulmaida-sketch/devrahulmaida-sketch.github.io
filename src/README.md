# Maida (मईडा) — site source & builder

This `src/` folder is the durable source of truth for the site. The rendered HTML at the
repo root (`index.html`, `class-6/` … `class-12/`) is generated from here. Never edit the
rendered pages by hand for new work — edit the content source and rebuild.

## Layout
- `build.py` — the renderer (chapter pages, subject indexes, class pages, homepage).
- `site_config.py` — class/subject metadata (names, emojis, subtitles, chapter counts, planned classes).
- `content/class-<N>/<subject>/ch<M>.py` — one module per chapter. Each defines `CH`, a dict:
  `num, title_en, title_hi, tagline, jee (HIGH/MEDIUM/LOW), meta_desc, video, card_tag,
   card_topics[4], long{hinglish,hi,en}, short{hinglish,hi,en}, practice[[q,a]x10], topic_strip, next`.
  - `video` = `{"youtube": "<id>", "dur": "M min SS sec"}` or `None` (renders "Video coming soon").
  - `long` / `short` values are lists of `{"h": heading, "body": html}` (long) or `{"h": heading, "items": [html]}` (short).
  - `topic_strip` = optional video chapter breakdown (only ch-1 chemistry currently).
- `tools/` — bootstrap scrapers used to reverse-engineer these sources from the built HTML
  (`scrape_from_html.py`, `scrape_subject.py`, `build_config.py`). Kept for the record / re-scrapes.

## Build
```
python3 src/build.py <output_dir>     # renders the full site into <output_dir>
```
Then sync `<output_dir>` over the repo root, EXCLUDING Rahul's originals (never overwrite):
`chapters/ch1.html`, `videos/`, `assets/img/ch1-thumb.jpg`, `.git`. Use `rsync -a` (no `--delete`).

Default language is Hinglish (main.js toggle: Hinglish / हिंदी / English). Biology auto-labels
"NEET"; all other subjects "JEE".

## Reconstruction notes
Sources were reverse-engineered from the live built HTML (Sept 2026). The rebuild is byte-faithful
except where it intentionally fixes pre-existing live bugs: class-12 pages linking nav to /class-11/,
class-12 subject cards showing class-11 chapter counts, the chemistry subject index not reflecting the
ch-6/8/9 videos, raw `<` in a few pages (now escaped), and 8 last-chapter "complete!" roadmap pages that
shipped with unrendered `{cls}` placeholders.
