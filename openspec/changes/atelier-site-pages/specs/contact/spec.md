# Spec Delta

## Purpose

Defines the contact page, where visitors and students reach Elena (or the Atelier) with a short form or directly, and know when to expect a reply.

## ADDED Requirements

### Requirement: Contact options
The contact page SHALL offer a short form (name, email, topic, message), a direct email address, the studio's city, and reply times ("within two working days"). Topic options include Courses, Portfolio review, Live class, Billing and Something else.

#### Scenario: Page content
- **WHEN** the contact page opens
- **THEN** the form, email address, city and reply time are all visible without scrolling on desktop

### Requirement: Form validation and states
The form SHALL validate required fields inline with text messages tied to each field, and on a valid submit SHALL show a sent state naming the email the reply will go to. No message is actually sent.

#### Scenario: Missing email
- **WHEN** the visitor submits without an email
- **THEN** the email field shows an error message linked to it, and focus moves to the first invalid field

#### Scenario: Sent
- **WHEN** all fields are valid and the form is submitted
- **THEN** the form is replaced by "Thanks, Elena will reply to <email>" (or "we will reply" in academy mode)

### Requirement: Help before writing
The page SHALL link to the three most common answers (refunds, course access, critique timing) before the form.

#### Scenario: Quick answers
- **WHEN** the visitor reads above the form
- **THEN** three short answers are shown, each linking to the matching question on the course or services page
