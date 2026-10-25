# Proposal

## Why

The home page has a distinct taste: an artist's studio presented as a gallery. It has numbered chapter labels, sentence headlines that land on a terracotta phrase, a drawing grid and construction circles, grey photographs that turn to colour when touched, poster cards, mono museum captions, a handwritten signature, paper grain, and slow drawn-line motion. That taste lives only in one file's CSS and in our heads. The course and lesson pages already drift from it:
- generic headings ("Curriculum", "Student reviews");
- no chapter labels;
- a plain white header with a text-only brand;
- radii of 10, 14 and 16px where the home page uses 12, 16 and 28px;
- three different letter-spacings on mono labels;
- no grain or drawing grid.

Twelve more pages are planned (`atelier-site-pages`). Without a written art direction they would drift further, one reasonable decision at a time. This change sets the taste down as rules, at every scale from a 1px rule to a whole page, and makes every page answer to it.

## What Changes

- **A written design language**, derived from the home page and not invented:
  - principles;
  - tokens (colour, type scale, spacing, radii, rules, motion);
  - the drawing grid;
  - imagery treatment;
  - the voice of headlines and captions;
  - micro-details (punctuation, numerals, arrows, icon drawing).
- **Page archetypes**, so the same language flexes by purpose instead of drifting:
  - **Gallery** (home, about, services, courses, notes list): beige paper, chapter labels, display headlines, grid lines, grain.
  - **Reading** (course detail, article): a white page like a printed sheet, beige used only for objects. This keeps the user's earlier "too much beige" feedback on the course page.
  - **Workroom** (lesson, quiz, assignment, dashboard): quiet tool screens in the same type and colour, without ornament.
  - **Counter** (account, checkout, contact): the calm forms where people commit.
- **A living style reference page** (`style.html`) in the artifact. It shows every token and component in its real CSS, with do and don't pairs, so the user can review the system itself.
- **Shared CSS made from the home page**: `assets/site.css` tokens come from the home page, not the course page. **BREAKING** for the plan in `atelier-site-pages`: its design decision 1 changes from "the course page's tokens" to "the design language tokens".
- **The existing pages brought in line:**
  - Course page: chapter labels and voiced headings, the brand mark and nav from the home page, the radius scale, one mono label style, and grid lines on its beige bands. The white ground stays.
  - Lesson page: same type, radius and label alignment, keeping the Workroom calm.
  - Home page: only token clean-ups that change nothing visible.
- **An art-direction review gate**: a written checklist (macro, meso, micro) and a scripted audit (tokens used, radii, shadows, label style, contrast, overflow). Every page must pass it before it's published.

Out of scope: new pages (they stay in `atelier-site-pages`, which will be built on this language), changing the palette or typefaces, and dark mode.

## Capabilities

### New Capabilities
- `design-language`: the Atelier's visual and verbal rules: principles, tokens, grid, imagery, voice, micro-details and motion.
- `page-archetypes`: the four page kinds (Gallery, Reading, Workroom, Counter) and what each must and must not use.
- `style-reference`: the published style reference page that demonstrates the language.
- `design-review`: the review checklist and scripted audit every page must pass before publishing.

### Modified Capabilities
<!-- none in openspec/specs/ yet. course-details (course-page-concept-v2) and the specs in atelier-site-pages are not archived; their pages are brought in line through the requirements here. -->

## Impact

- New: `style.html`, `assets/site.css` (the language's tokens and components), `tools/audit.mjs` (scripted review).
- Edited: `course.html` (labels, headings, brand/nav, radii, label style, band grid), `lesson.html` (radii, labels), `index.html` (token variables only, no visible change).
- `openspec/changes/atelier-site-pages/design.md`: decision 1 re-pointed to this language, and every page task gets the review gate.
- `HANDOFF.md` / `HANDOFF-NEXT.md`: the language summary replaces the stale "Design system" section.
- `tools/build-artifact.py`: includes `style.html` and `assets/`.
