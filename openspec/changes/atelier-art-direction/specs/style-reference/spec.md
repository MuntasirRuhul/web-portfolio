# Spec Delta

## Purpose

Publishes the design language as a page people can look at and review, built from the same shared CSS the site uses, so the reference can't drift from the real pages.

## ADDED Requirements

### Requirement: Style reference page
`style.html` SHALL be a Gallery page built only from `assets/site.css` and its own layout CSS, with eleven chapters covering the language: principles, colour, type, spacing and radii, grid, labels and voice, imagery, micro-details, components, motion and archetypes.

#### Scenario: Live samples
- **WHEN** a component on the style page is inspected
- **THEN** it is rendered by the same class names in `assets/site.css` that the pages use

#### Scenario: Chapter content
- **WHEN** the reviewer reads the style page
- **THEN** colour shows swatches with hex and contrast ratios, type shows live samples per step, motion has a replay control, and archetypes show thumbnails linking to example pages

### Requirement: Component catalogue
The Components chapter SHALL show buttons, text links, chapter label, poster card, step cards, colour blocks, book FAQ, form field with error, tabs, facts table and review bar, each with its hover and focus states.

#### Scenario: States visible
- **WHEN** the reviewer tabs through the Components chapter
- **THEN** every interactive sample shows a visible terracotta focus ring

### Requirement: Do and don't pairs
Each chapter SHALL include at least one do / don't pair drawn from real decisions (for example, round tick vs line tick, pill count badge vs superscript count, "Curriculum" vs "Six topics, one drawing at a time.").

#### Scenario: Pairs shown
- **WHEN** the reviewer reads the Micro-details chapter
- **THEN** there are do / don't pairs for ticks, count badges and separators, with the don't side visibly marked

### Requirement: Reachable from the site
The style page SHALL be linked from the footer base row ("Style") on every page and published in the artifact.

#### Scenario: Footer link
- **WHEN** the reviewer clicks Style in any footer
- **THEN** `style.html` opens
