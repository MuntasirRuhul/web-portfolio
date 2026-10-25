# Proposal

## Why

The course page (`course.html`) is designed only for a visitor who hasn't bought yet, but a real Tutor LMS course page is seen most often by enrolled students coming back. Comparing it with Tutor LMS 4.1.1's `single-course.php` also showed gaps a reviewer would notice: no wishlist or share, no student count or update date, a "Questions" section whose name clashes with Tutor's enrolled-only Q&A, and a review-only header switch that shows the trailer and price twice. This is a design concept, not a build, so the aim is a credible concept, not field-for-field parity.

## What Changes

- **Enrolled view of the course page.** The same page gets a second state for an enrolled student (Marta K., 12 of 24 items done, same data as `lesson.html`):
  - the hero says "Welcome back" and shows progress;
  - the enrol card becomes a "Continue" card for the next lesson, linking to `lesson.html`;
  - the curriculum shows done ticks, the current item and open items where it showed locks.
  - A small review switch at the bottom left toggles **Visitor / Enrolled** (`#visitor` / `#enrolled`), replacing the header switch.
- **One header: Cinema.** **BREAKING** (for the review page only): the Cover header and the Cinema/Cover switch are removed from `course.html`. Cover stays on record in `course-heroes.html`. The enrol card drops its trailer image so the trailer appears once, in the hero.
- **Small additions in the visitor view:**
  - Wishlist and Share as quiet text links in the hero;
  - students enrolled and "Updated Oct 2026" in the facts grid;
  - the course medium (Pencil) as a mono label above the title.
- **Rename** the "Questions" section and tab to **"Before you enrol"**, so the name stays free for Tutor's student Q&A.
- **New "Week 1 → Week 6" strip** of student drawings, placed before the reviews. It shows each student's first and final drawing side by side, with name and weeks taken. The photos are placeholders.

Assumptions recorded (the user can flip either before apply): Cinema was picked over Cover, and the drawings strip is in this change rather than deferred.

Out of scope: the course-full and free states of the card, playing the free lesson inside the card, a six-week calendar view, the home page and the lesson page beyond keeping their data consistent.

## Capabilities

### New Capabilities
- `course-details`: what the course details page shows a visitor: header, facts, actions, section order and names, the enrol card, and the student-drawings proof strip.
- `course-enrolled-view`: how the course details page changes for an enrolled student: progress in the hero, the Continue card, curriculum states, and the Visitor / Enrolled review switch.

### Modified Capabilities
<!-- none: no specs exist yet -->

## Impact

- `course.html`: markup, CSS and the small inline script (switch, tabs, curriculum).
- `tools/build-artifact.py`: no change expected; the published artifact is rebuilt and republished.
- `HANDOFF-NEXT.md`: course page section, open decision 1 (header) closed, and the switch description.
- `course-heroes.html`: untouched, keeps the Cover option on record.
- No dependencies added. Static HTML/CSS/vanilla JS, Google Fonts, same tokens.
