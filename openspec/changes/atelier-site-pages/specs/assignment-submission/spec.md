# Spec Delta

## Purpose

Defines submitting the final drawing for Elena's private critique and seeing its status and review, inside the learning area.

## ADDED Requirements

### Requirement: Assignment brief
`assignment.html` SHALL use the learning-area shell and show the brief: what to submit, the deadline guidance ("within 30 days of finishing topic 6"), how to photograph a drawing, file limits (JPG or PNG, up to 3 files, 10 MB each) and what the critique includes.

#### Scenario: Brief content
- **WHEN** the assignment page opens
- **THEN** the brief, photo tips and file limits are shown above the upload area

### Requirement: Upload and submit
The page SHALL let the student add up to three image files (picker and drag-and-drop) with previews and remove buttons, add a note to Elena, and submit. Files outside the limits SHALL show an inline error.

#### Scenario: Add and submit
- **WHEN** the student adds two JPG images, writes a note and submits
- **THEN** the page switches to the Submitted state listing both files and the note, with "Elena replies within 10 days"

#### Scenario: Wrong file
- **WHEN** the student adds a PDF or a file over 10 MB
- **THEN** that file is rejected with an inline message and the others stay

### Requirement: Review state
A demo switch SHALL show the Reviewed state: a video critique poster with duration, Elena's written notes, a grade line ("Passed"), and the certificate now unlocked.

#### Scenario: Reviewed
- **WHEN** the reviewer switches to Reviewed
- **THEN** the critique video, notes and an unlocked certificate link are shown
