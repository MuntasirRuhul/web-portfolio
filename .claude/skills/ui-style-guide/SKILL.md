---
name: ui-style-guide
description: Creates an industry-standard UI style guide covering typography and color tokens, for websites and product UI. Use whenever someone asks for a style guide, type scale, typography system, color tokens, color palette, design tokens, or a design-system foundation. The type scale is generated from a chosen ratio (Minor Second to Golden Ratio), with separate desktop and mobile typography, and the ratio decides how many display styles exist. Colors use semantic tokens (text, background, surface, border, brand, button, status, icon), always with light and dark mode.
---

# UI Style Guide Skill (Typography + Color)

This skill produces a complete **typography system** and **color token system** that can be reused on every project.

Rules that always apply:
- **Line height is always in %.**
- **Letter spacing is always in %.**
- **Typography always has a desktop set and a separate mobile set.**
- **Colors always have Light and Dark values.**
- **Token names use hyphens, never slashes** (e.g. `text-title-primary`).

---

## Step 0 — Inputs

Collect these before starting. If something is missing, use the default and say so.

| Input | Default |
|---|---|
| Type scale ratio | Ask. If there's no answer: **1.250 Major Third** for websites, **1.200 Minor Third** for product UI |
| Base body size | 16px |
| Heading / display font | Ask (or suggest one from Google Fonts that fits the brand) |
| Body font | Ask (it may be the same as the heading font) |
| Brand colors | Primary is required. Secondary and tertiary are optional |
| Neutral tone | Cool gray, neutral gray, or warm gray (picked to match the brand) |
| Mobile breakpoint | Mobile ≤ 767px, desktop ≥ 768px |

Use at most **2 font families**: one for headings and display, one for body. One family for everything is fine too.

---

## Part 1 — Typography

### 1.1 Ratio rules

The chosen ratio decides **how many display styles** exist, **how many heading levels** exist, and **which ratio mobile uses**.

| Desktop ratio | Name | Display styles | Headings | Mobile ratio |
|---|---|---|---|---|
| 1.067 | Minor Second | 3 (D1–D3) | H1–H6 | 1.067 |
| 1.125 | Major Second | 3 (D1–D3) | H1–H6 | 1.125 |
| 1.200 | Minor Third | 3 (D1–D3) | H1–H6 | 1.125 |
| 1.250 | Major Third | 2 (D1–D2) | H1–H6 | 1.125 |
| 1.333 | Perfect Fourth | 1 (D1) | H1–H6 | 1.200 |
| 1.414 | Augmented Fourth | **0** | **H1–H4** | 1.250 |
| 1.500 | Perfect Fifth | **0** | **H1–H4** | 1.333 |
| 1.618 | Golden Ratio | **0** | **H1–H4** | 1.414 |

Why:
- **1.414 and above use no display styles.** These scales are already very large, so H1 does the job of a display style.
- **They also stop at H4.** At these ratios, H5 and H6 would be almost the same size as the body text.
- **Mobile uses the ratio two steps down,** but never below 1.125 (unless desktop is already 1.067). This stops huge headings from breaking small screens.
- **Mobile keeps exactly the same style names as desktop.** Only the sizes change.

### 1.2 Formula

```
size(step) = base × ratio^step          (base = 16px)

Headings H1–H6:  H6 = step 1, H5 = step 2, … H1 = step 6
Headings H1–H4:  H4 = step 1, H3 = step 2, H2 = step 3, H1 = step 4
Display:         continues above H1 (next step = smallest display, D1 = largest)
```

**Rounding:**
- Below 32px, round to the nearest **even** number.
- From 32px up, round to the nearest **multiple of 4**.
- If rounding makes two styles the same size, use whole-pixel values without the even/×4 rounding instead.

### 1.3 Precalculated sizes (px, base 16)

Use these tables directly. Calculate with the formula only if the base size isn't 16.

**1.067 Minor Second** (mobile 1.067)
| | D1 | D2 | D3 | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|---|---|---|
| Desktop | 29 | 27 | 25 | 24 | 22 | 21 | 19 | 18 | 17 |
| Mobile | 29 | 27 | 25 | 24 | 22 | 21 | 19 | 18 | 17 |

**1.125 Major Second** (mobile 1.125)
| | D1 | D2 | D3 | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|---|---|---|
| Desktop | 48 | 40 | 36 | 32 | 28 | 26 | 22 | 20 | 18 |
| Mobile | 48 | 40 | 36 | 32 | 28 | 26 | 22 | 20 | 18 |

**1.200 Minor Third** (mobile 1.125)
| | D1 | D2 | D3 | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|---|---|---|
| Desktop | 84 | 68 | 56 | 48 | 40 | 32 | 28 | 24 | 20 |
| Mobile | 48 | 40 | 36 | 32 | 28 | 26 | 22 | 20 | 18 |

**1.250 Major Third** (mobile 1.125)
| | D1 | D2 | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|---|---|
| Desktop | 96 | 76 | 60 | 48 | 40 | 32 | 26 | 20 |
| Mobile | 40 | 36 | 32 | 28 | 26 | 22 | 20 | 18 |

**1.333 Perfect Fourth** (mobile 1.200)
| | D1 | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|---|
| Desktop | 120 | 88 | 68 | 52 | 36 | 28 | 22 |
| Mobile | 56 | 48 | 40 | 32 | 28 | 24 | 20 |

**1.414 Augmented Fourth** (mobile 1.250)
| | H1 | H2 | H3 | H4 |
|---|---|---|---|---|
| Desktop | 64 | 44 | 32 | 22 |
| Mobile | 40 | 32 | 26 | 20 |

**1.500 Perfect Fifth** (mobile 1.333)
| | H1 | H2 | H3 | H4 |
|---|---|---|---|---|
| Desktop | 80 | 56 | 36 | 24 |
| Mobile | 52 | 36 | 28 | 22 |

**1.618 Golden Ratio** (mobile 1.414)
| | H1 | H2 | H3 | H4 |
|---|---|---|---|---|
| Desktop | 108 | 68 | 40 | 26 |
| Mobile | 64 | 44 | 32 | 22 |

### 1.4 Line height and letter spacing for display and headings

These depend on the **font size**, not the style name, so the same rules work for every ratio and for both desktop and mobile.

| Font size | Line height | Letter spacing |
|---|---|---|
| ≥ 96px | 100% | -3% |
| 72–95px | 105% | -2.5% |
| 56–71px | 110% | -2% |
| 40–55px | 115% | -1.5% |
| 32–39px | 120% | -1% |
| 24–31px | 130% | -0.5% |
| < 24px | 140% | 0% |

**Weights:**
- Display: 600–700.
- Headings: 600.
- Use 500 if the font is heavy, 700 if it's light.
- A display font may use a lighter weight (300–400) if the brand calls for it.

### 1.5 Body, label, overline and footnote (fixed sizes)

These styles **don't follow the ratio**. Body text has to stay readable at any scale.

| Style | Desktop | Mobile | Line height | Letter spacing | Weights |
|---|---|---|---|---|---|
| Body XL | 20 | 18 | 150% | 0% | 400 / 500 / 600 |
| Body L | 18 | 17 | 155% | 0% | 400 / 500 / 600 |
| Body M | 16 | 16 | 150% | 0% | 400 / 500 / 600 |
| Body S | 14 | 14 | 145% | 0% | 400 / 500 / 600 |
| Body XS | 12 | 12 | 140% | 0% | 400 / 500 / 600 |
| Label L | 16 | 16 | 120% | 0% | 500 / 600 |
| Label M | 14 | 14 | 120% | 0% | 500 / 600 |
| Label S | 12 | 12 | 120% | +1% | 500 / 600 |
| Overline | 12 | 12 | 120% | +8% | 600, UPPERCASE |
| Footnote | 12 | 12 | 140% | +1% | 400 |

What the non-body styles are for:
- **Label:** buttons, form labels, tabs, tags, navigation.
- **Overline:** the small eyebrow text above a heading.
- **Footnote:** legal text, captions, image credits, fine print.

### 1.6 Style names

Every name uses hyphens. Desktop and mobile share the same names; the device is a prefix in Figma and a media query in code.

```
display-1, display-2, display-3
h1, h2, h3, h4, h5, h6
body-xl-regular, body-xl-medium, body-xl-semibold
body-l-regular … body-xs-semibold
label-l-medium, label-l-semibold, label-m-medium … label-s-semibold
overline
footnote
```

In Figma, create two sets of text styles: `desktop-h1`, `desktop-body-m-regular`, … and `mobile-h1`, `mobile-body-m-regular`, …

### 1.7 Line breaking and text rules

- **Line length:** 45–75 characters for body text (`max-width: 65ch`). Headings can be wider but rarely more than about 20 words per line.
- **Headings:** `text-wrap: balance` so that lines come out roughly equal in length.
- **Paragraphs:** `text-wrap: pretty` to avoid a single word alone on the last line.
- **No hyphenation** in headings or display text (`hyphens: none`). Body text may use `hyphens: auto` only in narrow columns.
- **Never** force line breaks with spaces or manual `<br>` for layout. Use width or `max-width` instead.
- **Avoid ALL CAPS** except for the overline and short labels, which always get positive letter spacing.
- **Paragraph spacing:** about 0.75–1× the body line height between paragraphs.
- **Large text needs tight spacing, small text needs open spacing.** Never use negative letter spacing below 20px.

### 1.8 Units in code vs Figma

| Property | Figma | CSS |
|---|---|---|
| Line height | `110%` | `line-height: 1.1;` (unitless, so it scales correctly when inherited) |
| Letter spacing | `-2%` | `letter-spacing: -0.02em;` |
| Font size | `px` | `rem` (`px / 16`), e.g. 60px → `3.75rem` |

---

## Part 2 — Color

### 2.1 Two layers

1. **Primitives**: raw colors with no meaning. Never used directly in designs.
   - `neutral-0` (white), `neutral-50`, `neutral-100` … `neutral-900`, `neutral-950`
   - `brand-primary-50` … `brand-primary-950` (plus `brand-secondary-*` and `brand-tertiary-*` if the brand has them)
   - `success-*`, `warning-*`, `error-*`, `info-*` (50–950)
   - Generate each scale from the base brand color: the base color sits around 500–600, lighter tints go toward 50 and darker shades toward 950. Keep the hue consistent, and adjust saturation so the extremes don't look washed out or muddy.
2. **Semantic tokens**: meaningful names that point to primitives. **Designs and code only use these.** Every semantic token has a **Light** value and a **Dark** value.

### 2.2 Semantic tokens (Light / Dark)

The defaults below are a starting point. Adjust the steps until every pair passes the contrast rules in 2.3.

**Brand**
| Token | Light | Dark |
|---|---|---|
| `brand-primary` | brand-primary-600 | brand-primary-500 |
| `brand-primary-subtle` | brand-primary-50 | brand-primary-950 |
| `brand-secondary` | brand-secondary-600 | brand-secondary-500 |
| `brand-secondary-subtle` | brand-secondary-50 | brand-secondary-950 |
| `brand-tertiary` | brand-tertiary-600 | brand-tertiary-500 |
| `brand-tertiary-subtle` | brand-tertiary-50 | brand-tertiary-950 |

**Text**
| Token | Light | Dark | Used for |
|---|---|---|---|
| `text-title-primary` | neutral-950 | neutral-50 | Display, H1–H3 |
| `text-title-secondary` | neutral-800 | neutral-200 | H4–H6, card titles |
| `text-title-tertiary` | neutral-600 | neutral-400 | Subtitles, small titles |
| `text-body-primary` | neutral-800 | neutral-200 | Main paragraphs |
| `text-body-secondary` | neutral-600 | neutral-400 | Supporting text, descriptions |
| `text-body-tertiary` | neutral-500 | neutral-500 | Meta info, captions, footnotes |
| `text-disabled` | neutral-400 | neutral-600 | Disabled text |
| `text-inverse` | neutral-0 | neutral-950 | Text on `bg-inverse` |
| `text-on-brand` | neutral-0 | neutral-0 | Text on brand-colored fills |
| `text-link` | brand-primary-600 | brand-primary-400 | Links |
| `text-link-hover` | brand-primary-700 | brand-primary-300 | Link hover |

**Background** (page and section level)
| Token | Light | Dark | Used for |
|---|---|---|---|
| `bg-primary` | neutral-0 | neutral-950 | Main page background |
| `bg-secondary` | neutral-50 | neutral-900 | Alternating sections |
| `bg-tertiary` | neutral-100 | neutral-800 | Emphasized sections |
| `bg-inverse` | neutral-950 | neutral-50 | Inverted sections, footer |
| `bg-brand` | brand-primary-600 | brand-primary-700 | Brand-colored sections and CTA banners |
| `bg-overlay` | neutral-950 at 60% | neutral-950 at 70% | Behind modals and drawers |

**Surface** (cards, modals, menus, inputs, anything that sits on a background)
| Token | Light | Dark | Used for |
|---|---|---|---|
| `surface-default` | neutral-0 | neutral-900 | Cards, inputs |
| `surface-raised` | neutral-0 + shadow | neutral-800 | Modals, dropdowns, popovers |
| `surface-sunken` | neutral-100 | neutral-950 | Wells, code blocks, inset areas |
| `surface-hover` | neutral-50 | neutral-800 | Hovered card or row |
| `surface-selected` | brand-primary-50 | brand-primary-950 | Selected card or row |

**Border**
| Token | Light | Dark | Used for |
|---|---|---|---|
| `border-subtle` | neutral-100 | neutral-800 | Dividers |
| `border-default` | neutral-200 | neutral-700 | Card and input outlines |
| `border-strong` | neutral-400 | neutral-500 | Emphasized outlines, hovered inputs |
| `border-focus` | brand-primary-500 | brand-primary-400 | Focus ring |
| `border-brand` | brand-primary-600 | brand-primary-400 | Selected or brand outlines |
| `border-error` | error-600 | error-400 | Invalid inputs |

**Button**
| Token | Light | Dark |
|---|---|---|
| `button-primary-bg` | brand-primary-600 | brand-primary-500 |
| `button-primary-bg-hover` | brand-primary-700 | brand-primary-400 |
| `button-primary-bg-pressed` | brand-primary-800 | brand-primary-300 |
| `button-primary-text` | neutral-0 | neutral-0 or neutral-950 (whichever passes contrast) |
| `button-secondary-bg` | transparent | transparent |
| `button-secondary-bg-hover` | neutral-50 | neutral-800 |
| `button-secondary-bg-pressed` | neutral-100 | neutral-700 |
| `button-secondary-border` | neutral-300 | neutral-600 |
| `button-secondary-text` | neutral-950 | neutral-50 |
| `button-tertiary-text` | brand-primary-600 | brand-primary-400 |
| `button-tertiary-bg-hover` | brand-primary-50 | brand-primary-950 |
| `button-destructive-bg` | error-600 | error-500 |
| `button-destructive-bg-hover` | error-700 | error-400 |
| `button-destructive-text` | neutral-0 | neutral-0 |
| `button-disabled-bg` | neutral-100 | neutral-800 |
| `button-disabled-text` | neutral-400 | neutral-600 |

**Status** (the same pattern for `success`, `warning`, `error` and `info`)
| Token | Light | Dark |
|---|---|---|
| `success-bg` | success-50 | success-950 |
| `success-text` | success-700 | success-300 |
| `success-border` | success-200 | success-800 |
| `success-icon` | success-600 | success-400 |

**Icon**
| Token | Light | Dark |
|---|---|---|
| `icon-primary` | neutral-800 | neutral-200 |
| `icon-secondary` | neutral-500 | neutral-400 |
| `icon-brand` | brand-primary-600 | brand-primary-400 |
| `icon-on-brand` | neutral-0 | neutral-0 |
| `icon-disabled` | neutral-400 | neutral-600 |

### 2.3 Contrast rules (WCAG 2.2 AA)

Check every text and icon token against the background or surface it sits on, in **both** modes.
- **Body text below 24px:** at least **4.5:1**.
- **Large text** (24px and up, or 19px+ bold) and icons: at least **3:1**.
- **Borders that show where an input is** (input outlines, focus ring): at least **3:1**. Decorative dividers are exempt.
- If a pair fails, move the token one or two primitive steps darker (light mode) or lighter (dark mode). Don't change the primitive itself.
- `text-disabled` and `button-disabled-*` are exempt, but should still be visible.

### 2.4 Dark mode rules

- Dark mode is **not** a simple inversion. Use the mapped values above.
- Avoid pure black for large areas. `neutral-950` should be a very dark tinted gray (e.g. #0A0A0B).
- In dark mode, lighter surfaces mean higher elevation: `bg-primary` < `surface-default` < `surface-raised`.
- Brand colors usually need a slightly lighter or less saturated step in dark mode, so they don't glow.
- Shadows are barely visible in dark mode. Show elevation with a lighter surface or a `border-subtle` outline instead.

---

## Part 3 — Output

Deliver all of the following.

### 3.1 Style guide document
1. **Typography specimen:** every style for desktop and mobile, with size, line height %, letter spacing % and weight, each shown with sample text.
2. **Color palette:** every primitive scale shown as swatches with hex values.
3. **Semantic token table:** name, Light value, Dark value, what it's used for, and the contrast ratio where relevant.

### 3.2 CSS

```css
:root {
  /* Typography — desktop */
  --font-heading: "Inter", system-ui, sans-serif;
  --font-body: "Inter", system-ui, sans-serif;
  --h1-size: 3.75rem; --h1-line-height: 1.1; --h1-letter-spacing: -0.02em;
  /* …every style… */

  /* Color — light (default) */
  --color-text-title-primary: #0A0A0B;
  --color-bg-primary: #FFFFFF;
  --color-button-primary-bg: #4F46E5;
  /* …every token… */
}

@media (max-width: 767px) {
  :root {
    --h1-size: 2rem; --h1-line-height: 1.2; --h1-letter-spacing: -0.01em;
    /* …mobile sizes… */
  }
}

[data-theme="dark"] {
  --color-text-title-primary: #FAFAFA;
  --color-bg-primary: #0A0A0B;
  /* …every token, dark values… */
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { /* same dark values */ }
}

.h1 {
  font-family: var(--font-heading);
  font-size: var(--h1-size);
  line-height: var(--h1-line-height);
  letter-spacing: var(--h1-letter-spacing);
  font-weight: 600;
  text-wrap: balance;
}
```

If the project uses Tailwind, also output the same tokens as `theme.extend` values (or as `@theme` variables in Tailwind v4).

### 3.3 Figma
- **Text styles:** `desktop-*` and `mobile-*` sets, with line height and letter spacing in %.
- **Variable collection "primitives":** every raw color.
- **Variable collection "tokens":** every semantic token, with two modes, **light** and **dark**, each pointing to a primitive (an alias, not a hard-coded hex).
- Names use hyphens (`text-title-primary`), not slashes.

---

## Part 4 — QA Checklist

- [ ] The ratio was confirmed and the display count and heading levels follow the table in 1.1
- [ ] The mobile set uses the right mobile ratio and the same style names as desktop
- [ ] All sizes are rounded (even below 32px, multiples of 4 from 32px up)
- [ ] All line heights and letter spacings are in % (unitless / em in CSS)
- [ ] Body, label, overline and footnote use the fixed sizes
- [ ] Every semantic token has a Light and a Dark value
- [ ] Every text/background pair passes WCAG AA in both modes
- [ ] No design or code uses primitives directly; only semantic tokens
- [ ] All names use hyphens; there are no slashes
- [ ] Line-breaking rules are applied (balance, pretty, max 65ch, no hyphenated headings)
