# Spec Delta

## Purpose

Defines how the course details page changes for an enrolled student returning to the course: progress in the header, a Continue card in place of the enrol card, curriculum states, and the review switch between visitor and enrolled views.

## ADDED Requirements

### Requirement: Visitor / Enrolled review switch
The course page SHALL show a small fixed switch at the bottom left with two options, Visitor and Enrolled, that changes the page between the two views without reloading. The chosen view SHALL be reflected in the URL hash (`#visitor`, `#enrolled`) and restored from it on load.

#### Scenario: Switch to enrolled
- **WHEN** the reviewer selects Enrolled
- **THEN** the page shows the enrolled view, the hash becomes `#enrolled`, and the Enrolled option shows as pressed

#### Scenario: Open by hash
- **WHEN** the page is opened with `#enrolled`
- **THEN** the enrolled view is shown on first paint without a flash of the visitor view

#### Scenario: Switch on phones
- **WHEN** the page is 390px wide in either view
- **THEN** the switch does not cover the fixed bottom bar or its buttons

### Requirement: Enrolled header
In the enrolled view the header SHALL greet the student by first name, show course progress as items done out of total with a bar and percentage, name the next lesson, and offer a primary Continue button. It SHALL NOT show price or Enrol buttons.

#### Scenario: Welcome back
- **WHEN** the enrolled view is shown for Marta K. with 12 of 24 items done
- **THEN** the header reads "Welcome back, Marta", shows "12 of 24 done" with a 50% bar, and the Continue button names "Three values, not seven"

### Requirement: Progress data consistent with the lesson page
The enrolled view SHALL use the same progress state as the lesson page: topics 1–3 complete, topic 4 lesson 1 current, 12 of 24 items done.

#### Scenario: Same numbers
- **WHEN** the reviewer compares the enrolled course page with `lesson.html`
- **THEN** the done count, percentage, current item and topic states match

### Requirement: Continue card replaces the enrol card
In the enrolled view the sidebar card SHALL show the next lesson (topic, title, duration, poster image) with a Continue button linking to `lesson.html`, the course progress, the date enrolled, and links to course resources and the certificate status. It SHALL NOT show price, refund or gift lines.

#### Scenario: Continue
- **WHEN** the enrolled student activates Continue in the card or header
- **THEN** the browser opens `lesson.html`

#### Scenario: Certificate status
- **WHEN** the course is not yet complete
- **THEN** the card shows the certificate as locked with how many items remain

### Requirement: Curriculum shows progress states
In the enrolled view each curriculum item SHALL show one of: done (line tick), current (marked "Up next" in the course accent), or open (no lock). Topic rows SHALL show "n of m done". The final critique assignment SHALL show as locked until the final drawing is done.

#### Scenario: Topic states
- **WHEN** the enrolled view is shown
- **THEN** topics 1–3 read "4 of 4 done", topic 4 is expanded with "Three values, not seven" marked Up next, and no lock icons appear except on the critique assignment

#### Scenario: Visitor states unchanged
- **WHEN** the reviewer switches back to Visitor
- **THEN** the curriculum shows the free preview label and locks as before

### Requirement: Phone bottom bar follows the view
On phones the fixed bottom bar SHALL show price and Enrol in the visitor view, and progress and Continue in the enrolled view.

#### Scenario: Enrolled bottom bar
- **WHEN** the enrolled view is shown at 390px
- **THEN** the bottom bar shows "50% · 12 of 24" and a Continue button linking to `lesson.html`
