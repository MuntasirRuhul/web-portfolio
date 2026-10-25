# Spec Delta

## Purpose

Defines taking a quiz inside the learning area: a start screen, one question at a time with progress, and a result that leads back to the course.

## ADDED Requirements

### Requirement: Quiz in the learning area
`quiz.html` SHALL use the same header, curriculum sidebar and bottom bar as `lesson.html`, with the quiz "Spot the edges" (topic 1, 8 questions, pass mark 70%) as the current item.

#### Scenario: Shell matches the lesson page
- **WHEN** the quiz page opens
- **THEN** the header progress, sidebar topics and item states match `lesson.html`, with the quiz marked as current

### Requirement: Start, questions, result
The quiz SHALL start on an intro screen (questions, time, pass mark, attempts left), then show one question at a time with a progress bar and Previous / Next, and end with a result screen (score, pass or fail, per-question review, Retake and Continue).

#### Scenario: Complete a quiz
- **WHEN** the student answers all questions and submits
- **THEN** the result screen shows the score out of 8, pass or fail against 70%, and Continue to the next item

### Requirement: Question types
The demo quiz SHALL include at least true/false, single choice with image answers, multiple choice, and ordering. Each SHALL be fully usable by keyboard.

#### Scenario: Image choice by keyboard
- **WHEN** the student reaches the image question and uses Tab and the arrow keys
- **THEN** they can select an answer and see the selection state without a mouse
