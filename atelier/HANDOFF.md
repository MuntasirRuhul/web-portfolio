# Elena Varga Atelier: theme handoff

**Date:** 23 October 2026 · **Status:** design complete, ready to build · **Owner:** hellomuntasir@gmail.com

A one-page website for an artist who sells online drawing and painting courses. The page should feel like a piece of artwork, but stay calm: almost no complex interaction.

---

## 1. Source of truth

| What | File | Notes |
|---|---|---|
| **Final page** | `atelier-v7.html` | Build from this. Single self-contained file: HTML, CSS and a little vanilla JS. |
| Previous version | `atelier-v6.html` | Same page with the old gallery (filters + featured work) and the old student story. Reference only. |
| Section options | `gallery-reviews-options.html` | The three gallery and three review directions that v7 chose from (A · Salon wall and C · Letters). |
| Style guide | `style-guide.html` | Type, spacing, components, imagery, motion, voice. **Colours in it are the original palette;** see section 4 here for the new ones. |
| **Single course page** | `course.html` | Course 01 · Foundations of Drawing, the template for every course (Tutor LMS `single-course.php`). Information-first layout: one reading column + one sticky enrol card, sticky section tabs (About · Curriculum · Teacher · Reviews · Questions), no grid lines or rail. Uses the v7 tokens and poster cards only for "Where students go next". See `research/tutorlms/STUDY.md` for the structure. |
| Course card (copy-paste) | `poster-card-c.html` | The white poster card used on the site, standalone with all six courses. |
| Figma | [art and potery](https://www.figma.com/design/0wA3LYabKVP9Jl4FMLjYKH/art-and-potery?node-id=0-1) | Course card component, level-meter variants, colour variables, text styles. |

**Run locally:** from this folder, `python3 -m http.server 8000`, then open <http://localhost:8000/atelier-v7.html>.

**External dependencies:** Google Fonts (Inter, Inter Tight, JetBrains Mono, Caveat) only. Photos are self-hosted placeholder copies in `img/` (downloaded from Unsplash by the `Fetch Atelier images` workflow from the list in `images.txt`). No frameworks, no build step.

---

## 2. Decisions still open (resolve before or during build)

| # | Decision | Options | Recommendation |
|---|---|---|---|
| D1 | ~~Colour palette~~ | **Decided:** Original, with plum instead of blue. Other palettes and the picker removed in v7. | Done. |
| D2 | ~~Student section layout~~ | **Decided:** colour blocks on the dark ground (ochre, rose, terracotta). Gallery decided too: Salon wall. | Done. |
| D3 | **Real content** | All names, quotes, stats, prices and images are placeholders | See section 9. |
| D4 | **Course page top section** | Narrowed to two, both now in `course.html` with a switch (bottom-left; `#cinema` / `#cover` links): **Cinema** (dark band, centred title, trailer, facts grid, price + buttons, signature) and **Cover** (full-width studio photo, cream panel with the facts grid and price + enrol). Facts follow the spec-sheet hierarchy: rating, lessons, length, level, then critique and certificate. | Pick one; then remove the switch and the other header. |

---

## 3. Page structure

Order top to bottom. `g6` = the 6-column grid wrapper.

| # | Section | Element / id | Purpose | Notes |
|---|---|---|---|---|
| | Left rail | `aside.rail` | Vertical tagline, socials | Fixed, 56px wide, desktop only (hidden at ≤ 980px). No hamburger: navigation lives in the hero. |
| 01 | **Hero** | `section.hero#top` | Who she is, entry to courses | Dark full-height band. Construction lines: a vertical rule at 38%, a broken horizontal rule at 48%, and an SVG circle that draws itself once. Small portrait left, large photo right, roles list, "Since 2006", "Explore the courses" link with a painted underline. Own split nav: About · Courses · Gallery · Students left, FAQ · Free lesson · Log in right. At ≤ 980px the links collapse into a **Menu** button (left) that opens a dropdown panel (`.hn-panel`, `aria-expanded`, closes on link click and Esc); Log in stays visible. The circle redraws every time the hero scrolls back into view. |
| | Side tab | `a.tabv` | Shortcut to free lesson | Fixed to the right edge: "EV. Free lesson" → `#join`. |
| 02 | **About** | `section.about#about` | The artist | Centred 880px column: statement heading, two paragraphs, signature. Two **cut-out** images (shot on white, `mix-blend-mode: multiply`). Section needs a solid background for the blend to work. |
| 03 | **Method** | `section.method` | Look · Sketch · Paint | Rounded panel on the signature band. Three step cards, solid colour blocks in the new palettes. Icons are inline SVG that draw in on scroll. |
| 04 | **Courses** | `section.courses#courses` | The catalogue (6 courses) | Poster cards on the signature band. See section 6.3. |
| 05 | **Gallery** | `section.gw#gallery` | Her work, linked to courses | **Salon wall.** Seven works in two rows, hung on a dashed centre line (`.gw-row::before`). Each `a.gw-w` sets its width with `--w`, image ratio with `--r` and course colour with `--pc`; frames are a white mat (`.gw-f`) or mat + ink border (`.gw-f.dark`). Museum label under each (`.gw-l`): title, medium · year · size, course dot. No filters, no JS. At ≤ 760px it becomes a 2-column grid, first work full width. |
| 06 | **Students** | `section.rl.rv-dark#students` | Social proof | Dark ground (`--night`). Three solid colour blocks (`.rv-block`, `--bg`/`--fg` per card: ochre, rose, terracotta), each with a big quote mark, the quote, and name · course. Then a 4-up stats row and "Read all reviews". 3 → 1 columns at 860px. |
| 07 | **FAQ** | `section.faq#faq` | Objections | Native `<details>`, first open. |
| 08 | **Join** | `section.join#join` | Conversion | Dark panel with two action cards (portfolio review, live class) + photo, then the newsletter strip. |
| | Footer | `footer` | Links | 3 columns + base row. |

---

## 4. Colour tokens

**Palette decided: Original, on white.** The page background is pure white (`--page:#FFFFFF`); the former cream paper `#F3ECDF` is now the surface colour (`--band`) for the method panel, courses section, newsletter strip, footer column and the gallery mats. Cards on it are white. Near-black hero, students section and CTA panel; terracotta accent. It is the only palette in v7: the other four palettes, the picker, its CSS and its script have been removed. No blue anywhere: the Original palette's one blue (Watercolour course accent and `--ultra`) is now garden plum `#7A3E5E`.

### 4.1 Token roles

| Token | Role |
|---|---|
| `--page` | Page background (white) |
| `--paper` | Light text on dark surfaces (cream) |
| `--card` | Cards (white) |
| `--band` | **Surface** (cream): method panel, courses section, newsletter strip, gallery mats |
| `--band-soft` | Footer column and image placeholders (same as `--band`) |
| `--on-band` / `--on-band-2` / `--band-accent` | Text, secondary text and accent **on** the band |
| `--ink` / `--ink-2` / `--muted` | Text: primary, secondary, labels |
| `--terra` | Brand accent: emphasis words, button hover fill |
| `--night` / `--night-2` | Dark surfaces: hero, CTA panel |
| `--accent-lt` | Accent on dark surfaces |
| `--dim` / `--dimmer` | Secondary text on dark |
| `--c1…--c6` | Course card accents (one per course) |
| `--ink-rgb`, `--on-dark-rgb` | RGB triplets used in `rgba()` for lines and shadows |

### 4.2 Values (all on `:root`)

```css
--page:#FFFFFF; --paper:#F3ECDF; --band:#F3ECDF; --card:#FFFFFF;
--ink:#1D1A16; --ink-2:#4A443B; --muted:#8A8172; --ink-rgb:29,26,22;
--terra:#C0512F; --ochre:#DDA43C; --ultra:#7A3E5E; --sage:#7E9271; --rose:#D9A7A0;
--band-soft:var(--band); --on-band:var(--ink); --on-band-2:var(--ink-2); --band-accent:var(--terra);
--night:#161412; --night-2:#2A2522; --accent-lt:#E8724A; --dim:#A9A092; --dimmer:#8F877A; --on-dark-rgb:243,236,223;
--c1:#8F6511; --c2:#A55C52; --c3:#7A3E5E; --c4:#1D1A16; --c5:#C0512F; --c6:#56694A;
```

Method step cards are warm-white cards on the band with ink text and terracotta step numbers (the colour-blocked cards only existed in the removed palettes). The paper grain is neutral grey at 14% so white stays white. **No shadows anywhere:** cards, gallery frames, colour blocks and the side tab are flat; separation comes from colour, the cream mats and 1px rules.

### 4.3 Course accents (`--pc` on each card)

| Course | Medium | Token |
|---|---|---|
| 01 Foundations of Drawing | Pencil | `--c1` |
| 02 The Portrait in Pencil | Graphite | `--c2` |
| 03 Watercolour Gardens | Watercolour | `--c3` (plum) |
| 04 Ink, Line & Silence | Ink | `--c4` |
| 05 Plein Air in Oil | Oil | `--c5` |
| 06 Abstract Colour | Acrylic | `--c6` |

### 4.4 Contrast (checked)

Original palette: body text ≥ 15:1, text on the signature band 6.3–10.7:1, course titles on white ≥ 3:1 (large text). Accent fills with white text are fine for large text and icons. **Don't put small body text in `--terra`.**

---

## 5. Typography

| Use | Font | Weight / size / line-height / tracking |
|---|---|---|
| Hero name + line | Inter Tight | 500 · clamp(30, 3.3vw, 56px) · 1.0 · −4.5% |
| Section headings (H2) | Inter Tight | 600 · clamp(40, 5vw, 68px) · 1.0 · −4% |
| About statement | Inter Tight | 500 · clamp(30, 3.5vw, 48px) · 1.08 · −4% |
| **Course card title** | **Inter** | **700 · 36px · 0.86 · −6.5%** (matches Figma) |
| Featured work title | Inter | 700 · clamp(40, 4.6vw, 68px) · 0.88 · −6% |
| Quote | Inter Tight | 500 · clamp(24, 2.4vw, 36px) · 1.12 · −3.5% |
| Body | Inter Tight | 400 · 16px · 1.65 |
| Small body | Inter Tight | 400 · 14–14.5px · 1.5 |
| Labels, facts, captions | JetBrains Mono | 400–500 · 9–10.5px · labels uppercase +6% |
| Signature only | Caveat | 500 · 32–48px |

Rules: emphasis is **colour, never italics** (one phrase per heading). Facts (level, length, dates, prices in cards) always in mono labels + Inter Tight 600 values.

---

## 6. Layout & components

### 6.1 Grid

- Fixed left rail **56px** + **6 columns** with visible 1px lines at 7.5% ink (`.cols`). Side padding `--pad` **48px**, **20px** at ≤ 980px.
- Section padding `clamp(80px, 10vw, 140px)` top and bottom.
- Breakpoints: **1100** (story tweak), **980** (rail hides, single-column sections, 2-up cards), **860 / 760** (two-column layouts stack), **700 / 600** (1-up cards, horizontal swipe rows).

### 6.2 Core components

| Component | Class | Spec |
|---|---|---|
| Primary button | `.btn.btn-ink` | Ink pill, padding 6/6/6/22, 36px round arrow chip. Hover: terracotta fills from the left (.45s), arrow rotates −45°. |
| Nav pill | `.login` style | Ink pill, 8×16px, hover terracotta. |
| Text link | `.link`, `.ulink` | 1px underline, hover accent. |
| Section label | `.lbl` | Mono uppercase, number in accent + 34px rule after. |
| Level meter | `.meter[data-l]` | Three 3px bars (100 / 72 / 44%). Fills from the bottom: `1` beginner, `2` intermediate, `3` advanced. Uses the card accent. |
| Newsletter | `.nl` | White input 60px tall + square accent submit button. |
| CTA card | `.cta-card` | Outlined dark card, 6px radius, underlined action at the bottom. |
| Side tab | `.tabv` | Fixed right, white, vertical text. |

### 6.3 Course card ("Poster white")

`a.pcard` with `style="--pc:var(--cN)"`

1. **Top row**: brand in muted mono, "No. 01 · Pencil" in accent, 1px rule.
2. **Title**: Inter 700 36px, accent colour, always two lines (`<br>`).
3. **Photo**: 3:4, right-aligned, fills remaining height. Grayscale + `mix-blend-mode: screen` over the accent = tinted. Full colour on hover.
4. **Tag** (optional): "New" / "Bestseller", small mono on the photo corner.
5. **Facts**: 2×2 `<dl>` (Level with meter, Lessons, Running, Admission). Top rules 2px, bottom row 1px, in accent.
6. **Card**: ratio **1 : 1.18**, padding 18px, square corners, no shadow, lifts 6px on hover; price shows "→ Enrol" on hover.

Figma equivalent: component **Course card / Poster white** (380×448) + **Level meter** variants; colour via the **Course accent** variable collection (one mode per course).

---

## 7. Interaction & motion

Everything is hover / scroll based. Nothing autoplays or loops.

| Behaviour | Implementation |
|---|---|
| Reveal on scroll | `.reveal` → `.is-in` via one `IntersectionObserver` (threshold .15). Opacity + 28px rise, .9s. Content is visible without JS (`.js` class gate). |
| Line drawing | `.draw` SVG paths with `pathLength="1"` and dash offset. Hero circle 2.4s, hero underline 1.3s after a .9s delay, method icons 1.4s. |
| Hero load | `.hero.is-in` added on load (rAF + 400ms fallback). |
| Hero circle | A second observer toggles `.hero.ring-on` (threshold .35): the circle draws on entry and resets instantly on exit, so it redraws on every return to the top. |
| Phone menu | Menu button toggles `.hn-panel` (`hidden`) and `aria-expanded`; Esc closes and returns focus. |
| Hover | Card lift −6px, image zoom 1.04–1.06, tinted/B&W photos return to colour, button fill. |
| Reduced motion | `prefers-reduced-motion: reduce` disables all animation and transitions and shows everything. |

---

## 8. Accessibility checklist

- [x] Landmarks: `main`, `nav`, `footer`, headings in order per section.
- [x] Decorative SVGs are `aria-hidden`.
- [x] Contrast checked (section 4.4).
- [x] Reduced motion respected.
- [ ] **Alt text:** many placeholder images have `alt=""`. Write real alt text when real artwork goes in.
- [ ] **Focus styles:** rely on browser defaults; add a visible `:focus-visible` ring in the accent.
- [x] Phone menu covers every hero link, uses `aria-expanded`, closes on Esc.
- [ ] Hero nav is not sticky: once you scroll past the hero there is no navigation on desktop. Decide if that's fine or add a small sticky bar.

---

## 9. Content & assets to replace

| Item | Now | Needed |
|---|---|---|
| **Images** | 18 Unsplash placeholders, self-hosted in `img/` | Elena's real portrait (hero, About), studio photos, her **own artwork** for the gallery, real **student work** with permission. About cut-outs: full-length, shot on a white sweep (or transparent PNG). Never present someone else's work as hers. |
| Copy | Written in her voice as a draft | Elena to approve bio, course descriptions and FAQ. |
| Students | Fictional names, quotes, weeks | Real quotes and consent. |
| Numbers | 12,400 students · 3,100 pieces · 4.9 rating / 2,870 reviews · 18 courses · 340h · 64 countries · prices | Real figures. |
| Contact | `hello@elenavarga.art`, Lisbon address | Real details. |
| Favicon | Missing (404 in console) | Add `favicon.ico` / SVG icon. |

---

## 10. Integration work (not designed, needs building)

- **34 links are `href="#"`**: course detail pages, Log in, socials, "See the full wall", gallery works, footer links.
- **Newsletter form**: front-end only (shows "Thanks!"). Connect to the email provider.
- **CTA cards**: "Schedule now" → booking tool; "Reserve a seat" → live-class signup.
- **Courses**: each card → course page and checkout (video platform / LMS).
- **Images**: self-host and serve responsive sizes (`srcset`), keep `loading="lazy"` below the fold.
- If building as a **WordPress theme**: each section maps cleanly to a block or template part, courses and gallery works to custom post types (fields: medium, level, lessons, duration, price, accent, tag, image).

---

## 11. Files in this folder

| Deliverable | Exploration / history (don't build from) |
|---|---|
| `atelier-v7.html`, `style-guide.html`, `poster-card-c.html`, `HANDOFF.md` | `atelier.html`, `atelier-v2…v6.html`, `gallery-reviews-options.html`, `course-cards*.html`, `poster-card-a/b.html`, `student-section-variations*.html`, `selvedge-grid*.html`, `pattern*.html`, `scher*.html`, `concepts.html`, `wireframe.html`, `workflow.html` |

`img/` holds old-master paintings from the first drafts; **v6 doesn't use them.**

---

## 12. QA before launch

- [x] Chosen palette merged into `:root`; picker and other palettes removed.
- [ ] Desktop 1440, laptop 1280, tablet 768, phone 375: no horizontal scroll.
- [x] No Unsplash hotlinks (placeholders self-hosted in `img/`).
- [ ] All images real, compressed, with alt text.
- [ ] Every `#` link wired; forms submit.
- [ ] Lighthouse: performance and accessibility ≥ 90.
- [ ] Reduced-motion and keyboard-only pass.
- [ ] Favicon and social share image added.
