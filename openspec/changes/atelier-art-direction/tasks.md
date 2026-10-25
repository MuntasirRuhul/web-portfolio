# Tasks

**Standard check:** Playwright (`/opt/node22/lib/node_modules/playwright/index.mjs`) screenshots at 1440px and 390px, before and after, looked at side by side. No page errors, and `scrollWidth` equals the viewport width.

## 1. Tokens and components

- [x] 1.1 Create `assets/site.css` with the role-named tokens (colour, type steps, spacing, radii, rules, motion curves) and scale-table comments, copied from the home page's measured values, with `--muted` at `#6E6658`. Verify every token value against the home CSS (list each with its source line) and check `--muted` contrast is at least 4.5:1 on paper and on white.
- [x] 1.2 Add the components to `site.css`: chapter, headline, room, poster, steps/block, faq-book, btn variants, field with error, facts, tabs, review-bar, grain, gridlines, and the `body[data-archetype]` hooks. Verify with a scratch page that renders each one next to its home-page original and matches by screenshot.

## 2. Review gate

- [x] 2.1 Write `tools/audit.mjs`: archetype, overflow, page errors, off-scale font sizes and radii, shadows, straight quotes and " - " separators, contrast, missing alt, `#` primary links; an allow-list with reasons; non-zero exit on blocking items. Verify it fails on a scratch page with a planted shadow, a 14px radius and a straight-quote headline, and passes once they're removed.
- [x] 2.2 Run the audit on `index.html`, `course.html` and `lesson.html` and save the baseline report to `tools/audit-baseline.txt`. Verify the report lists the drift items from the design's table.
- [x] 2.3 Write the review checklist (macro, meso, micro) into `HANDOFF-NEXT.md` and replace its stale "Design system" section with a summary of the language. Verify the handoff no longer contradicts the specs (ground colours, radii, label style).

## 3. Style reference

- [x] 3.1 Build `style.html` (Gallery) with the eleven chapters, live samples from `site.css`, do / don't pairs, contrast ratios, a motion replay, and archetype thumbnails. Verify that the audit passes, every sample uses `site.css` classes, focus rings show when tabbing the Components chapter, and the standard check passes.

## 4. Realign existing pages

- [x] 4.1 Course page: link `site.css`, declare `data-archetype="reading"`, add chapter labels and the headlines from design decision 4, use the strokes brand mark, put radii on the scale, use one mono label style, add grain and gridlines inside the beige bands, and keep the white ground, beige card, tabs, ticks and safe gaps. Verify that the audit passes for the course page, both views (`#visitor`, `#enrolled`) pass the standard check, and the `course-page-concept-v2` checks still hold (23/1 locks, Continue links, 64px card gap, single tab line).
- [x] 4.2 Lesson page: declare `data-archetype="workroom"`, move the H1 to the h3 step, put radii on the scale, and use the shared label style. Verify the audit passes for the lesson page and the standard check shows only those changes.
- [x] 4.3 Home page: declare `data-archetype="gallery"`, set `--muted` to `#6E6658`, align the `.18em`/`.2em` tracking leftovers to `.06em` only where the audit flags them, and add the Style link in the footer base row. Also fix the audit's blocking items with the smallest visible change: CTA card radius 14 → 16; curly quotes; the italic “see” set in weight 600; `--accent-text` for small terracotta text; full-strength white text on terracotta blocks; full-opacity student-card captions; and the live dot ring and menu icon redrawn without `box-shadow` (no visible change). Verify the audit passes and the before/after diff shows only these listed changes.
- [x] 4.4 Add a Style link to the footers of the course page and `style.html`. Verify each footer's Style link opens `style.html`.

## 5. Hand over to the site pages plan

- [x] 5.1 Update `openspec/changes/atelier-site-pages/design.md`: decision 1 uses this language's `site.css` (from the home page), each page states its archetype (per `page-archetypes`), and the standard check includes `tools/audit.mjs`. Update its `tasks.md` 1.1 to "extend `site.css`" instead of "create". Verify with `openspec validate atelier-site-pages --strict` and by reading the changed lines.
- [x] 5.2 Add `style.html` and `assets/` to `tools/build-artifact.py`, build, and publish the main artifact. Verify the publish reports a new version and `style.html` opens from a footer in the artifact.

## Workflow follow-up

- After the user's review of `style.html` and the realigned pages, archive `course-page-concept-v2` and then this change with `/opsx:archive`.
