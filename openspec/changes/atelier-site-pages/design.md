# Design

## Context

`atelier/` holds three finished pages with fully inline CSS/JS: `index.html` (home, own dark-hero nav, beige ground), `course.html` (white ground, light header, Visitor / Enrolled switch), `lesson.html` (learning-area shell). There is no build step except `tools/build-artifact.py`, which embeds `img/*.jpg` as data URIs and writes `site/*.html` for the multi-file artifact. Tokens are duplicated per page. Reference structure comes from the captured Tutor demos in `research/tutorlms/` (WellThrive: solo coach, About = story / beliefs / qualifications / approach / FAQ; Pathwise: academy, About = vision / values / educators, `instructors` archive, category archive, signup, cart) and the Tutor 4.1.1 templates (`archive-course.php`, `login.php`, `ecommerce/checkout.php`, `dashboard/*`, `learning-area/quiz/*`, `single-assignment.php`). Requirements are in this change's `specs/`.

## Goals / Non-Goals

**Goals:**
- Twelve new pages share one shell and one place for tokens, so later edits happen once.
- Solo / academy is a presentation switch over the same markup, not two sites.
- Each page has its demo states reachable without a backend.

**Non-Goals:**
- Refactoring the three existing pages onto the shared CSS. They only get link fixes, the shared script for the mode switch, and `lesson.html` gets the extracted learning-area CSS.
- A templating step or JSON data source. Content stays as static markup.

## Decisions

1. **Shared assets: `assets/site.css` and `assets/site.js`.** `site.css` already exists from `atelier-art-direction`: the design language's tokens (taken from the home page, not the course page), base, brand mark, light header, footer room, chapter label and headline, room, colour blocks, poster card, book FAQ, buttons, facts, tabs, forms and the review bar. This change *extends* it (menu dropdown, mode classes) rather than creating it, and every page declares `<body data-archetype>` per the `page-archetypes` spec (Gallery: courses, about, teachers, services, notes; Reading: note; Workroom: dashboard, quiz, assignment; Counter: account, checkout, contact). `site.js` holds the menu toggle, the mode switch, the review bar and small helpers (form validation messages, tabs). New pages link both and add page-only CSS inline. *Alternative:* inline everything like today. Rejected because twelve copies of the header and footer would drift on the first comment.
2. **Learning-area CSS goes to `assets/learn.css`.** It's extracted from `lesson.html` (header, sidebar, bottom bar, tabs) and used by `lesson.html`, `quiz.html` and `assignment.html`. Before/after screenshots of `lesson.html` must match.
3. **Mode is an attribute on `<html>`.** A two-line inline head script sets `data-mode` from `?mode=` first, then `localStorage['atelier-mode']` (in try/catch), else `solo`, before first paint. CSS shows `.m-solo` / `.m-academy` blocks. `site.js` writes the choice back on switch. Each page keeps its own other states (course: `data-view`, account: tabs) independent of mode.
4. **One review bar per page.** `site.js` renders a single fixed bottom-left bar: "Mode: Solo | Academy", plus the page's own state segment when `<body data-states="…">` declares one (for example `visitor,enrolled` on the course page, `brief,submitted,reviewed` on the assignment page). The course page's existing switch moves into this bar, so there's never more than one floating control. The bar's phone offset clears any fixed bottom bar, as today.
5. **Academy content set.** Four teachers: Elena Varga (founder; Pencil 01, Graphite 02), Tomás Reis (Watercolour 03), Ana Lobo (Ink 04), Jonas Weber (Oil 05, Acrylic 06). Initials stand in for portraits except Elena's existing photo. Course cards carry `data-medium`, `data-level`, `data-price`, `data-hours`, `data-new`, `data-teacher` for filtering and sorting.
6. **Archive filtering in place.** All six cards are in the HTML (it works without JS). Filters are `<button aria-pressed>` in two text rows, sort is a native `<select>`, and a `role="status"` count line announces results. The empty state is a hidden block shown when the count is 0.
7. **Page patterns reused, not invented:**
   - About opens with a portrait and statement, and uses the home page's step cards for the method.
   - Services uses the home CTA card language for its two offers, and the step cards for the process.
   - Notes and the article are editorial, in a 680px column.
   - Account is a split layout: studio photo on the left, card on the right; stacked on phones.
   - Checkout has the summary on the right on desktop and first on phones.
   - The dashboard has a 240px side menu and content (Tutor 4.x Modern order), with a horizontal menu on phones.
   - Quiz and assignment use the `lesson.html` shell.
8. **Demo-only behaviour is honest.** Forms validate and switch to a sent or success state but post nothing. Payment fields are plain inputs labelled as demo. The coupon `STUDIO10` is the only accepted code.
9. **Links.** Home: Log in → `account.html`, courses "All" → `courses.html`, CTA cards → `services.html`, newsletter stays in-page, FAQ "Free lesson" → `lesson.html`. Course page: Enrol now → `checkout.html`, Log in → `account.html` (was `lesson.html`), header nav → the new pages. Lesson page: quiz and assignment sidebar items → `quiz.html` / `assignment.html`. Footers point to real pages.
10. **Build script.** `build-artifact.py` takes a list of pages, embeds images in each, rewrites `index.html` → `home.html`, copies `assets/*` to `site/assets/`, and prints sizes. Publish sends every page and asset in one call.

## Risks / Trade-offs

- [Twelve pages is a large change] → Tasks are grouped so each group ends in a reviewable, published state. The user can comment between groups or trim groups before apply.
- [Placeholder photos are reused on many pages] → Accepted for a concept. Teachers other than Elena use initials, so no stock face pretends to be a named person.
- [The shared script now runs on the existing pages] → It only adds the review bar and mode attribute. The course page's own view switch is moved into the bar, and it's re-tested with the existing course-page checks.
- [Artifact size grows with repeated embedded images] → Pages embed only the images they use. Check the total stays under the 64 MB per-publish limit (today about 3 MB).

## Migration Plan

Build and publish group by group (shell first). Each publish updates the same main artifact, adding pages. Rollback is `git revert` of a group and a republish.

## Open Questions

- Real teacher names and portraits for academy mode can replace the four demo teachers later. That doesn't change the pages.
