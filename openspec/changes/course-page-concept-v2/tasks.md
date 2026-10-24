# Tasks

Verification for every visual task: Playwright screenshots of `atelier/course.html` at 1440px and 390px (import from `/opt/node22/lib/node_modules/playwright/index.mjs`), no page errors, and `document.documentElement.scrollWidth` equal to the viewport width.

## 1. One header and the view switch

- [ ] 1.1 Remove the Cover header (`.vb`), its CSS and the `data-hero` head script and switch. Verify the page opens with the Cinema header at `#`, `#cinema` and `#cover`, with no console errors.
- [ ] 1.2 Add the `data-view` head script, the `.v-visitor` / `.v-enrolled` CSS rules and the bottom-left Visitor / Enrolled switch with `aria-pressed` and hash sync. Verify that clicking toggles the hash and the attribute, that loading `#enrolled` shows the enrolled view on first paint, and that at 390px the switch sits above the phone bar.

## 2. Visitor view additions

- [ ] 2.1 Add the "Course 01 · Pencil" mono label above the title, and grow the facts grid to Rating · Lessons · Length · Level · Students · Updated (Certificate stays in the card list). Verify on screenshots at both widths that the grid stays 6 across on desktop and 2 across on phones.
- [ ] 2.2 Add the Wishlist (`aria-pressed`, Wishlist ↔ Saved) and Share (native share, or copy with a "Link copied" note) text links with line icons. Verify by clicking each in Playwright and checking the label and `aria-pressed` change.
- [ ] 2.3 Remove the trailer image from the visitor enrol card. Verify the card starts with the price and that the trailer appears once on the page.
- [ ] 2.4 Rename the Questions tab and section to "Before you enrol" (id `before`). Verify that the tab scrolls to the section and that no "Questions" or "Q&A" label remains for it.
- [ ] 2.5 Build the "Week 1 → Week 6" strip before the reviews: three pair cards with alt text, week labels, names and weeks taken. On phones it becomes a scroll-snap row in its own container. Verify the placement and that the 390px page has no overflow.

## 3. Enrolled view

- [ ] 3.1 Add the enrolled Cinema hero: "Welcome back, Marta", "12 of 24 done" with a 50% bar, the Up next row ("Three values, not seven", 19:40, poster) and a Continue button to `lesson.html`; no price or Enrol. Verify on an `#enrolled` screenshot that Continue's `href` is `lesson.html`.
- [ ] 3.2 Add the Continue card in the sidebar: next lesson, progress, date enrolled, a resources link, certificate "locked · 12 items to go", and no price, refund or gift lines. Verify on screenshots at both widths.
- [ ] 3.3 Add enrolled curriculum states: done ticks for topics 1–3 ("4 of 4 done"), topic 4 opened with "Up next" on lesson 1, no locks except on the critique assignment, and the visitor states unchanged. Verify by switching views in Playwright and counting the lock icons visible in each view (visitor: all locked items; enrolled: 1).
- [ ] 3.4 Add the enrolled phone bar ("50% · 12 of 24" and Continue to `lesson.html`). Verify on the 390px `#enrolled` screenshot.
- [ ] 3.5 Cross-check the numbers with `lesson.html` (done count, percentage, current item, topic states). Verify by reading both files' values side by side.

## 4. Integration and handoff

- [ ] 4.1 Audit both views at 1440px and 390px against the design system rules (no shadows, line ticks, no pill badges for counts or tags, palette only). Verify by grepping the new CSS for `box-shadow` and by reviewing the screenshots.
- [ ] 4.2 Update `atelier/HANDOFF-NEXT.md`: the course page section, open decision 1 closed as Cinema (with Cover in `course-heroes.html`), the Visitor / Enrolled switch, the shared 12/24 state and the placeholder drawings. Verify the file no longer mentions the Cinema/Cover switch as current.
- [ ] 4.3 Commit, push, run `tools/build-artifact.py` from a scratch folder, and republish the main artifact with `home.html`, `course.html` and `lesson.html`. Verify the publish result reports a new version.

## Workflow follow-up

- Collect the user's artifact comments on both views, then archive with `/opsx:archive`.
