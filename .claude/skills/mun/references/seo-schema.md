# Launch SEO and schema markup

Apply this to public pages: marketing, landing, blog and product pages. Skip it for logged-in app screens.

## On-page essentials
- `<title>`: 50–60 characters, main topic first, brand last, unique on every page.
- `<meta name="description">`: 140–160 characters that describe the page honestly and make people want to click.
- One `h1` that matches the page's intent, with a logical `h2`/`h3` outline below it.
- Readable URLs: `/courses/beginner-poetry`, not `/page?id=12`.
- Descriptive link text and internal links to related pages.
- Image `alt` text describes the image (see the accessibility checklist), and file names are descriptive.
- `<link rel="canonical">`, `<meta name="viewport">` and `lang` are set.
- Open Graph and Twitter tags (`og:title`, `og:description`, `og:image` at 1200×630) for nice share previews.
- Mobile-friendly and fast (see the performance basics in the design critique).

## Site-level
- `robots.txt` and `sitemap.xml` at launch.
- A favicon set and `site.webmanifest`.
- No accidental `noindex` on live pages.

## Generative and answer engines (GEO/AEO)
- Answer the main question plainly near the top of the page.
- Use clear headings phrased like real questions, and a short FAQ where it genuinely helps.
- State facts concretely (who, what, price, duration, location) so AI search tools can quote them correctly.

## Schema markup (JSON-LD)
Add one `<script type="application/ld+json">` per relevant type. **Only describe content that is visible on the page and true.** Never add fake ratings or reviews.

| Page | Schema types |
|---|---|
| Home / about | `Organization` or `Person`, `WebSite` |
| Course | `Course` (with `provider`, `offers`, `hasCourseInstance`) |
| Product | `Product` + `Offer` |
| Article / blog | `Article` or `BlogPosting` (with `author`, `datePublished`) |
| FAQ section | `FAQPage` |
| Local business | `LocalBusiness` (with `address`, `openingHours`) |
| Event | `Event` |
| Any deep page | `BreadcrumbList` |

Validate with Google's Rich Results Test and the Schema.org validator.
