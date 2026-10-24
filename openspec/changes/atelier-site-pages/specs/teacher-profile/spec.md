# Spec Delta

## Purpose

Defines how the teaching side of the site is presented: Elena's own About page in solo mode, and a teachers page with individual profiles in academy mode.

## ADDED Requirements

### Requirement: About page (solo)
The About page SHALL tell Elena's story in this order: an opening statement with portrait, her story, what she believes, her method (Look, Sketch, Finish), qualifications and experience, the Lisbon studio, teaching numbers, a note from students, and a closing call to the courses and the free lesson.

#### Scenario: Section order
- **WHEN** the About page opens in solo mode
- **THEN** the sections appear in the order above, with the first-person voice ("I teach…") throughout

### Requirement: About page (academy)
In academy mode the About page SHALL speak as the Atelier ("We teach…"), keep the method and studio sections, replace the qualifications with a teachers preview (three teachers and a link to `teachers.html`), and keep Elena as founder.

#### Scenario: Academy voice
- **WHEN** academy mode is on
- **THEN** the heading and intro use "we", a teachers preview shows three teachers, and Elena is labelled Founder

### Requirement: Teachers page (academy)
`teachers.html` SHALL list the teachers as cards (photo or initial, name, medium, courses count, students, a short line) with a medium filter, and each card SHALL open a profile panel or section with bio, courses and a quote.

#### Scenario: Open a profile
- **WHEN** the visitor opens a teacher card
- **THEN** that teacher's bio, courses (linking to `course.html`) and quote are shown, and focus moves to the profile

#### Scenario: Teachers page in solo mode
- **WHEN** `teachers.html` is opened in solo mode
- **THEN** it explains that this is the academy view and offers a link to switch, rather than showing a broken page
