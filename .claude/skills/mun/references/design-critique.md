# Design critique

Use this for self-review before delivering, and when the user asks for a review. Give findings ranked by impact, each with a concrete fix.

## 1. First impression (5-second test)
- Can a newcomer tell what this is, who it's for, and what to do next?
- Is there one clear primary action per screen?

## 2. Hierarchy
- Size, weight, color and space lead the eye in the intended order.
- Only one element is the loudest. Everything else supports it.
- Related items are grouped, and spacing between groups is larger than spacing within them.

## 3. Consistency
- Colors, type sizes, radius, shadows and spacing come from the tokens, with no one-off values.
- Components look and behave the same everywhere.

## 4. Distinctiveness
- Would this look the same for any other product in the category? If yes, find the generic default (see `frontend-design.md`) and replace it with a choice tied to this subject.
- Remove one decoration that doesn't serve the brief.

## 5. Usability
- States are covered: hover, focus, active, disabled, loading, empty, error, success.
- Forms are short, labeled, forgiving, and give inline validation.
- Mobile: thumb-reachable actions, no tiny text, nothing cut off.

## 6. Performance basics
- Images are sized and in modern formats (WebP/AVIF), with `loading="lazy"` below the fold.
- At most two font families with only the weights used, and `font-display: swap`.
- No layout shift: images and embeds have width and height set.

## Output format for reviews
1. **Top 3 issues** (highest impact first): the problem, why it matters, the fix.
2. **Quick wins**: small changes worth making.
3. **What works**: keep these.
