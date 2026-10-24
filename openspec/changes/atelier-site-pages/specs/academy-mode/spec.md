# Spec Delta

## Purpose

Lets the solo-instructor concept be shown as a multi-teacher academy, so anyone adopting the theme can see both setups and how the same pages convert between them.

## ADDED Requirements

### Requirement: Solo / Academy review switch
Every page SHALL show a small fixed review switch at the bottom left with Solo and Academy options. The choice SHALL be remembered across pages (with browser storage, guarded so pages still work without it) and SHALL be settable with `?mode=academy` or `?mode=solo`. Solo is the default.

#### Scenario: Remembered across pages
- **WHEN** the reviewer picks Academy on the courses page and then opens the about page
- **THEN** the about page opens in academy mode with Academy pressed

#### Scenario: Storage unavailable
- **WHEN** browser storage throws or is empty
- **THEN** the page renders in solo mode without errors

#### Scenario: Coexists with other switches
- **WHEN** a page also has a demo-state switch (for example Visitor / Enrolled on the course page)
- **THEN** both switches are visible, don't overlap, and don't cover the phone bottom bar

### Requirement: Academy changes on shared parts
In academy mode the header SHALL add "Teachers" to the navigation and rename "About" to "About us". Course cards SHALL show a teacher line (avatar initial and name), and the footer brand line SHALL say "the Atelier's teachers" instead of Elena alone.

#### Scenario: Header in academy mode
- **WHEN** academy mode is on
- **THEN** the nav reads Courses, Teachers, About us, Services, Studio notes, Contact, and Teachers links to `teachers.html`

#### Scenario: Course cards in academy mode
- **WHEN** academy mode is on and course cards are shown on any page
- **THEN** each card names its teacher, and at least three different teachers appear across the six courses

### Requirement: Solo mode has no academy traces
In solo mode no page SHALL show a teachers link, teacher filters or teacher names other than Elena.

#### Scenario: Solo audit
- **WHEN** solo mode is on
- **THEN** no visible text names a teacher other than Elena Varga and no link points to `teachers.html`
