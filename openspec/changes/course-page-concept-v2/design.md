# Design

## Context

`course.html` is one static file (about 780 lines): an inline `<style>`, an SVG icon sprite, the markup, and a short script. Today it holds two headers (`.va` Cinema and `.vb` Cover), shown one at a time by `html[data-hero]`, which a head script sets from the hash before first paint. A fixed `.switch` at the bottom left flips them. The published artifact is built by `tools/build-artifact.py`, which embeds `img/` photos as data URIs. `lesson.html` already holds the enrolled student's data (Marta K., 12/24, topic 4 lesson 1). Requirements are in `specs/course-details` and `specs/course-enrolled-view`.

## Goals / Non-Goals

**Goals:**
- Both views live in one file and share markup wherever the content is the same (curriculum list, About, teacher, reviews).
- The view switch costs nothing on load and doesn't flash.

**Non-Goals:**
- Real persistence (wishlist state, share). Demo behaviour is enough.
- A shared data source between `course.html` and `lesson.html`. Numbers are kept in step by hand.

## Decisions

1. **The view is an attribute on `<html>`.** The existing head script changes to `document.documentElement.dataset.view = location.hash === "#enrolled" ? "enrolled" : "visitor"`. CSS hides view-only blocks with `html[data-view="enrolled"] .v-visitor{display:none}` and the reverse. This is the same pattern as the current hero switch, so there's no first-paint flash. *Alternative:* two separate files (`course.html`, `course-enrolled.html`). Rejected: everything below the hero would be duplicated and drift.
2. **Two hero blocks, not one morphing hero.** `.va` keeps the visitor content. A new `.va.enrolled` block reuses the Cinema band styles and holds: "Welcome back, Marta", a progress line, a "Up next" row with the poster thumbnail and title, and Continue / Course resources buttons. Both live inside `.hx`. *Alternative:* toggling individual elements inside one hero. Rejected because the two layouts differ (no trailer and facts in enrolled).
3. **Remove the Cover header and the `data-hero` logic outright.** `#cinema` and `#cover` fall through to the visitor view. Cover stays documented in `course-heroes.html`.
4. **The sidebar holds two cards**, `.card.v-visitor` (existing, trailer removed) and `.card.v-enrolled` (new Continue card). The Continue card uses the same soft-beige ground, 16px radius and pill buttons, and reuses the washed hand-drawn icons for resources, certificate and Q&A.
5. **Curriculum states come from classes on the shared list.** Each item gets its enrolled state as a class (`is-done`, `is-next`, `is-locked`) and the topic rows carry both meta texts (`.mt .v-visitor` / `.mt .v-enrolled`). The status cell holds both glyphs (lock or preview / tick or "Up next"), shown by view. In the enrolled view, topic 4 is opened when switching; the visitor view keeps topic 1 open.
6. **Wishlist** is a `<button aria-pressed>` that swaps a line bookmark icon (outline ↔ filled ink) and its label "Wishlist" ↔ "Saved". **Share** uses `navigator.share` when available, otherwise copies the URL with `navigator.clipboard` and shows "Link copied" for 2 s. Both sit right-aligned under the facts grid as text links with line icons.
7. **Facts grid** grows from 5 to 6 cells: Rating · Lessons · Length · Level · Students (12,400) · Updated (Oct 2026). Certificate moves out, because the card's "This course includes" list already has it. The 860px rule already turns it into a 2-column grid.
8. **Drawings strip** (`#progress`, "Week 1 → Week 6") is a 3-column grid of pair cards on white. Each card holds two images side by side (Week 1 grey and faded, final drawing at full contrast), a mono label row and the name with the weeks taken. It goes on phones to a horizontal scroll-snap row inside its own `overflow-x:auto` container. The placeholders are small inline SVG pencil studies (egg, mug, pear): a faint, stiff outline for Week 1 and a three-value study with a cast shadow for the final week. *Changed during apply:* the available `img/` photos had no matching before/after subjects, and drawn studies show the course's own lesson (three values) more honestly than mismatched photos. It is not added as a tab.
9. **Phone bar** gets two variants, also by `v-visitor` / `v-enrolled`. The `.switch` keeps its current offset above the bar.

## Risks / Trade-offs

- [Placeholder before/after drawings aren't real student work] → Label the section as placeholder in HANDOFF, and treat the photos as list item 4 ("replace placeholder content").
- [Duplicate hero and card markup grows the file] → Acceptable for a concept. Keep shared sections single.
- [Progress numbers duplicated across two files] → Note in HANDOFF that `lesson.html` and `course.html` share the 12/24 state.
- [Removing Cover closes an open decision on the user's behalf] → Recorded as an assumption in the proposal. Restoring it from git history or `course-heroes.html` is cheap.

## Migration Plan

Edit in place, screenshot both views at 1440px and 390px, check `scrollWidth`, commit, rebuild with `tools/build-artifact.py`, and republish the main artifact with `home.html`, `course.html` and `lesson.html`. Rollback is `git revert` and a republish.
