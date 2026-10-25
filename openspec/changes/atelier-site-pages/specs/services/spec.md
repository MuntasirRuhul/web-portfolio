# Spec Delta

## Purpose

Defines the services page, where Elena's two bookable offers, a one-to-one portfolio review and a weekly live class, are explained, priced and booked.

## ADDED Requirements

### Requirement: Two offers
The services page SHALL present the portfolio review (30 min video call, from $45) and the live weekly class (Thursdays 18:00 WET, free for enrolled students) as two side-by-side offers. Each offer has what you get, who it's for, price and a primary booking button.

#### Scenario: Offers visible
- **WHEN** the services page opens
- **THEN** both offers are shown with price and a booking button, matching the home page CTA cards

### Requirement: How it works
Each offer SHALL have a short numbered process (for the review: send your work, book a time, meet, get notes), shown as the ochre / rose / terracotta step cards used elsewhere.

#### Scenario: Review process
- **WHEN** the visitor reads the portfolio review section
- **THEN** four steps are shown in order with the step colours from the method cards

### Requirement: Booking state
The booking button SHALL open an in-page booking panel with a few demo time slots and a confirm button that shows a confirmation state. No real booking is made.

#### Scenario: Book a slot
- **WHEN** the visitor picks a slot and confirms
- **THEN** a confirmation names the slot and offers "Add to calendar" as a non-functional link

### Requirement: Services FAQ
The page SHALL end with three to five questions about the services, using the book icon FAQ from the home page.

#### Scenario: FAQ toggles
- **WHEN** a question is opened
- **THEN** its answer shows and the icon changes from a closed book to an open book
