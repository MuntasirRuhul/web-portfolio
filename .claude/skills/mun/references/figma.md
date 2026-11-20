# Figma mode: designing in Figma with auto layout

Use this mode when the user asks for a design **in Figma**, shares a figma.com link, or asks for Figma frames, components or variables. The deliverable is real, editable Figma layers built with auto layout: never a screenshot or a flat image of a UI.

## 0. Requirements and routing (mandatory)

- You need the **Figma connector** (the official Figma MCP server, with tools such as `use_figma`, `create_session`, `search_design_system`, `get_screenshot`). If it isn't connected, tell the user to connect Figma (Claude Code: add the Figma MCP server; claude.ai: Settings → Connectors → Figma), then stop. Never fake a Figma result.
- Figma ships its own required skills. **Load them before the matching tool calls.** They hold the API rules (font loading, color ranges, sizing order) that make scripts work:
  - `figma-use`: **always**, before every `use_figma` call.
  - `figma-generate-design`: for pages, screens, modals, forms, dashboards and other composed views.
  - `figma-generate-library`: for variables/tokens, text styles and reusable components with variants.
  - `figma-create-new-file`: before `create_new_file`, when the user has no target file.
  - `figma-design-to-code`: for the reverse direction (Figma → code), before `get_design_context`.
  - Load them as installed skills if present, otherwise read them from the Figma connector with `get_figma_skill` (for example `skill://figma/figma-use/SKILL.md`).
- Call `create_session` with the file key before working in a file, and reuse the session ID.
- When Figma's skill and this file disagree on **how to call the API**, Figma's skill wins. This file decides **what to design** and the **quality bar**.

## 1. Brief and target file

- Get the brief as in mun's step 1 (product, audience, page purpose, brand).
- Get the target file: a figma.com link from the user, or create a new file (via `figma-create-new-file`). Ask which page to use if the file has several. Don't edit or delete other people's existing frames unless asked.
- Check what the file already has: libraries (`get_libraries`), variables, text styles, components, existing screens. **Reuse an existing design system.** Only create new foundations when there is none.

## 2. Foundations (when the file has no design system)

Decide the design system with mun's design database and `frontend-design.md` first (palette, type, spacing, radius), then build it in Figma with `figma-generate-library`:
- **Color variables**: a `Primitives` collection (raw palette) and a `Semantic` collection (`bg/default`, `bg/subtle`, `text/primary`, `text/secondary`, `border/default`, `action/primary`, `action/primary-hover`, `status/error` …) aliased to primitives. Add a `Dark` mode when it fits the product.
- **Number variables**: spacing on a 4/8 scale (`space/1`=4, `space/2`=8, `space/3`=12, `space/4`=16, `space/6`=24, `space/8`=32, `space/12`=48, `space/16`=64, `space/24`=96), and radius (`radius/sm`, `md`, `lg`, `full`).
- **Text styles**: `Display`, `H1`–`H4`, `Body/Large`, `Body/Default`, `Body/Small`, `Label`, `Caption`, using the chosen fonts (not Inter by default), with sensible line heights (roughly 1.1–1.25 for headings, 1.4–1.6 for body).
- **Effect styles**: 1–3 elevation shadows, only if the style uses them.
- **Core components with variants** (only the ones the design needs): Button (variant × size × state), Input (state), Card, Nav item, Badge. States: default, hover, focus, disabled (plus error for inputs). Use component properties (TEXT, BOOLEAN, INSTANCE_SWAP) instead of exploding variants.

## 3. Auto layout standards (every frame)

- **Everything is auto layout.** No absolutely positioned groups for layout. Use absolute positioning only for true overlays (badges on avatars, decorative shapes), and say so in the layer name.
- **Structure**: Page (vertical) → Section (vertical, full width) → Container (max-width content area, centered) → Rows/columns (horizontal or vertical) → Components.
- **Direction and gap**: vertical stacks for content flow, horizontal for rows. Use **gap** for spacing between children, never spacer rectangles. Bind gap and padding to spacing variables.
- **Sizing**:
  - Sections and text blocks inside them: **Fill container** horizontally.
  - Buttons, badges, chips: **Hug contents**.
  - Text: **Fill** width with auto height inside layouts so it wraps; Hug only for single-line labels.
  - Cards in a row: **Fill** so they share width equally.
  - Set sizing **after** appending a child to its parent (see `figma-use` gotchas).
- **Container width**: content max-width around 1200px on desktop (1440 frame), centered, with side padding bound to spacing variables. Mobile frame 390 wide with 16–24px side padding.
- **Grids of cards**: a horizontal auto layout row with wrap (or rows of Fill items). Never hand-place cards.
- **Alignment**: pick it on purpose (left-aligned text by default; center only for short, centered hero or CTA blocks).
- **Bind, don't hardcode**: fills, strokes, padding, gap and radius use variables; text uses text styles.

## 4. Building screens

Follow `figma-generate-design`. On top of it:
- Create **one wrapper frame per screen**: `Desktop / Home` (1440 wide) and `Mobile / Home` (390 wide) when the user wants both (default to both for websites). Build mobile with the **same components**, re-stacked vertically, not scaled down.
- Name layers by purpose: `Header`, `Hero`, `Hero / Content`, `Features`, `Feature Card`, `CTA`, `Footer`. No `Frame 123` or `Rectangle 4`.
- **Componentize** anything that repeats (cards, list items, nav links, testimonials) once, then use instances.
- Real copy (follow `ux-copy.md`) and no fake testimonials, stats or logos; mark placeholders as `[Real testimonial]`.
- Images: reuse assets in the file first; otherwise use Figma's `generate_image` or `generate_vector_illustration` for placeholders and tell the user Figma AI credits were used. Icons go in as SVG (`createNodeFromSvg`), never redrawn from shapes.
- Work section by section in retry-safe calls, and return node IDs from every call.

## 5. Quality gate (before "done")

- Take **one screenshot** of each finished screen (`get_screenshot`) and check for clipped or overlapping text, leftover placeholder text ("Title", "Button"), wrong fonts, broken sizing, and unaligned edges. Fix with targeted edits, then take one more screenshot.
- Resize test: confirm that sections set to Fill stretch and that text wraps, by checking the mobile frame or temporarily resizing the wrapper.
- Accessibility in design: text contrast ≥ 4.5:1 (3:1 for large text), touch targets ≥ 44×44 on mobile, a visible focus state on interactive components, and color never the only signal.
- Confirm that colors, spacing and text are bound to variables and styles. Replace any raw hex or pixel values you find.

## 6. Report

Give the Figma link to the created frames and list: the screens built, the foundations created or reused (collections, styles, components), key design decisions, and anything left for the user (real images, copy, brand assets).
