# Accessibility checklist (WCAG 2.2 AA)

Check each item and fix failures in the code. Report only what you couldn't fix.

## Perceivable
- Text contrast is at least 4.5:1 (or 3:1 for large text, 24px+ or 18.66px+ bold). UI parts and focus rings are at least 3:1 against what's next to them.
- Color is never the only signal. Errors, required fields and status also use text or an icon.
- Every meaningful image has `alt`. Decorative images use `alt=""`. Icon-only buttons have an `aria-label`.
- Text resizes to 200% without loss. Content reflows at 320px with no horizontal scroll.
- Video has captions. Audio has a transcript.

## Operable
- Everything works with a keyboard alone: Tab order is logical and there are no traps.
- Focus is always visible (`:focus-visible`) and never hidden behind sticky headers.
- A "Skip to main content" link is the first focusable element on content-heavy pages.
- Touch targets are at least 24×24px (aim for 44×44px on mobile), with spacing between them.
- `prefers-reduced-motion` turns off non-essential animation. Nothing flashes more than 3 times a second.
- Carousels and auto-playing content have pause, previous and next controls.

## Understandable
- `<html lang>` is set. The page `<title>` is unique and descriptive.
- Every input has a visible `<label>`. Placeholder text is not a label.
- Errors say what went wrong and how to fix it, sit next to the field, and are announced (`aria-describedby`, `aria-live`).
- Navigation and naming are consistent across pages.

## Robust
- Use semantic HTML first: `header`, `nav`, `main`, `footer`, `button` for actions, `a` for navigation, and headings in order (one `h1`, no skipped levels).
- ARIA only where native HTML can't do the job, and states (`aria-expanded`, `aria-current`) are kept in sync.
- Modals trap focus, close with Esc, and return focus to the element that opened them.

## Quick test
1. Tab through the whole page.
2. Zoom to 200%, then view at 320px width.
3. Check contrast on every text and background pair.
4. Turn on reduced motion.
