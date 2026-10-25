# Spec Delta

## Purpose

Defines four page kinds, so the one design language flexes by purpose (showing, reading, working, committing) instead of drifting page by page.

## ADDED Requirements

### Requirement: Every page has one archetype
Every page SHALL declare one archetype on `<body data-archetype="…">`: Gallery, Reading, Workroom or Counter. Pages SHALL follow that archetype's rules. The assignments are:
- Gallery: home, about, teachers, services, courses, notes list;
- Reading: course detail, article;
- Workroom: lesson, quiz, assignment, dashboard;
- Counter: account, checkout, contact.

#### Scenario: Declared archetype
- **WHEN** the scripted audit opens a page
- **THEN** `data-archetype` is present and matches the list above

### Requirement: Gallery archetype
Gallery pages SHALL use the paper ground with grain, the drawing grid, chapter labels with display headlines, at least one dark room (28px radius) and at most one row of colour blocks. Objects (cards, frames) sit on paper in white.

#### Scenario: Gallery check
- **WHEN** a Gallery page is reviewed
- **THEN** grain, grid lines, chapter labels and one dark room are present

### Requirement: Reading archetype
Reading pages SHALL use a white ground like a printed sheet, with a 680–760px reading column and chapter labels with voiced h2 headlines. Paper beige is used only for objects (cards, summary boxes, bands), and grain and grid only inside beige bands. The hero MAY be a dark room.

#### Scenario: Beige restraint
- **WHEN** the course page is reviewed
- **THEN** the page ground is white and beige appears only on the enrol card, the review summary, the drawings strip and the closing band

### Requirement: Workroom archetype
Workroom pages SHALL be quiet tools: white ground, soft beige for the navigation column, no grain, no grid lines, no display headlines, no reveal motion, and chapter labels only as small mono context. They keep the type scale, radii, line icons, line ticks and the course accent for progress.

#### Scenario: Quiet tool
- **WHEN** the lesson page is reviewed
- **THEN** it has no grain, grid lines or reveal animations, and progress uses the course accent

### Requirement: Counter archetype
Counter pages SHALL put the one task in a single white card on paper, beside a dark room or studio photograph that carries a short line of voice and the signature. Forms use 12px-radius fields on paper, mono labels, inline errors in terracotta text (not red), and one primary button.

#### Scenario: Form styling
- **WHEN** a Counter form shows a validation error
- **THEN** the message is terracotta text tied to its field, with no red and no shake
