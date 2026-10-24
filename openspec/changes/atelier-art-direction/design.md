# Design

## Context

The taste is defined by `atelier/atelier-v7.html` (inline CSS, about 470 lines). What it actually uses, measured from its CSS:
- **Radii:** 28px (method room), 22px (that room on phones), 16px (CTA panel, newsletter, footer), 12px (top bar, newsletter field), 999px (buttons), 50% (discs), three irregular paint-pot blobs.
- **Display sizes:** `clamp(40px,5vw,68px)`, `clamp(30px,3.5vw,48px)`, `clamp(22px,2vw,28px)`.
- **Mono:** 9–11px. Labels use `.06em` tracking after the v4 override; the footer uses `.18em` and some leftovers use `.2em`.
- **Motion curves:** objects `cubic-bezier(.2,.7,.2,1)`, lines `cubic-bezier(.6,.1,.2,1)`.
- **Imagery:** `grayscale(1) contrast(1.05–1.18)`, poster mix-blend `screen` over the course colour.
- **Ground:** paper `#FAF6EF` plus a fixed grain overlay at `.14` multiply, with fixed 3-column grid lines at `.075`.
- **Section voice:** chapter labels "02 THE ARTIST ——", and the headlines "Look. Sketch. Paint.", "Six courses, hung like posters.", "Hung in the studio.", "Letters from the wall.", "Before you begin."

Drift found by screenshot review of the other pages:

| Where | Drift | Rule broken |
|---|---|---|
| course.html headings | "About this course", "Curriculum", "Your teacher", "Student reviews" | Headline voice, chapter labels |
| course.html header | white bar, text brand, no strokes mark | Same brand everywhere |
| course.html radii | 14px method cards, 10px thumbnails, 16px cards | Radius scale |
| course.html mono | 10.5/11px at `.06em`, the home footer at `.18em` | One label style |
| course.html bands | beige bands (drawings strip, more courses) without grain or grid | Reading archetype: grain and grid inside beige bands |
| lesson.html | 10px item radius, 12px compose field, display H1 at 48px | Radius scale; Workroom has no display headlines |
| home | `.2em`/`.18em` tracking leftovers, `--muted` contrast `#8A8172` on paper is 3.6:1 | Label style; contrast |

The full rules are in this change's `specs/`.

## Goals / Non-Goals

**Goals:**
- One token source (`assets/site.css` `:root`) that matches the home page's look exactly.
- Every page states its archetype and passes the same audit.
- Realign the course and lesson pages without undoing the user's earlier decisions: white course ground, light beige card, line ticks, no pill badges, tabs under the header, safe gaps.

**Non-Goals:**
- Moving the home page's CSS into `site.css` now. The home keeps its inline CSS. It only gets token-name clean-ups and the muted-contrast fix, and it must render pixel-identical apart from that.
- New pages (those come in `atelier-site-pages`, which now depends on this change).

## Decisions

1. **Tokens are named by role, not colour.** `--paper`, `--object`, `--room`, `--ink`, `--ink-2`, `--muted` (raised to `#6E6658` for 4.5:1 on paper), `--accent`, `--accent-on-dark`, `--block-1/2/3`, `--c1…c6`, `--rule`, `--grid`. Plus `--r-room:28px`, `--r-card:16px`, `--r-field:12px`, `--r-pill:999px`, the type steps `--t-display/h2/h3/lead/body/small/mono`, the spacing steps `--s1…s10`, and `--ease-object`/`--ease-line`. *Alternative:* keep the per-page literal values. Rejected because that is how the drift happened.
2. **Components in `site.css` are copied from the home page's CSS and generalised, not redrawn:**
   - `.chapter` (from `.lbl`);
   - `.headline` (with `<em>` as the accent phrase, from `h2 em`);
   - `.room`;
   - `.poster` (from `.pcard`);
   - `.steps` / `.block` (from `.step`);
   - `.faq-book`;
   - `.btn` / `.btn-ink` / `.btn-line` (from `.btn` and `.cta-card .u`);
   - `.field`;
   - `.facts` (from the course facts grid);
   - `.tabs`;
   - `.review-bar`;
   - `.grain` and `.gridlines` as opt-in layers.
3. **Archetype hooks.** `body[data-archetype]` turns on the right layers: Gallery gets grain and gridlines, Reading gets them only inside `.band`, and Workroom and Counter get neither. Each page declares its archetype, so `site.css` can't apply grain to a tool screen by mistake.
4. **Course page headlines (copy set):**

   | Chapter label | Headline |
   |---|---|
   | 01 About | "Learn to look before you draw." |
   | 02 Curriculum | "Six topics, one drawing at a time." |
   | 03 Teacher | "Taught by Elena, at her own table." |
   | 04 Progress | "Week 1, then week 6." |
   | 05 Reviews | "Letters from students who finished." |
   | 06 Before you enrol | "Before you begin." |

   The tab labels stay short nouns, because tabs are navigation, not statements. The h2 size moves to the h2 step (`clamp(30px,3.5vw,48px)`). *Alternative:* keep the nouns. Rejected, because nouns as headlines are the clearest drift from the home page's voice.
5. **Brand mark everywhere.** The home's strokes logo (three coloured 3×13px bars and "Elena Varga") replaces the text-only brand in the course page header, and becomes the shared header's brand.
6. **Lesson page stays a Workroom.** The H1 drops to the h3 step plus weight, and radii go to the scale (10 → 12 for item rows, 12 kept for fields, 16 for the video). No grain, grid or reveal is added.
7. **Audit script** (`tools/audit.mjs`, Playwright). It reads computed styles of all visible elements, so values come from the browser, not from parsing CSS. It checks against the scale tables exported from `site.css` comments, lists offenders by selector, and exits non-zero on blocking items. Contrast is computed from the text colour and the nearest opaque background.
8. **Style page** is a Gallery page assembled from `site.css` samples. Its "don't" side uses an inline `.dont` wrapper with a struck caption, so the bad examples are visibly marked and never reused.
9. **Order of work:** tokens and components → audit → style page → realign the course page → realign the lesson page → home clean-ups → update the `atelier-site-pages` plan → publish. The audit lands before any realignment, so every later step is measured.

## Risks / Trade-offs

- [Rewriting course headlines changes copy the user has reviewed] → Tab labels and section order stay. The headlines are shown in the summary for approval, and each one is a one-line revert.
- [The home page must not change visibly] → Screenshot it before and after at both widths, and diff the images. Any visible pixel change other than the muted text colour fails the task.
- [Audit false positives (paint pots, poster captions)] → An allow-list with a reason per selector lives in the audit file and on the style page.
- [`atelier-site-pages` was planned against course-page tokens] → Its design decision 1 and task 1.1 are rewritten in this change, before any of it is built.

## Migration Plan

Each step is committed separately, the audit is run, then build and publish. Rollback is a per-commit revert. The two in-flight changes are archived in order: `course-page-concept-v2`, then this one, then `atelier-site-pages`.
