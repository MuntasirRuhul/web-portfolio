# Spec Delta

## Purpose

Sets down the Atelier's taste, taken from the home page, as rules every page follows, at every scale from a single hairline to a whole page: an artist's studio presented as a gallery.

## ADDED Requirements

### Requirement: Principles
Every page SHALL express the five principles: the studio is the gallery; drawn, then painted; look longer; the hand is present; quiet labels, loud statements. The meaning of each is shown in the scenarios below.

#### Scenario: The studio is the gallery
- **WHEN** a section is designed
- **THEN** it is framed as a thing in Elena's studio (posters, a wall, letters, labels), not as a generic UI block

#### Scenario: Drawn, then painted
- **WHEN** colour is added to a section
- **THEN** structure is already grey line and paper, and colour arrives in a few deliberate blocks

#### Scenario: Look longer, the hand is present, quiet labels
- **WHEN** a page is reviewed
- **THEN** it has generous space and one idea per section, at least one hand mark (signature, irregular shape, small tilt; never a wobble filter), and tiny mono captions against big plain-sentence headlines

### Requirement: Colour roles
Colours SHALL be used by role: Paper `#FAF6EF` gallery ground, White object and reading ground, Night `#161412` rooms, Ink `#1D1A16` text, Ink-2 `#4A443B` secondary text. Terracotta `#C0512F` is the single accent (`#E8724A` on dark only). Blue SHALL NOT be used.

#### Scenario: Accent discipline
- **WHEN** any viewport-height slice of a page is inspected
- **THEN** terracotta appears at most twice as text accent and once as a primary button

### Requirement: Colour blocks and course accents
Full colour blocks SHALL use Ochre `#DDA43C`, Rose `#D9A7A0` and Terracotta in that order. Each course keeps its own accent (`--c1`…`--c6`) for its poster, progress and numerals. Sage and plum appear only as course accents.

#### Scenario: Block order
- **WHEN** a row of colour blocks is shown
- **THEN** the blocks run ochre, rose, terracotta

### Requirement: Typefaces
Type SHALL use Inter Tight for text and headings, Inter 700 for poster titles and display numerals, JetBrains Mono for labels and captions, and Caveat only for the signature. Italics and serif faces SHALL NOT be used.

#### Scenario: No italics
- **WHEN** the scripted audit checks computed styles
- **THEN** no visible text is italic and no serif family is used

### Requirement: Typography scale
Sizes SHALL come from one scale: display `clamp(40px,5vw,68px)`, h2 `clamp(30px,3.5vw,48px)`, h3 `clamp(22px,2vw,28px)`, lead 18px, body 16px, small 14px, and mono 10.5px uppercase with `.06em` tracking. Headings use tracking of `-.04em` to `-.055em` and a line-height of 1.1 or less.

#### Scenario: Off-scale sizes
- **WHEN** the scripted audit lists font sizes on a page
- **THEN** every size maps to a scale step or a documented component exception (for example 9–10px captions on poster objects)

### Requirement: Spacing, radii and rules
Spacing SHALL use the 4-step scale (4, 8, 12, 16, 24, 32, 40, 64, 96, 140) with section padding `clamp(80px,10vw,140px)`. Radii SHALL be one of:
- 28px: rooms (dark panels);
- 16px: cards, objects, footer;
- 12px: inputs, the top bar, small panels;
- 999px: buttons and switches;
- 50%: avatars and discs.

Rules are 1px (`rgba(ink,.14)`, or `.075` for grid lines), and 2px ink only to open a facts table. Shadows SHALL NOT be used, except the inset rim on paint pots.

#### Scenario: Radius audit
- **WHEN** the scripted audit lists border radii
- **THEN** no value outside {28, 16, 12, 999px, 50%, paint-pot blobs} appears

### Requirement: Drawing grid and construction
Gallery grounds SHALL show the drawing grid: thin vertical lines at the thirds of the content area, and content aligned to them. Construction marks (circle, crossing rules) MAY appear once per page in a hero or a room, drawn in on view.

#### Scenario: Alignment
- **WHEN** a Gallery page is overlaid with its grid lines
- **THEN** section labels, headline starts or list rules sit on a grid line, not floating between them

### Requirement: Chapter labels and headline voice
Gallery and Reading sections SHALL open with a chapter label: a two-digit number in terracotta, a mono name, and a 34px rule ("02 THE ARTIST ——"). Headlines SHALL be plain sentences ending in a full stop. They may land on one terracotta phrase ("Six courses, hung like posters."). Headlines SHALL NOT be generic UI nouns ("Curriculum", "Reviews"); those words belong in the chapter label.

#### Scenario: Course page sections
- **WHEN** the course page's sections are read
- **THEN** each has a chapter label (for example "02 CURRICULUM ——") and a voiced headline (for example "Six topics, one drawing at a time.")

### Requirement: Imagery
Photographs SHALL be greyscale with a slight contrast lift by default. Colour is revealed only on interaction (hover or focus) or inside a course-accent mix on poster cards. Cut-out objects are multiplied into the paper. Faces of people who aren't Elena SHALL NOT be used to stand for named people; initials are used instead. Captions SHALL be mono, museum-style ("Her brushes, in order of use · No. 2 … No. 24").

#### Scenario: Image treatment
- **WHEN** a page shows a photograph at rest
- **THEN** it renders greyscale unless it's a course trailer or video still, which stay natural

### Requirement: Micro-details
Text SHALL use real typographic characters: curly quotes and apostrophes, the middle dot `·` as the separator, `→` for forward links, `×` for dimensions, the en dash for ranges, and tabular numerals for times, prices and counts. Icons SHALL be 1.5–1.7px line drawings with round caps. "Hand" icons MAY carry a soft colour wash. Ticks are plain lines without a circle. Counts and tags are never pill badges.

#### Scenario: Character audit
- **WHEN** the scripted audit scans visible text
- **THEN** it reports no straight double quotes in prose, no " - " used as a separator, and no pill-shaped count badges

### Requirement: Motion
Motion SHALL use two curves:
- `cubic-bezier(.2,.7,.2,1)` for objects (reveal .9s with a 28px rise, hover lift `translateY(-6px) rotate(-.6deg)` in .45s);
- `cubic-bezier(.6,.1,.2,1)` for drawn lines (1.3–2.4s stroke draw).

Arrows rotate `-45deg` on hover. All motion SHALL stop under `prefers-reduced-motion`, and content SHALL be visible without JavaScript.

#### Scenario: Reduced motion
- **WHEN** the page is loaded with reduced motion requested
- **THEN** every element is in its final state, with no transitions or animations running
