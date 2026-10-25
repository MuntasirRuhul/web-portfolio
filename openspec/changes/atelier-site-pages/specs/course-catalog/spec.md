# Spec Delta

## Purpose

Defines the courses archive: how visitors browse all six courses, narrow them by medium and level, sort them, and recover when no course matches.

## ADDED Requirements

### Requirement: Courses archive
The courses page SHALL list all six courses as the home page's poster cards. Each card shows number, medium, title, picture, level, lessons, running time and price, and links to the course page.

#### Scenario: All courses
- **WHEN** the courses page opens
- **THEN** six poster cards are shown with a count line "6 courses", and each card links to `course.html`

### Requirement: Filter by medium and level
The archive SHALL offer medium filters (All, Pencil, Graphite, Ink, Watercolour, Oil, Acrylic) and level filters (All, Beginner, Intermediate, Advanced) as plain text toggles with a clear active state, not pill badges. Filters combine, and the count updates.

#### Scenario: Combine filters
- **WHEN** the visitor picks Watercolour and Beginner
- **THEN** only matching cards are shown and the count reads "1 course"

#### Scenario: Keyboard and state
- **WHEN** a filter is toggled with the keyboard
- **THEN** its pressed state is exposed to assistive technology and the result count is announced

### Requirement: Sort
The archive SHALL sort by Recommended (default), Newest, Price low to high and Shortest first.

#### Scenario: Price sort
- **WHEN** the visitor picks Price low to high
- **THEN** cards reorder by price ascending

### Requirement: Empty state
When no course matches, the archive SHALL show a friendly empty state with a reset link and a pointer to the free lesson.

#### Scenario: No match
- **WHEN** the filters match no course (for example Oil and Beginner)
- **THEN** the grid is replaced by a message, "Clear filters" resets everything, and a link offers the free lesson

### Requirement: Academy filter
In academy mode the archive SHALL add a Teacher filter and show the teacher on each card.

#### Scenario: Teacher filter
- **WHEN** academy mode is on and the visitor picks one teacher
- **THEN** only that teacher's courses are shown
