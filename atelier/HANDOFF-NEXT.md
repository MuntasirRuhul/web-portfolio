# Handoff: Elena Varga Atelier (start a new chat from this file)

Updated 24 Oct 2026. Repo `MuntasirRuhul/web-portfolio`, branch `claude/gracious-fermat-bqbft2`. Everything here is committed and pushed. Static HTML/CSS/vanilla JS, no build step, Google Fonts.

**To resume in a new chat:** "Read `atelier/HANDOFF-NEXT.md` and continue." This file replaces `SESSION-NOTES.md`. The full design spec is in `atelier/HANDOFF.md`, but where the two disagree, trust this file (see "Stale in HANDOFF.md" below).

---

## 1. Links

| What | Link |
|---|---|
| **Main site (home + course page, linked, takes comments)** | https://claude.ai/artifact/99R7pSgDvcfXydKFhzy8tk |
| Course page alone (old copy, has its own comment history) | https://claude.ai/artifact/YQCTkW8qtcDWazMmMxViMf |
| v8 colour experiment (dcognition.ai scheme, not chosen) | https://claude.ai/artifact/UBUXF74htZnKJqduXDYaw7 |
| Course hero options (Cinema vs Cover) | https://claude.ai/artifact/9HSwGohQj1wet7VU3HZzFm |
| Gallery/review options (history) | https://claude.ai/artifact/5D8MpLJLCNnfkWdmNnxMCt |
| Localhost | clone the branch, `cd atelier && python3 -m http.server 8000`, open http://localhost:8000/atelier-v7.html |
| GitHub preview | `https://raw.githack.com/MuntasirRuhul/web-portfolio/<commit-id>/atelier/atelier-v7.html` (use a commit id; branch names with "/" break githack) |

Only the main site artifact is being updated now. All its comment threads are resolved.

## 2. Files (`atelier/`)

| File | What it is |
|---|---|
| `atelier-v7.html` | **Home page.** The one to build from. |
| `course.html` | **Course detail page** (Course 01 · Foundations of Drawing), the Tutor LMS `single-course.php` template. |
| `HANDOFF.md` | Full spec: tokens, sections, decisions D1–D5, accessibility, QA. Partly stale (see below). |
| `HANDOFF-NEXT.md` | This file. |
| `tools/build-artifact.py` | Builds the artifact: embeds `img/` photos as data URIs (artifacts block external images) and writes `atelier-v7.html` (main page, doctype stripped), `site/home.html` and `site/course.html` (course links rewritten to `home.html`). Run it from a scratch folder that has a `site/` subfolder; it reads from `/home/user/web-portfolio/atelier/`. Needs Pillow. |
| `img/` + `images.txt` | 18 self-hosted placeholder photos (Unsplash, fetched by a GitHub Action). |
| `atelier-v8.html` | dcognition.ai colour experiment. Not chosen. |
| `course-heroes.html` | Hero options page (A1 Cinema, B Cover + notes). |
| `atelier-v6.html`, `gallery-reviews-options.html` | History. |

Elsewhere: `research/tutorlms/STUDY.md` (Tutor LMS page inventory, Course → Topic → Lesson/Quiz/Assignment model, learning-area templates, Elena's course mapped into that structure) and `research/refs/dcognition.ai/`. The sandbox can't reach the web, so fetching runs in GitHub Actions: `.github/workflows/fetch-atelier-images.yml`, `capture-tutorlms.yml`, `capture-refs.yml`.

## 3. Design system (current)

- **Palette (Original, earthy, no blue):** terracotta `#C0512F`, ochre `#DDA43C`, rose `#D9A7A0`, plum `#7A3E5E` (replaces blue), sage `#7E9271`, ink `#1D1A16`, ink-2 `#4A443B`, near-black `#161412`, paper `#F3ECDF`.
- **Grounds:** home page `--page:#FAF6EF` (soft beige), cards white. Course page: white page, soft beige `--soft:#FAF6EF` for the enrol card, review summary and "More courses" band. The strong cream `#F3ECDF` is now only the Cover header panel and text on dark.
- **No shadows anywhere.** Separation comes from colour, rules and rounded corners (16px on cards).
- **Type:** Inter Tight (body and headings; Inter 700 for display), JetBrains Mono for small uppercase labels, Caveat for the signature. Heading accent words in terracotta, no italics. No serif.
- **Ticks and crosses:** plain line tick / cross in terracotta, no circle (the user dislikes round ticks).
- **No pill badges** for counts or tags: use plain text, mono labels or superscripts. Pill **buttons** (Enrol now etc.) are still in use.
- **Icons:** smooth hand-drawn lines with soft colour washes. Never jagged or "wobble" filters.

## 4. Home page (`atelier-v7.html`)

1. **Hero:** dark; construction circle redraws each time the hero comes back into view (`.hero.ring-on`); nav links in the hero, no hamburger on desktop, Menu dropdown on phones; extra gap under the photo (`.big` bottom 27%, row at 15%).
2. **Left rail:** tagline + social links as paint-pot blobs (ochre / rose / terracotta).
3. **Grid:** 4 vertical lines at thirds; the one-third line lines up with the FAQ rules.
4. **03 Method:** dark panel, ochre / rose / terracotta step cards (Look · Sketch · Paint).
5. **04 Courses:** white poster cards on beige; all link to `course.html#cinema`.
6. **05 Gallery:** salon wall, larger labels (title → details → course link).
7. **06 Students:** colour blocks on dark, auto-looping ticker (70s, pauses on hover, static under reduced motion).
8. **07 FAQ:** two columns, text indented from the grid line, book icon (closed = collapsed, open = expanded).
9. **Closing stack:** CTA panel + newsletter + footer with 10px gaps on every side. CTA cards: label, icon disc, fact chips, pill button, photo fading into the panel. Newsletter: one large line, 76px field. Footer: dark, rounded, hero circle drawn in the middle column.

## 5. Course page (`course.html`)

- **Header:** two versions behind a bottom-left switch (`#cinema` default / `#cover`). **Cinema:** dark band, centred title, trailer, facts grid (Rating, Lessons, Length, Level, Certificate), price + buttons, signature. **Cover:** studio photo with a cream panel, facts grid, price + Enrol.
- **Layout:** reading column (760px) + sticky enrol card (360px). Section tabs (About · Curriculum · Teacher · Reviews · Questions) sit directly under the header, sticky; counts are small superscripts, terracotta on the active tab.
- **About:** intro → What you'll learn (line ticks) → **How each topic works** (ochre / rose / terracotta step cards: step number, time ~10/25/30 min, line icon, big title, short text, footer naming the item type; arrows between cards; colour bar "One topic ≈ 1 hour" underneath) → Who it's for (line tick / cross) → What you'll need.
- **Curriculum:** 6 topics with large numerals, aligned item rows (icon / title / type / time / state), "Free preview" as a small terracotta mono label; summary line in plain text.
- **Teacher:** photo + Elena's name, role, quote, three facts, signature, "More about Elena". Spacing opened up (48px photo–text, 32–40px between blocks).
- **Enrol card:** soft beige, rounded, no border; natural-colour trailer with a "Watch the trailer" chip; price $79 / $99 "Autumn price"; Enrol now + Watch lesson 1 free; refund line; "This course includes" with hand-drawn washed icons; gift link. Phones: card first, 24px under the header; sticky bottom price bar.
- **Then:** reviews (average + cards), questions, More courses (poster cards), footer.

## 6. Open decisions (waiting on the user)

1. **Course header:** Cinema or Cover? Then remove the switch and slim the enrol card so price and trailer aren't repeated.
2. **Teacher block:** the text column is now taller than the photo on desktop; make the photo taller to line up? (offered, no answer)
3. **v8:** keep as reference or delete.
4. **Enrol card beige:** now the light `#FAF6EF`; offered to go one step stronger if it reads too faint.

## 7. Next work

1. Lesson / learning-area screen (sidebar curriculum, video, Overview · Exercise files · Comments tabs, Previous / Mark complete / Next).
2. Courses archive (poster cards + medium and level filters).
3. Then About, Studio notes (blog), Services (portfolio review, live class), Contact, Login / Register, Cart / Checkout, and a restyle of the Tutor LMS dashboard.
4. Replace placeholder content: photos, prices, review numbers and quotes, step times.
5. Known: ~5px horizontal overflow on phones from the home About cut-out image (left as is).

## 8. Stale in `HANDOFF.md`

- Section 4 still says the page background is pure white with cream `--band` surfaces. Current: home page soft beige `#FAF6EF`, surfaces and cards white.
- Section 4.2 says method step cards are warm-white. Current: ochre / rose / terracotta on a dark panel.
- Nothing yet about the course page changes from 24 Oct (step cards, line ticks, no pill badges, tabs under the header, soft-beige enrol card).

## 9. How the user gives feedback, and how to publish

- The user comments on the artifact. Comments arrive as notifications: read with ArtifactComments → fix in the repo → commit and push → run `tools/build-artifact.py` → republish the same artifact (main file `atelier-v7.html`, extra files `home.html`, `course.html`) → reply in the thread saying what changed → resolve.
- Screenshot every change at 1440px and 390px with Playwright (pre-installed; import it by absolute path `/opt/node22/lib/node_modules/playwright/index.mjs`) and check `scrollWidth` for phone overflow.
- How the user works: short comments, often with typos; iterate fast and cheaply; ask before big directional changes. When a comment is ambiguous, pick the likeliest reading and say so in the reply. Do exactly what's asked ("make less" means reduce, not remove).
