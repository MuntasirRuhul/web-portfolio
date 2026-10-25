# Spec Delta

## Purpose

Defines signing in and creating an account: one page with Log in and Create account, a password reset state, and where a successful sign-in leads.

## ADDED Requirements

### Requirement: Log in and create account on one page
`account.html` SHALL show Log in and Create account as two tabs in one card beside a studio picture with a short quote. `#login` and `#register` open the matching tab.

#### Scenario: Open register by hash
- **WHEN** the page is opened with `#register`
- **THEN** the Create account tab is active and its first field is ready

### Requirement: Log in form
The Log in tab SHALL have email, password with a show/hide toggle, "Keep me signed in", "Forgot password?" and a primary Log in button. A valid demo submit SHALL go to `dashboard.html`.

#### Scenario: Successful log in
- **WHEN** the visitor fills both fields and submits
- **THEN** the browser opens `dashboard.html`

#### Scenario: Missing password
- **WHEN** the password is empty on submit
- **THEN** an inline error is shown for the password field and no navigation happens

### Requirement: Create account form
The Create account tab SHALL ask for first name, email and password (with a strength hint), agreement to the terms, and an optional newsletter opt-in. Submit leads to `dashboard.html` with a welcome note.

#### Scenario: Register
- **WHEN** all required fields are valid and the form is submitted
- **THEN** the browser opens `dashboard.html?welcome=1` and the dashboard shows a first-visit welcome

### Requirement: Password reset
"Forgot password?" SHALL switch the card to a reset form (email only) with a sent state and a link back to Log in.

#### Scenario: Reset sent
- **WHEN** the visitor submits a valid email in the reset form
- **THEN** the card says a link was sent to that email and offers "Back to log in"
