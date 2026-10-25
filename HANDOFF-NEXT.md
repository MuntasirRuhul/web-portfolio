# START HERE (updated 25 Oct 2026)

**New chat? Say:** "Read `HANDOFF-NEXT.md` and continue." Work on branch **`atelier-site`** of `MuntasirRuhul/web-portfolio`. It holds only the Atelier, with the home page at `index.html`. Older history is on the `atelier` branch.

**Preview:** https://claude.ai/artifact/99R7pSgDvcfXydKFhzy8tk. Build with `python3 tools/build-artifact.py` run from a scratch folder, then republish the main file `index.html` plus every page in `PAGES` and `assets/*`.

**Status of the 12 new pages** (plan: `openspec/changes/atelier-site-pages/tasks.md`):
- Done: `courses.html` (filters, sort, Solo/Academy) and `about.html` (hero statement; the same chair across twenty years; overheard in 3,900 critiques; brushes in order of use / four teachers, four tools; studio table; tally marks; letter on the drying wall; pull up a chair). The user approved the About hero and asked for non-generic, studio-specific sections, the bar for every page.
- Next: Services, Studio notes (list and article), Contact, then Account, Checkout, Dashboard, Quiz, Assignment. Teachers is optional (academy content already sits on About).
- **Desktop first:** build and check at 1440px only (`node tools/audit.mjs --desktop <page>`). Phone and tablet are a later pass (task group 6).
- Shared parts: `assets/site.css` (design language), `assets/site.js` (menu, Solo/Academy review bar, helpers). Every page declares `<body data-archetype>`, uses `.site-head` and the dark `.site-foot` on a `.foot-band`, and must pass the audit before publishing.
- Header links still point to home anchors for pages not built yet (Services, Questions). Re-point them as pages land.
- Keep replies short: the user is watching token use.

---

# Handoff: Elena Varga Atelier (start a new chat from this file)

Updated 24 Oct 2026. Repo `MuntasirRuhul/web-portfolio`, branch `claude/gracious-fermat-bqbft2`. Everything here is committed and pushed. Static HTML/CSS/vanilla JS, no build step, Google Fonts.

**To resume in a new chat:** "Read `HANDOFF-NEXT.md` and continue." This file replaces `SESSION-NOTES.md`. The full design spec is in `HANDOFF.md`, but where the two disagree, trust this file (see "Stale in HANDOFF.md" below).

---

## 1. Links

| What | Link |
|---|---|
| **Main site (home + course + lesson pages, linked, takes comments)** | https://claude.ai/artifact/99R7pSgDvcfXydKFhzy8tk |
| Course page alone (old copy, has its own comment history) | https://claude.ai/artifact/YQCTkW8qtcDWazMmMxViMf |
| v8 colour experiment (dcognition.ai scheme, not chosen) | https://claude.ai/artifact/UBUXF74htZnKJqduXDYaw7 |
| Course hero options (Cinema vs Cover) | https://claude.ai/artifact/9HSwGohQj1wet7VU3HZzFm |
| Gallery/review options (history) | https://claude.ai/artifact/5D8MpLJLCNnfkWdmNnxMCt |
| Localhost | clone the branch, `cd atelier && python3 -m http.server 8000`, open http://localhost:8000/index.html |
| GitHub preview | `https://raw.githack.com/MuntasirRuhul/web-portfolio/<commit-id>/index.html` (use a commit id; branch names with "/" break githack) |

Only the main site artifact is being updated now. All its comment threads are resolved.

## 2. Files (`atelier/`)

| File | What it is |
|---|---|
| `index.html` | **Home page.** The one to build from. |
| `course.html` | **Course detail page** (Course 01 · Foundations of Drawing), the Tutor LMS `single-course.php` template. Its "Log in" button opens `lesson.html` (demo path into the learning area). |
| `lesson.html` | **Lesson / learning area** (Topic 04 · Lesson 1 "Three values, not seven"), the Tutor LMS `single-lesson.php` + `learning-area/*` templates. |
| `HANDOFF.md` | Full spec: tokens, sections, decisions D1–D5, accessibility, QA. Partly stale (see below). |
| `HANDOFF-NEXT.md` | This file. |
| `tools/build-artifact.py` | Builds the artifact: embeds `img/` photos as data URIs (artifacts block external images) and writes `index.html` (main page, doctype stripped), `site/home.html`, `site/course.html` (course links rewritten to `home.html`) and `site/lesson.html`. Run it from a scratch folder that has a `site/` subfolder; it reads from `/home/user/web-portfolio/atelier/`. Needs Pillow. |
| `img/` + `images.txt` | 18 self-hosted placeholder photos (Unsplash, fetched by a GitHub Action). |
| `atelier-v8.html` | dcognition.ai colour experiment. Not chosen. |
| `course-heroes.html` | Hero options page (A1 Cinema, B Cover + notes). |
| `atelier-v6.html`, `gallery-reviews-options.html` | History. |

Elsewhere: `research/tutorlms/STUDY.md` (Tutor LMS page inventory, Course → Topic → Lesson/Quiz/Assignment model, learning-area templates, Elena's course mapped into that structure) and `research/refs/dcognition.ai/`. The sandbox can't reach the web, so fetching runs in GitHub Actions: `.github/workflows/fetch-atelier-images.yml`, `capture-tutorlms.yml`, `capture-refs.yml`.

## 3. Design language (source of truth)

The rules live in OpenSpec change `atelier-art-direction` (`openspec/changes/atelier-art-direction/specs/`), the tokens and components in `assets/site.css`, and the visual reference in `style.html`. If anything below disagrees with those, they win.

- **Idea:** an artist's studio presented as a gallery. Sections are things in the studio (posters, a wall, letters, labels). Structure is grey line and paper; colour arrives in a few blocks (ochre → rose → terracotta). Look longer: space, slow motion, one idea per section. The hand is present: signature, irregular pots, a small tilt. Quiet mono labels, loud sentence headlines.
- **Colour roles:** paper `#FAF6EF` (gallery ground), white (objects and reading pages), room `#161412`, ink `#1D1A16`, ink-2 `#4A443B`, muted `#6E6658` (was `#8A8172`, too faint). The accent is terracotta `#C0512F`. As text under 24px on light grounds use `--accent-text #B24A2B`; on dark use `#E8724A`. Text on the terracotta block is white. Course accents `--c1…c6`. No blue.
- **Type:** Inter Tight, Inter 700 (posters and numerals), JetBrains Mono 10.5px uppercase at `.06em` (labels), Caveat (signature only). Scale: display `clamp(40,5vw,68)`, h2 `clamp(30,3.5vw,48)`, h3 `clamp(22,2vw,28)`, 18 / 16 / 14. No italics, no serif.
- **Radii:** 28 room (22 on phones), 16 card, 12 field and bar, 999 pill, 50% disc. 1px rules (`.14`), grid lines `.075`. **No shadows** (paint pots' inset rim excepted).
- **Voice:** each section opens with a chapter label (`02 THE ARTIST ——`) and a sentence headline ending in a full stop, often landing on one terracotta phrase. Nouns such as "Curriculum" go in labels and tabs, never as headlines.
- **Micro:** curly quotes, `·` separators, `→`, `×`, en dashes, tabular numbers; 1.6px round-cap line icons; plain line ticks; no pill badges for counts or tags.
- **Motion:** objects `cubic-bezier(.2,.7,.2,1)` (reveal .9s, lift −6px with a −.6° tilt), lines `cubic-bezier(.6,.1,.2,1)` (1.3–2.4s draw). Everything stops under reduced motion.
- **Archetypes** (`<body data-archetype>`): **Gallery** (paper, grain, grid lines, chapter labels, one dark room), **Reading** (white sheet; beige, grain and grid only inside bands), **Workroom** (quiet tool: no grain, grid, display headlines or reveal), **Counter** (one white card on paper beside a room or photo; errors in terracotta text).

### Review checklist (run before every publish)

- **Macro (page):** the right archetype and its rules; the shared header brand and the shared dark footer (`.site-foot` on a paper band; Workroom screens have none); one idea per section; a rhythm of paper → room → objects; one clear first action; it ends with a next step.
- **Meso (section):** a chapter label and a voiced headline; aligned to the grid lines; colour blocks in order; images grey at rest, colour on touch; captions in mono.
- **Micro (details):** sizes on the scale; radii and rules on the scale; real characters (curly quotes, `·`, `→`, `×`, en dash); line icons and ticks; hover and focus states (terracotta focus ring); reduced motion; contrast of 4.5:1 for body text and 3:1 for large text.
- **Scripted:** `node tools/audit.mjs <pages>` must pass (exit 0). Then look at before/after screenshots at 1440px and 390px.

## 4. Home page (`index.html`)

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

- **Two views behind a bottom-left review switch:** Visitor (`#visitor`, default) and Enrolled (`#enrolled`); `#cinema` / `#cover` fall back to Visitor. Built by OpenSpec change `course-page-concept-v2` (`openspec/changes/`).
- **Header (Visitor), Cinema only:** dark band, "Course 01 · Pencil" mono label, centred title, trailer, 6-cell facts grid (Rating, Lessons, Length, Level, Students 3,180, Updated Oct 2026), Wishlist (toggles to Saved) and Share (copies the link) as quiet text links, price + buttons, signature. Cover was dropped; it stays on record in `course-heroes.html`.
- **Header (Enrolled):** "Welcome back, Marta", progress 50% · 12 of 24 done (ochre bar), Up next card (poster, Topic 04 · Lesson 1, "Three values, not seven", 19:40), Continue + Course resources buttons, all to `lesson.html`. No price.
- **Layout:** reading column (760px) + sticky enrol card (360px). Section tabs (About · Curriculum · Teacher · Reviews · Before you enrol) sit directly under the header, sticky; counts are small superscripts, terracotta on the active tab.
- **About:** intro → What you'll learn (line ticks) → **How each topic works** (ochre / rose / terracotta step cards: step number, time ~10/25/30 min, line icon, big title, short text, footer naming the item type; arrows between cards; colour bar "One topic ≈ 1 hour" underneath) → Who it's for (line tick / cross) → What you'll need.
- **Curriculum:** 6 topics with large numerals, aligned item rows (icon / title / type / time / state), "Free preview" as a small terracotta mono label; summary line in plain text. Enrolled view: topics 1–3 "4 of 4 done" in terracotta, line ticks on done items, topic 4 open with "Up next" on lesson 1, no locks except the critique assignment.
- **Teacher:** photo + Elena's name, role, quote, three facts, signature, "More about Elena". Spacing opened up (48px photo–text, 32–40px between blocks).
- **Enrol card (Visitor):** soft beige, rounded, no border; no trailer (it's in the header); price $79 / $99 "Autumn price"; Enrol now + Watch lesson 1 free; refund line; "This course includes" with hand-drawn washed icons; gift link. Phones: card first, 24px under the header; sticky bottom price bar.
- **Continue card (Enrolled):** poster with an "Up next 19:40" chip, lesson title, progress bar, Continue learning + Course resources, "Your course" list (certificate locked · 12 items to go, private critique after topic 6, reference sheets 4 of 6, enrolled 3 Sep 2026), "Ask Elena". Phone bar shows 50% · 12 of 24 done + Continue.
- **Shared state:** the enrolled view and `lesson.html` both show Marta at 12 of 24 (50%), topic 4 lesson 1 current. Change both files together.
- **Then:** **Week 1 → Week 6** strip (three first-vs-final drawing pairs: Marta egg, Priya mug, Leila pear; drawn SVG placeholders, swap for real student work), reviews (average + cards), Before you enrol (pre-sale FAQ; the name avoids Tutor's enrolled-only Q&A), More courses (poster cards), footer.

## 5b. Lesson page (`lesson.html`)

- **State shown:** Marta K., enrolled, topics 1–3 done (12 of 24 items, 50%), on Topic 04 · Lesson 1 "Three values, not seven".
- **Header (sticky, 64px):** ← Course (to `course.html#curriculum`) · "Course 01 · Pencil / Foundations of Drawing" · progress "12 of 24 done", bar in the course accent, % · avatar. Phones: progress becomes a 2px line under the header, plus a "Contents" pill.
- **Sidebar (340px, soft beige, sticky, own scroll):** "Course content 12 / 24", topics as accordions (numeral in course accent, "4 of 4 done" in terracotta), items with line tick when done, type icon otherwise; current item is a white row with a 3px accent bar and "Now playing"; the critique assignment is locked ("After your final drawing"). "Stuck on something?" card at the bottom. Phones: a drawer from the left with a scrim (Escape / scrim / × close).
- **Lesson column (max 880px):** 16:9 player (rounded 16px; simulated playback, scrub with chapter marks, CC, speed, full screen); mono label "Topic 04 · Light and value · Lesson 1 of 4", H1, meta line, and a small 3-segment "Step 02 · Sketch" bar tying the lesson to the Look / Sketch / Finish method.
- **Tabs:** Overview · Exercise files ³ · Comments ¹⁴ (superscript counts, ARIA tabs, arrow keys).
  - Overview: lead, "In this lesson" chapter list (clickable times seek the video), "Have these ready" (line ticks), two tilted note cards: rose "A note from Elena" with signature, ochre "After this lesson" (links to the files tab).
  - Exercise files: three rows with drawn thumbnails (three-value scale, egg reference, notes), outline pill "Download".
  - Comments: compose box (beige field), comments with initials, "at 06:12" timestamps, Elena's reply indented with a rose rule and a mono "Teacher" label (not a pill). Posting adds the comment (demo).
- **Bottom bar (sticky):** Previous (outline circle + title) · Mark as complete (ink pill → outline "Completed" with a terracotta line tick; updates the sidebar item, topic count and progress) · Next (ink circle + title). Phones: fixed, titles hidden.

## 6. Open decisions (waiting on the user)

1. ~~Course header~~ Cinema chosen 24 Oct (Cover removed, trailer no longer repeated in the card). Assumed on the user's behalf in `course-page-concept-v2`; easy to flip back from `course-heroes.html`.
2. **Teacher block:** the text column is now taller than the photo on desktop; make the photo taller to line up? (offered, no answer)
3. **v8:** keep as reference or delete.
4. **Enrol card beige:** now the light `#FAF6EF`; offered to go one step stronger if it reads too faint.

## 7. Next work

1. ~~Lesson / learning-area screen~~ done 24 Oct (`lesson.html`), waiting for the user's comments. Follow-ups: quiz screen, assignment upload ("Submit for Elena's critique"), free-preview variant for non-enrolled visitors.
2. Courses archive (poster cards + medium and level filters).
3. Then About, Studio notes (blog), Services (portfolio review, live class), Contact, Login / Register, Cart / Checkout, and a restyle of the Tutor LMS dashboard.
4. Replace placeholder content: photos, prices, review numbers and quotes, step times.
5. Known: ~5px horizontal overflow on phones from the home About cut-out image (left as is).

## 8. Stale in `HANDOFF.md` (section 3 above replaces its design-system parts)

- Section 4 still says the page background is pure white with cream `--band` surfaces. Current: home page soft beige `#FAF6EF`, surfaces and cards white.
- Section 4.2 says method step cards are warm-white. Current: ochre / rose / terracotta on a dark panel.
- Nothing yet about the course page changes from 24 Oct (step cards, line ticks, no pill badges, tabs under the header, soft-beige enrol card).

## 9. How the user gives feedback, and how to publish

- The user comments on the artifact. Comments arrive as notifications: read with ArtifactComments → fix in the repo → commit and push → run `tools/build-artifact.py` → republish the same artifact (main file `index.html`, extra files `home.html`, `course.html`, `lesson.html`) → reply in the thread saying what changed → resolve.
- Screenshot every change at 1440px and 390px with Playwright (pre-installed; import it by absolute path `/opt/node22/lib/node_modules/playwright/index.mjs`) and check `scrollWidth` for phone overflow.
- How the user works: short comments, often with typos; iterate fast and cheaply; ask before big directional changes. When a comment is ambiguous, pick the likeliest reading and say so in the reply. Do exactly what's asked ("make less" means reduce, not remove).
