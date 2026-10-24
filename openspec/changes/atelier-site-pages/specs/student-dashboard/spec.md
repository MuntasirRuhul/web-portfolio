# Spec Delta

## Purpose

Defines the enrolled student's home: where Marta lands after signing in, picks up where she left off, and finds her courses, wishlist, quiz results, certificates and settings.

## ADDED Requirements

### Requirement: Dashboard home
`dashboard.html` SHALL greet the student and show, in order: a Continue card for the next lesson (same data as `lesson.html`: 12 of 24, topic 4 lesson 1), this week's live class, totals (courses, hours drawn, critiques), and a short list of pending items.

#### Scenario: Continue
- **WHEN** the dashboard opens
- **THEN** the Continue card names "Three values, not seven", shows 50%, and links to `lesson.html`

### Requirement: Dashboard sections
The dashboard SHALL have a section menu (side column on desktop, horizontal scroll row on phones) with: Home, My courses, Wishlist, Quiz attempts, Certificates, Settings. Each section shows realistic demo content, and My courses has In progress / Completed tabs.

#### Scenario: Switch section
- **WHEN** the student picks Quiz attempts
- **THEN** a list of attempts (quiz, date, score, result) is shown and the menu marks Quiz attempts as current

### Requirement: Welcome state
When opened with `?welcome=1` the dashboard SHALL show a first-visit welcome card with three first steps instead of the Continue card.

#### Scenario: New account
- **WHEN** the dashboard is opened from Create account
- **THEN** the welcome card is shown and the Continue card is hidden
