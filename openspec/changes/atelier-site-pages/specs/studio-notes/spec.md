# Spec Delta

## Purpose

Defines Studio notes, the Atelier's blog: a list of short articles and a readable article page that leads back to the courses.

## ADDED Requirements

### Requirement: Notes list
`notes.html` SHALL show a featured note and a grid of at least six notes, each with a picture, category (Technique, Materials, Studio life, Student work), title, date and reading time. Text category filters SHALL narrow the list.

#### Scenario: Filter notes
- **WHEN** the visitor picks Materials
- **THEN** only Materials notes are shown, with a count

### Requirement: Article page
`note.html` SHALL show one article with a title, a byline with date and reading time, a hero picture, body text in a 680px column with subheadings, a pull quote, an inline figure with caption, a related course card, and two "Keep reading" notes.

#### Scenario: Reading layout
- **WHEN** the article opens on a phone
- **THEN** body text is at least 17px with comfortable line length, and pictures fit the width without overflow

### Requirement: Newsletter sign-up
Both pages SHALL include the newsletter sign-up from the home page. Submitting a valid email SHALL show a thank-you state without leaving the page.

#### Scenario: Subscribe
- **WHEN** the visitor submits a valid email
- **THEN** the form is replaced by a short thank-you line; an invalid email shows an inline error
