---
name: figma-expert
description: Master Figma workflows with auto layout, components, variables, prototyping, and team collaboration.
category: creative-design
---

## Overview

Figma rewards systematic thinking: designers who master auto layout, components,
and variables
design 3x faster and hand off cleaner files. This skill covers the professional
Figma workflow —
from file organization and component architecture to variables, prototyping, and
developer handoff —
plus the collaboration habits that keep team files healthy.

## When to use

- Setting up a new Figma file or design system library

- Building responsive layouts with auto layout

- Creating and managing component variants

- Using variables for theming (light/dark mode, brands)

- Prototyping interactions and preparing dev handoff

## Core concepts

- - - **Auto layout is the foundation.** Frames that resize with content
  (padding, gaps, direction,
  wrapping) make designs responsive by default and components bulletproof. Learn
it before anything
  else — it changes how you think about layout.
- - - **Components with variants.** One component, many states
  (default/hover/disabled;
  small/medium/large) via variant properties. Boolean properties for toggles
like icons.
  Well-architected variants eliminate dozens of duplicate components.
- - - **Variables for theming.** Color, spacing, radius, and typography
  variables enable instant theme
  switching and multi-brand systems. Use modes for light/dark; collections for
semantic grouping
  (e.g., "surface/primary" not "gray-100").
- - - **File hygiene.** Named pages (Cover, Components, Flows, Archive),
  consistent frame naming, no
  stray layers. A messy file slows everyone and signals sloppy thinking to
developers.
- - - **Prototype with intent.** Prototype the flows that need validation or
  handoff clarity — not the
  entire app. Smart animate for realistic transitions; keep interactions
purposeful.
- - - **Dev Mode done right.** Mark sections "ready for dev," document behaviors
  in situ, link to
  tickets. The handoff file should answer questions before developers ask them.

## Practical workflow

1. 1. 1. **Set up the file.** Pages: Cover (thumbnail + status), Foundations
   (styles/variables),
   Components (library), Designs (flows by feature), Archive. Set up color and
text styles or
   variables first.
2. 2. 2. **Build with auto layout.** Every card, button, list, and page section
   uses auto layout. Set
   hug/fill/fixed deliberately. Test responsiveness by dragging frame edges — it
should behave, not
   break.
3. 3. 3. **Create the component architecture.** Atoms (buttons, inputs, badges)
   → molecules (cards,
   list items) → organisms (headers, modals). Variants for states and sizes;
keep the default
   variant the most common use.
4. 4. 4. **Apply variables.** Convert hard-coded colors to semantic variables.
   Set up light/dark modes
   if needed. Typography: define a scale (not 47 text styles) and stick to it.
5. 5. 5. **Design the flows.** One flow per user journey, clearly labeled, with
   annotations for edge
   cases and behaviors. Use sections to group related screens.
6. 6. 6. **Prototype key interactions.** Connect the critical paths; add
   micro-interactions where
   motion communicates (loading, success, transitions). Keep it focused —
prototype to answer
   questions.
7. 7. 7. **Prepare handoff.** Mark ready sections, add measurements/notes for
   tricky behaviors, clean
   up hidden layers, and walk through with developers. The file is done when a
developer can build
   from it without pinging you.

## Common pitfalls

- - - **Detaching instances.** Detaching "just this once" creates divergence
  that compounds. Fix the
  component instead — that's what variants and properties are for.
- - - **Hard-coded values everywhere.** Colors and spacing typed manually in 200
  places. One rebrand
  later, you're doing find-and-replace for a week. Variables from day one.
- - - **Variant explosion.** 40 variants of a button because properties weren't
  planned. Design the
  property matrix first (size × state × style), then build.
- - - **No responsive behavior.** Fixed-size frames that break on different
  screens. Auto layout +
  constraints should handle the common breakpoints.
- - - **Prototype everything.** Spending days prototyping flows nobody
  questioned. Prototype to learn
  or to specify — otherwise it's expensive theater.
- - - **The junk-drawer file.** Unnamed layers ("Rectangle 47"), dead pages,
  duplicate components. Ten
  minutes of weekly cleanup saves hours of confusion.

## This project: Elena Varga Atelier

The Figma file is `art-and-craft` (file key `ItZHErcmmcHMa2KCxR8qeT`). The code's style guide is the source of truth; Figma follows it, never the other way round.

**Pages:** `Style guide` (foundations), `Components` (reusable parts), `Home` (the desktop homepage, frame "Home / Desktop 1440"). `Page 1` is older work: leave it alone.

**Variables and styles** (collection "Elena Varga Atelier", mode Light): colours `color/<name>` (the same names as `--<name>` in `assets/tokens.css`), spacing `space/space-1…10`, radii `radius/radius-*`. Text styles are `Display/`, `Heading/`, `Body/`, `Utility/`, `Hand/` + the style name (`Heading/heading-3`). Bind every fill, gap, padding and radius to a variable and every text to a style. Never type a hex or a raw size when a token exists.

**Components** (all variants, with text properties): Button (Ink/Paper), SectionLabel (Light/Dark), CourseCard (Course 01–06), MethodCard (Ochre/Rose/Terra), LetterCard (Rose/Terra/Ochre), Stat, FaqItem (Open true/false), GalleryWork (Light/Dark frame). Build sections from instances; override text with `setProperties` (property keys end in `#id`, so match on the prefix).

**Sync routine** when the style guide changes: read `tokens.json`, diff against the file's variables and text styles, update or add only what changed, then check the pages. Heights and spacing must keep the "line = size × percentage, even whole pixels" rule.

### Lessons from building the homepage

- Switch pages once per call (`setCurrentPageAsync`); component sets on other pages can still be edited by ID.
- A node inside a component instance cannot be resized or given min/max sizes. For things that vary per use (a picture's aspect ratio), make the picture FILL its parent in the component and resize the instance instead.
- Rebinding a text range to the *same* variable keeps a stale colour (it renders black). Bind a different variable first, then the right one.
- A text node's accent colour is a range fill; the base colour is the node fill. Set the base first, then the accent range, and use `indexOf` for the range, not a hand-counted index.
- `figma.createComponent()` is added to the current page immediately; a failed script leaves nothing behind (it rolls back), but check before retrying.
- Images: `upload_assets` returns upload URLs; POST each file to its URL with `curl -F "file=@x.jpg"` (the layer name comes from the filename; WebP is refused, send PNG with `;type=image/png`). Then copy the returned `imageHash` into an IMAGE fill on the placeholder (named `IMG/<name>`) and delete the temporary frames the upload placed on the page.
- Screenshots: use `enableBase64Response: true`; the screenshot download host is not reachable from the cloud container. The upload host `mcp.figma.com` must be allowed in the environment.
- Photos that are black and white on the site use an image fill with `filters: { saturation: -1 }`.

### Before saying a design is done

- Pull **every graphic** from the source, not just the text and photos: inline `<svg>`, CSS `mask`/`background` data URIs (the FAQ book icons were in a `summary::after` rule), and glyphs inside buttons. Import them with `createNodeFromSvg` and bind their fills or strokes to variables. Never leave a placeholder shape or a text character standing in for an icon.
- Compare the Figma result with the source **element by element** (rail, nav, cards, toggles, hover/open states), not only section by section.
