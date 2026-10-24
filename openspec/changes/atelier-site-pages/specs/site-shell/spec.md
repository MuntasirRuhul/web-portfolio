# Spec Delta

## Purpose

Defines the shared frame of every Atelier page: one header with navigation, one footer, and a complete set of linked pages, so a reviewer can walk the whole site without hitting dead links.

## ADDED Requirements

### Requirement: Shared header on content pages
Every new marketing and account page SHALL use one shared light header: the brand linking to the home page, main navigation (Courses, About, Services, Studio notes, Contact), and a Log in pill. When the student is shown as signed in, the pill reads "My learning" and links to the dashboard. On phones the links collapse into a Menu dropdown.

#### Scenario: Navigation on desktop
- **WHEN** any new content page is opened at 1440px
- **THEN** the header shows the brand, the five links and the Log in pill, and the current page's link is marked as current

#### Scenario: Navigation on phones
- **WHEN** the page is 390px wide
- **THEN** the links are hidden behind a Menu button that opens and closes a dropdown, and Escape closes it

### Requirement: Shared footer
Every new page except the learning-area screens (quiz, assignment) SHALL end with the same footer: brand line, Learn, Studio and Help link columns, and a base row with copyright and social names.

#### Scenario: Footer links
- **WHEN** the footer is shown
- **THEN** each footer link points to an existing page or section, not `#`

### Requirement: No dead primary links
Primary navigation, footer links, course cards and main calls to action on all pages SHALL link to a page in the set. Links that would need a real backend (payment, social profiles, download files) MAY stay as `#`, but they SHALL NOT be primary navigation.

#### Scenario: Link audit
- **WHEN** every `href` on every page is listed
- **THEN** none of the header, footer, course-card or primary-button links is `#`, and every relative link resolves to an existing file and anchor

### Requirement: Design system and responsiveness
All new pages SHALL follow the Atelier design language (`atelier-art-direction`): its tokens and components from `assets/site.css`, a declared archetype, no shadows, line ticks without circles, no pill badges for counts or tags, the earthy palette without blue, Inter Tight / JetBrains Mono / Caveat type. They SHALL work at 1440px and 390px.

#### Scenario: Responsive check
- **WHEN** each page is rendered at 1440px and 390px
- **THEN** there are no script errors, `scrollWidth` equals the viewport width, and `atelier/tools/audit.mjs` passes for the page
