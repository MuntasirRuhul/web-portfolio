# Spec Delta

## Purpose

Defines what the course details page shows a visitor who has not enrolled: the header, key facts, actions, section order and names, the enrol card, and the student-drawings proof strip.

## ADDED Requirements

### Requirement: Single course header
The course details page SHALL show one header layout, the dark Cinema band, with the title, short promise, trailer, facts grid, price with Enrol and free-lesson buttons, and Elena's signature. No header-layout switch SHALL be shown.

#### Scenario: Visitor opens the course page
- **WHEN** a visitor opens the course page with no hash or with `#visitor`
- **THEN** the Cinema header is shown and no Cover header or Cinema/Cover switch is present

#### Scenario: Old review hash
- **WHEN** the page is opened with `#cinema` or `#cover`
- **THEN** it shows the visitor view with the Cinema header and does not error

### Requirement: Course medium label
The header SHALL show the course number and medium as a small mono label above the title (for example "Course 01 · Pencil").

#### Scenario: Label above title
- **WHEN** the visitor view is shown
- **THEN** a mono uppercase label naming the course number and medium appears directly above the course title

### Requirement: Facts grid includes enrolment and freshness
The header facts grid SHALL include, besides rating, lessons, length, level and certificate, the number of students enrolled and the date the course was last updated.

#### Scenario: Facts shown
- **WHEN** the visitor view is shown
- **THEN** the facts grid lists Rating, Lessons, Length, Level, Students and Updated, with Certificate kept either in the grid or in the enrol card list

#### Scenario: Facts on phones
- **WHEN** the page is 390px wide
- **THEN** the facts grid wraps into two columns without horizontal page scroll

### Requirement: Wishlist and share actions
The header SHALL offer Wishlist and Share as quiet text links with line icons, not pill buttons. Wishlist SHALL toggle between saved and not saved and show the current state.

#### Scenario: Save to wishlist
- **WHEN** the visitor activates Wishlist
- **THEN** its icon and label change to the saved state ("Saved") and its pressed state is exposed to assistive technology

#### Scenario: Share
- **WHEN** the visitor activates Share
- **THEN** the page offers a way to share or copy the course link and confirms the action in text

### Requirement: Trailer and price shown once each above the fold
The enrol card SHALL NOT repeat the trailer image shown in the header. The card keeps price, enrol actions, refund line, what the course includes, and the gift link.

#### Scenario: No duplicate trailer
- **WHEN** the visitor view is shown on desktop
- **THEN** the trailer image appears only in the header, and the enrol card starts with the price

### Requirement: Pre-sale questions section name
The pre-sale questions section and its tab SHALL be named "Before you enrol", and the name "Q&A" or "Questions" SHALL NOT be used for it.

#### Scenario: Tab label
- **WHEN** the section tabs are shown
- **THEN** the last tab reads "Before you enrol" and scrolls to the section with that heading

### Requirement: Student drawings strip
The visitor view SHALL include a section before the reviews that shows at least three students' first-week and final drawings side by side, each pair labelled with the student's name and the number of weeks taken.

#### Scenario: Strip placement
- **WHEN** the visitor scrolls past the teacher section
- **THEN** the "Week 1 → Week 6" strip appears before the reviews section

#### Scenario: Pair labels
- **WHEN** a pair is shown
- **THEN** both images have text alternatives, the earlier drawing is labelled "Week 1" and the later one with its week, and the student's name is visible

#### Scenario: Strip on phones
- **WHEN** the page is 390px wide
- **THEN** the pairs stack or scroll within their own container and the page has no horizontal overflow

### Requirement: Design system constraints
All new or changed parts SHALL follow the Atelier design system: no shadows, line ticks without circles, no pill badges for counts or tags, the earthy palette without blue, Inter Tight / JetBrains Mono / Caveat type.

#### Scenario: Visual audit
- **WHEN** the changed page is reviewed at 1440px and 390px
- **THEN** none of the new elements use box shadows, round tick badges, pill-shaped count or tag badges, or colours outside the palette
