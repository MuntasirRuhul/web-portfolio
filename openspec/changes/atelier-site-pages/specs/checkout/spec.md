# Spec Delta

## Purpose

Defines buying a course: a single checkout page that shows what is being bought, takes details and payment, and confirms the order.

## ADDED Requirements

### Requirement: Order summary
`checkout.html` SHALL show the course being bought (poster thumbnail, title, level, lessons) with price $79, the struck-out $99, an optional gift toggle, a coupon field and the total. Enrol buttons on the course page SHALL link here.

#### Scenario: From the course page
- **WHEN** the visitor clicks Enrol now on the course page
- **THEN** `checkout.html` opens with Foundations of Drawing in the summary and a total of $79

#### Scenario: Coupon
- **WHEN** the visitor applies the demo code `STUDIO10`
- **THEN** a 10% discount line appears and the total updates; any other code shows an inline "Code not recognised"

### Requirement: Details and payment
The checkout SHALL collect email (or show the signed-in student), name and country, and a payment method choice (card, PayPal) with card fields. It SHALL repeat the 14-day refund promise beside the Pay button.

#### Scenario: Validation
- **WHEN** a required field is empty on Pay
- **THEN** that field shows an inline error and focus moves to it

### Requirement: Success state
A valid Pay SHALL show a success state: thank you, what happens next, a "Start learning" button to `lesson.html`, and a receipt summary. No payment is taken.

#### Scenario: Paid
- **WHEN** the form is valid and Pay is pressed
- **THEN** the page shows the success state with "Start learning" linking to `lesson.html`
