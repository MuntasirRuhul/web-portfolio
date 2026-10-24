# Session notes: Elena Varga Atelier (for resuming after compaction)

Last updated: 24 Oct 2026. Branch: `claude/gracious-fermat-bqbft2` (repo `MuntasirRuhul/web-portfolio`). Everything below is committed and pushed.

## Links
| What | Link |
|---|---|
| **Main site (home + course page, linked)** | https://claude.ai/artifact/99R7pSgDvcfXydKFhzy8tk |
| Course page alone (its own comment history) | https://claude.ai/artifact/YQCTkW8qtcDWazMmMxViMf (`#cinema` / `#cover`) |
| v8 colour experiment (dcognition.ai scheme) | https://claude.ai/artifact/UBUXF74htZnKJqduXDYaw7 (`#dark` / `#light`) |
| Course hero options (rounds 1–3) | https://claude.ai/artifact/9HSwGohQj1wet7VU3HZzFm |
| Gallery/review options (round 1) | https://claude.ai/artifact/5D8MpLJLCNnfkWdmNnxMCt |
| Real-photo copy on GitHub (commit-pinned) | `https://raw.githack.com/MuntasirRuhul/web-portfolio/<commit>/atelier/atelier-v7.html` (branch names with "/" don't work on githack; use a commit id) |
| Localhost | clone the branch, `cd atelier && python3 -m http.server 8000`, open http://localhost:8000/atelier-v7.html |

## Files (atelier/)
- `atelier-v7.html` – **main home page** (build from this).
- `course.html` – course detail page (Foundations of Drawing), Tutor LMS single-course template. Two header layouts with a bottom-left switch: Cinema (dark, default) / Cover.
- `atelier-v8.html` – v8 colour experiment only (not chosen).
- `course-heroes.html` – hero options page (A1 dark cinema + B magazine cover remain).
- `gallery-reviews-options.html`, `atelier-v6.html` – history.
- `HANDOFF.md` – full spec (tokens, sections, decisions D1–D5, QA). `img/` – 18 self-hosted placeholder photos; `images.txt` list.
- `research/tutorlms/STUDY.md` – Tutor LMS study (page inventory, course→topic→lesson/quiz/assignment structure, template files). `research/refs/dcognition.ai/` – captured reference.
- Workflows: `.github/workflows/fetch-atelier-images.yml`, `capture-tutorlms.yml`, `capture-refs.yml` (GitHub Actions do the web fetching; the sandbox can't reach external sites).

## Decisions so far
- **Palette:** Original (earthy): terracotta #C0512F, ochre #DDA43C, rose #D9A7A0, ink #1D1A16, near-black #161412. **No blue** (watercolour accent = plum #7A3E5E).
- **Home page background:** soft beige `--page:#FAF6EF`; cards (course, gallery mats, newsletter) white. No shadows anywhere.
- **Font:** Inter Tight (+ JetBrains Mono labels, Caveat signature). Not the serif. Heading accent words in terracotta (no italics).
- **Grid lines:** 4 vertical lines at thirds; the one-third line aligns with the FAQ rules.
- **Hero:** dark; construction circle redraws each time hero re-enters view; extra gap under the photo.
- **Nav:** links in hero, no hamburger on desktop; phone uses a Menu dropdown. Left rail: tagline + social icons as **paint pots** (ochre/rose/terracotta blobs).
- **Method (03):** dark panel, step cards ochre / rose / terracotta.
- **Courses (04):** poster cards; all link to `course.html#cinema`.
- **Gallery (05):** salon wall; labels title → details → course link (larger).
- **Students (06):** colour blocks on dark, **auto-looping ticker** (70s, pauses on hover, static under reduced motion), 6 placeholder reviews.
- **FAQ (07):** two columns, text indented from grid line, **book icon** (closed = collapsed, open = expanded).
- **Closing stack:** CTA panel + newsletter + footer, **10px gap on all sides**. CTA cards redesigned (label, icon disc, chips, pill button; photo fades into panel). Newsletter: tall, one large line, 76px field. Footer: dark rounded, hero circle drawn in middle column (same as hero, no spin).
- **Course page:** info-first layout (reading column + sticky enrol card, sticky section tabs with counts), filled tick icons, tick/cross "Who it's for", aligned curriculum rows with large topic numerals, teacher section about Elena (no sketchbook row), hand-drawn icons with colour washes in "This course includes". Course page still uses white page + cream panels (not yet matched to home's soft beige).

## Open / next
1. Pick course header: **Cinema** or **Cover**; then remove switch, slim the enrol card (avoid repeating price/trailer).
2. Match course page colours to home (soft beige page, white cards)? – asked, no answer yet.
3. v8: keep only as reference, or delete.
4. Next pages from the Tutor LMS study: lesson / learning area, courses archive, then About, Studio notes, Services, Contact, Login/Register, Cart/Checkout, dashboard restyle.
5. Real content: photos, prices, review numbers, student quotes (all placeholders). Phone pages have a pre-existing ~5px horizontal overflow from the About cut-out image.

## How I publish (for continuity)
- Build script in scratchpad `art/site.py` embeds `img/` photos as data URIs and publishes `atelier-v7.html` as the main page with `home.html` + `course.html` as extra files (course links rewritten to `home.html`). If the scratchpad is gone, rebuild: embed images, strip doctype/head wrapper, publish with `files`.
- Comments arrive via notifications → read thread → fix → commit/push → republish → reply → resolve.
