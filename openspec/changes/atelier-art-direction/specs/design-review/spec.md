# Spec Delta

## Purpose

Makes the art direction enforceable: a written checklist from whole page to single pixel, and a scripted audit, that every page passes before it's published.

## ADDED Requirements

### Requirement: Review checklist
A checklist SHALL cover three scales.
- **Macro** (page): archetype rules; one idea per section; rhythm of paper, rooms and objects; a clear first action; an ending with a next step.
- **Meso** (section): chapter label and voiced headline; grid alignment; colour-block order; image treatment.
- **Micro** (details): type-scale steps; radii and rules; characters and numerals; icons and ticks; hover and focus states; reduced motion; contrast.

It lives in the style reference and in the handoff.

#### Scenario: Reviewer uses the list
- **WHEN** a page is ready to publish
- **THEN** each checklist line is either satisfied or noted with a reason in the commit message

### Requirement: Scripted audit
`atelier/tools/audit.mjs` SHALL open each page at 1440px and 390px and report:
- `data-archetype`;
- horizontal overflow;
- page errors;
- font sizes and radii outside the scale;
- any `box-shadow` other than paint pots;
- straight quotes or " - " separators in visible text;
- text contrast below 4.5:1 for body and 3:1 for large text;
- images missing alt text;
- links to `#` among primary navigation.

It SHALL exit non-zero when any blocking item fails.

#### Scenario: Audit fails on a shadow
- **WHEN** a page adds `box-shadow` to a card
- **THEN** the audit lists the selector and exits non-zero

#### Scenario: Audit passes
- **WHEN** all pages follow the language
- **THEN** the audit prints a summary per page and exits zero

### Requirement: Gate before publishing
No page SHALL be published to the artifact while the audit fails for it. Before/after screenshots at both widths SHALL be looked at for every visual change.

#### Scenario: Publish flow
- **WHEN** a page change is ready
- **THEN** the audit runs clean and screenshots are reviewed before `build-artifact.py` and publish
