# Proposal

## Why

The Atelier concept has a home page, a course page (visitor and enrolled) and a lesson page, but nowhere to go from them: half the links are `#`. To read as a complete Tutor LMS theme concept, it needs the rest of the page set. The concept is for a solo instructor (Elena), and it should be easy to convert into an academy with many teachers. Tutor's own themes split the same way: WellThrive is a one-coach site ("I'm James…", services, my approach), Pathwise is a many-mentor academy (teachers archive, categories, "Our vision"). Designing one site that does both, without becoming generic, is the opportunity.

## What Changes

New static pages in `atelier/`, all in the existing design system and cross-linked:
- **Courses** (`courses.html`): the archive, with Elena's poster cards, medium and level filters, sorting and an empty state. Tutor `archive-course.php` + `course-filter/*`.
- **About** (`about.html`): Elena's story, method, qualifications, studio, press and teaching numbers. WellThrive's "About" structure.
- **Services** (`services.html`): portfolio review and live weekly class as two bookable offers, with process, pricing and FAQ. These are the two CTA cards on the home page.
- **Studio notes** (`notes.html` list + `note.html` article): the blog promised by the newsletter.
- **Contact** (`contact.html`): a short form, direct email, studio address and reply times.
- **Log in / Create account** (`account.html`): one page with two tabs, plus a "forgot password" state. Tutor `login.php` / registration.
- **Checkout** (`checkout.html`): order summary, coupon, billing, payment and a success state. Tutor native e-commerce (`ecommerce/checkout.php`); one course, so cart and checkout merge into one step.
- **Student dashboard** (`dashboard.html`): continue learning, my courses with progress, wishlist, quiz attempts, certificates and settings, in the 4.x Modern dashboard order but restyled.
- **Quiz** (`quiz.html`): start screen, one question at a time and a result, inside the learning-area shell of `lesson.html`.
- **Assignment** (`assignment.html`): "Submit for Elena's critique": brief, upload, notes, submitted and reviewed states.
- **Solo / Academy mode across the site:** a review switch (like Visitor / Enrolled), remembered across pages, that turns the solo site into an academy version: "Teachers" in the nav, a teachers page (`teachers.html`), an instructor line on course cards, an instructor filter in the archive, and "About us" instead of "About Elena". The solo version stays the default.
- **One shared header and footer** across the new pages, with real links between all pages. The home and course pages link to the new pages instead of `#`.

The scope and assumptions are recorded in the design. This is a design concept, not a WordPress build. The pages are static HTML/CSS/vanilla JS, and the demo states are switched in the page.

Out of scope: privacy and terms pages, a standalone FAQ page, the instructor dashboard and course builder, real form submission, payments or auth, and redesigning the home, course or lesson pages beyond link fixes and the shared mode switch.

## Capabilities

### New Capabilities
- `site-shell`: shared header, navigation, footer and page set; every page reachable, with no dead primary links.
- `academy-mode`: the solo / academy switch and what each page shows in each mode.
- `course-catalog`: the courses archive, its filters, sorting and empty state.
- `teacher-profile`: the About page in solo mode and the teachers page in academy mode.
- `services`: the bookable offers (portfolio review, live class) and how they are presented.
- `studio-notes`: the blog list and article pages.
- `contact`: the contact page and form states.
- `account-access`: log in, create account and password reset.
- `checkout`: buying a course, from summary to success.
- `student-dashboard`: the enrolled student's home.
- `learning-quiz`: taking a quiz in the learning area.
- `assignment-submission`: submitting work for critique and seeing its review.

### Modified Capabilities
<!-- none: course-details and course-enrolled-view (in course-page-concept-v2, not yet archived) are unchanged apart from link targets -->

## Impact

- New files in `atelier/`: `courses.html`, `about.html`, `teachers.html`, `services.html`, `notes.html`, `note.html`, `contact.html`, `account.html`, `checkout.html`, `dashboard.html`, `quiz.html`, `assignment.html`.
- Edited: `index.html`, `course.html`, `lesson.html`. Nav, footer and CTA links point to the new pages, and the mode switch is added.
- `tools/build-artifact.py`: builds and embeds images for every page, and rewrites `index.html` links to `home.html` in all extra pages. The artifact grows from 3 to about 15 files.
- `HANDOFF-NEXT.md`: page list, links, mode switch and next work.
- No new dependencies.
