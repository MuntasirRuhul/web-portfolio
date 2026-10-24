# Tasks

**Desktop first (user decision, 24 Oct):** build and check every page at 1440px first (`audit.mjs --desktop`); phone and tablet layouts are a separate pass in group 6.

**Standard check** for every page task: Playwright (`/opt/node22/lib/node_modules/playwright/index.mjs`) screenshots at 1440px and 390px in solo and academy mode; no page errors; `scrollWidth` equals the viewport width; `node atelier/tools/audit.mjs <page> --strict-links` exits 0 (no shadows, scale radii, curly quotes, contrast, alt text, no `#` primary links), and the art-direction review checklist in `atelier/HANDOFF-NEXT.md` is walked. Each group ends published, so the user can comment before the next one.

## 1. Shared shell and mode switch

- [x] 1.1 Extend `atelier/assets/site.css` (from `atelier-art-direction`) with the phone menu dropdown and the `.m-solo` / `.m-academy` mode rules, and create `atelier/assets/site.js` (menu, mode head logic helper, review bar with mode plus optional `data-states`, form helper, tabs helper). Verify with a scratch page that uses every component and passes the standard check.
- [ ] 1.2 Add the mode head script and `site.js` to `atelier-v7.html`, `course.html` and `lesson.html`; move the course page's Visitor / Enrolled switch into the shared review bar. Verify `?mode=academy` persists across the three pages, storage blocked still renders solo, and the course-page checks from `course-page-concept-v2` still pass (hash views, 23/1 locks, Continue links).
- [ ] 1.3 Extract the learning-area CSS from `lesson.html` into `atelier/assets/learn.css` and link it. Verify `lesson.html` screenshots at both widths match the pre-change screenshots pixel for pixel or by visual review.
- [ ] 1.4 Extend `tools/build-artifact.py` to take the page list, embed images per page, rewrite home links, and copy `assets/`. Verify it writes every listed page plus `site/assets/*` and prints sizes.

## 2. Courses and teaching pages

- [x] 2.1 Build `courses.html`: header, intro, medium and level filter rows, sort select, count line, six poster cards with `data-*` attributes, empty state, footer; academy teacher filter and teacher lines. Verify that Watercolour + Beginner shows 1, Oil + Beginner shows the empty state, Clear filters restores 6, Price low to high orders $69 → $129, the count is announced, and the standard check passes.
- [x] 2.2 Build `about.html` with the solo section order and the academy variant (we-voice, teachers preview, Elena as founder). Verify the solo order matches the spec, the academy shows three teachers and a link to `teachers.html`, and the standard check passes.
- [ ] 2.3 Build `teachers.html`: four teacher cards, a medium filter, an in-page profile with bio, courses and quote, and a solo-mode notice with a switch link. Verify that opening a card moves focus to its profile, the course links go to `course.html`, solo mode shows the notice, and the standard check passes.
- [ ] 2.4 Add academy teacher lines to the poster cards on `atelier-v7.html` and `course.html` ("Where students go next"), and add Teachers / About us to the shared header in academy mode. Verify the solo audit (no other teacher names, no `teachers.html` links) and the academy header order.
- [ ] 2.5 Build, publish, and update `HANDOFF-NEXT.md` (page list and the mode switch). Verify the publish reports a new version and the handoff lists the new pages.

## 3. Services, notes and contact

- [ ] 3.1 Build `services.html`: two offers, a review process as step cards, a live-class block, the booking panel with slots and a confirmation, and the services FAQ with the book icon. Verify that booking a slot shows the confirmation naming it, the FAQ icon swaps, and the standard check passes.
- [ ] 3.2 Build `notes.html` (featured note, six or more notes, category filter with count, newsletter) and `note.html` (article layout, pull quote, figure, related course card, keep reading, newsletter). Verify the Materials filter, the newsletter's valid and invalid states, 17px or larger body text on phones, and the standard check on both pages.
- [ ] 3.3 Build `contact.html`: quick answers, the form with topic select, inline validation, a sent state naming the email, and direct email, city and reply time. Verify that an empty email shows a linked error and focuses it, a valid submit shows the sent text (with the we-voice in academy mode), and the standard check passes.
- [ ] 3.4 Point the home CTA cards to `services.html` and the footers' Studio notes and Contact links to the new pages. Build, publish and update the handoff. Verify the link audit has no `#` in primary links for groups 1–3.

## 4. Account and checkout

- [ ] 4.1 Build `account.html`: split layout, Log in / Create account tabs (`#login`, `#register`), password show/hide, strength hint, reset form and sent state; a valid log in goes to `dashboard.html`, register to `dashboard.html?welcome=1`. Verify each hash, each validation error, both redirects (checking the URL), and the standard check.
- [ ] 4.2 Build `checkout.html`: summary with gift toggle and coupon (`STUDIO10` gives 10%, others show an error), details, payment choice, refund line, and a success state with Start learning → `lesson.html`. Verify the coupon maths ($79 → $71.10), the required-field errors and focus, the success state link, and the standard check (summary first on phones).
- [ ] 4.3 Link Log in buttons on all pages to `account.html` and Enrol now (course page hero, card, phone bar) to `checkout.html`. Build, publish and update the handoff. Verify with a link audit across all pages.

## 5. Student area

- [ ] 5.1 Build `dashboard.html`: greeting, Continue card (12/24, `lesson.html`), live class, totals, pending items, side menu sections (Home, My courses with In progress / Completed tabs, Wishlist, Quiz attempts, Certificates, Settings), and the `?welcome=1` state. Verify that each section switches with the current state marked, the welcome card replaces Continue, the numbers match `lesson.html`, and the standard check passes (horizontal menu on phones).
- [ ] 5.2 Build `quiz.html` on `learn.css`: sidebar with "Spot the edges" current, intro screen, 8 questions (true/false, image choice, multiple choice, ordering), progress, result with review, Retake and Continue. Verify a full keyboard-only run to the result, a pass and a fail path against 70%, and the standard check.
- [ ] 5.3 Build `assignment.html` on `learn.css`: brief and photo tips, upload with previews and drag-and-drop (JPG/PNG, at most 3, 10 MB each), note, Submitted state, and a Reviewed state through the review bar. Verify that a PDF is rejected inline, two images submit to the Submitted list, Reviewed shows the critique and the unlocked certificate, and the standard check passes.
- [ ] 5.4 Link the lesson sidebar's quiz and assignment items and the dashboard items to the new pages. Build, publish and update the handoff (next work, open decisions). Verify the final link audit across all 15 pages: every relative link resolves and no primary link is `#`.

## 6. Phone and tablet pass

- [ ] 6.1 Lay out every new page for tablet (768–1024px) and phone (390px), and run the standard check at those widths. Verify `audit.mjs` (without `--desktop`) passes for all pages.

## Workflow follow-up

- Collect the user's artifact comments per group, then archive `course-page-concept-v2` and this change with `/opsx:archive`.
