# Leoprado Academy — TutorLMS business template (static prototype)

Homepage prototype for a TutorLMS course-selling theme aimed at solo business,
strategy and finance instructors. Built from the "upcoming" Figma file (home frame).

Open `index.html` in a browser — no build step.

```
academy/
├── index.html          # homepage
└── assets/
    ├── css/style.css   # design tokens + all components
    ├── js/main.js      # mobile nav, course filter, pricing toggle, reveal/scroll-spy
    └── img/            # images exported from the Figma file
```

Sections: announcement bar, header, hero, student-company logos, course grid
(filterable), results, program roadmap, instructor, reviews, pricing
(monthly/yearly toggle), FAQ, newsletter CTA, footer.

Next: course archive, single course, lesson, dashboard and checkout pages, then
port to a WordPress theme with TutorLMS template overrides.

## Style guide

All tokens live at the top of `assets/css/style.css`. Never set a font size or
family directly on a component — use a role.

**Typeface:** Geist for everything, Geist Mono for labels. No other faces.

| Role      | Token          | Use for                                              |
|-----------|----------------|------------------------------------------------------|
| mega      | `--t-mega`     | Masthead and giant background word only              |
| display   | `--t-display`  | Hero headline, closing CTA headline, featured quote  |
| h2        | `--t-h2`       | Every section title                                  |
| h3        | `--t-h3`       | Card, phase, plan and sticker titles                 |
| stat      | `--t-stat`     | Every big number                                     |
| title     | `--t-title`    | List items, FAQ questions, short quotes, captions     |
| lead      | `--t-lead`     | Intro paragraph under a title                        |
| body      | `--t-body`     | Running text                                         |
| small     | `--t-small`    | Meta, captions, fine print                           |
| label     | `--t-label`    | Eyebrows, datelines, tags (mono, uppercase)          |

Headlines are sentence case. Only labels are uppercase.

**Spacing:** sections use `--space-section` top and bottom; label → title is
`--gap-label`; title → lead is `--gap-text`; section head → content is
`--space-head`. Section heads are left-aligned (label + title on the left,
lead or control on the right); the About statement is the one centered block.

## Versions

| Version            | Where                                  | Notes                                                        |
|--------------------|----------------------------------------|--------------------------------------------------------------|
| Poster (current)   | `index.html`                           | Poster hero and CTA, staircase, magazine-cover instructor     |
| Structural Grid    | `versions/structural-grid/index.html`  | Whole page on a visible 12-column grid with a left rail; own `style.css` |
