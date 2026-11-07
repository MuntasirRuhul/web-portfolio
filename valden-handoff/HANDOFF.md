# Valden handoff (read this first after a context compaction)

Last updated: 2026-11-08. Written at the end of a long session so a fresh context can continue.

## 1. The project in one paragraph
**Valden** is a concept one-page coffee storefront (fictional "grand cru" brand, placeholder names and sample prices).
Look: warm cream / maroon / terracotta / gold, chunky Titan One display type, Mouse Memoirs tape labels, DM Sans body,
playful scroll scenes. Final design lives in **Figma**; we **iterate in HTML**; Figma is only touched when the user asks.
Product placeholders: Helios "First Light" instant jar (hero, shop corner), tins Nuit / Velours / Aurore / Le Coffret.

## 2. Working rules (user's explicit preferences, follow them)
1. **Experiments are always separate.** One folder + one published link each. Never publish an experiment onto the main link.
   Main only changes after the user says a direction is approved, then move it over once.
2. **HTML first, Figma last.** The user said "final design will be in Figma", but "do not touch Figma unless I ask".
   (I broke this once by building the Brew Bar in Figma unasked; user said "fine". Do not repeat.)
3. **Be token-friendly.** Short answers, one change at a time, one screenshot of the changed section, avoid 5-option
   comparison pages unless asked. The user watches token cost and context use.
4. **Say what you did not check** (e.g. phone view, published page). Do not claim Figma/web access you do not have.
5. Ask before touching other branches/sessions. (Exception granted once: copied the figma-expert skill to the
   Elena Varga Atelier branch `claude/vigilant-ramanujan-yihv1h`.)

## 3. Links
| What | URL |
|---|---|
| **MAIN page (v1, approved baseline)** | https://claude.ai/artifact/3UWzMufGStwAajWZPy9neE |
| **v2 experiment (Heist-inspired info sections)** | https://claude.ai/artifact/KvTXopEoD7Q1iVmhfx6ZiK |
| Shop profile card experiments | feed GdLsk7hSNnYbjMZAzjCace, styles HUqGqYhBfm6qAv9NhsFLoL, variants TjncvjWkF6gx7HdXPKn3Nn |
| Text-tile ideas | tiles QhpemctL9uz35CsoxiRfFK, tiles-2 H7BW9w5B8BCWvMcWF4NrFE |
| Polished shop card | https://claude.ai/artifact/NP85kgT9tPXzpVuvhQxvj7 |
| Background shapes / shop on shape | bg QxztbT7g6HnswaeUMDbVFM, shop-shapes 8GF3ziWJbTbbj3Jr3cNYp9 |
| **Bean + Brew Bar merges (5 variants, Heist-style claims layout)** | source: `experiments/bean-merge/index.html` (link added in section 11) |
| Earlier idea pages | ribbons 7myURUmnErY5u4SveJL6VV, shop Fi4ZivdGtrmJS6xJ6WLHho, brew Ad124JwiKjNtdF1WC1vtwf, closing JrvG94yTB3ccgv9XpcR8fj, invitation 1xzHb8YC2JjBKGDWn6kaPh |
| Figma file | https://www.figma.com/design/LR0CyHXtwvuIzxqA42ccDc/coffee-briew (home frame node `40:32`) |
All artifact links are private to the user (claude.ai/artifact/<id>). Republish = same `file_path` + `url`.

## 4. Where the files are
- **This repo folder** (`valden-handoff/`, committed on branch `claude/gifted-planck-eie5g2`):
  - `snapshot-v1-main/` = frozen copy of the current MAIN page: `index.html` (published output), `img/`, `build.py`,
    `src/Main.dc.html` (original design source from the user's zip).
  - `v2/` = build script + output of the v2 experiment.
  - `experiments/*/index.html` = every experiment page (sources only, images are in `snapshot-v1-main/img/`).
- **Session scratchpad** (may vanish): `/tmp/claude-0/-home-user-web-portfolio/ae4ab52b-784c-5b50-a1fc-4ff19b51af15/scratchpad/`
  with `build_valden.py` (main build), `vsite/` (published main + img), `experiments/<name>/`.
- **To rebuild from this repo** (new session): 
  ```bash
  S=$PWD/work; mkdir -p $S/valden/Valden/project $S/experiments/valden-v2 $S/vsite/img
  cp valden-handoff/snapshot-v1-main/src/Main.dc.html $S/valden/Valden/project/
  cp valden-handoff/snapshot-v1-main/img/* $S/vsite/img/ ; cp valden-handoff/snapshot-v1-main/img/* $S/experiments/valden-v2/img/ 2>/dev/null
  cp valden-handoff/snapshot-v1-main/build.py $S/build_valden.py && python3 -I $S/build_valden.py $S   # -> $S/valden.html
  ```
  (`v2/build.py` writes `$S/experiments/valden-v2/out.html`.) Publish with the Artifact tool using `files` for `img/*`.
  Page needs a wrapper (`<!doctype html>...`) only for local Playwright tests; the Artifact tool wraps it itself.

## 5. How the page is built (important)
The design source is `Main.dc.html` (a "Design Component" template: `{{value}}`, `<sc-for>`, `<sc-if>`, a `DCLogic` class).
The canvas runtime is not available, so `build.py` **ports it to plain HTML**: it extracts CSS/markup/script, adds a tiny
template shim (renders the template, wires onClick/onChange, morphs DOM), and applies **ordered patches** (python
`markup.replace`/`script.replace` blocks inside `build.py`, each marked with a `# ----------` comment). Patch order:
mobile CSS, header/section classes, review cards (Figma card style), blend order (Velours, Aurore, Nuit), hero (Helios
jar + doodle arrow), ribbons (wave dividers with text), notebook heading hidden, shop **sliding panels**, brew bar
**profile card with poster grid**, closing **boarding-pass ticket**, sharp doodle arrow everywhere, neutral brew tips.
Gotchas learned: bound-class name collisions (`.v-bt` clashed once), re-binding Figma variable twice gives black fill,
string `assert` before every replace, SVG `textPath` ids must be unique.

## 6. Current state of MAIN (v1) by section
Header, Hero (Helios jar, scroll-driven: rises and lands on a line-drawn table; beans float and burst), Interlude (6:58 AM
drawing), Blend showcase (pinned scroll, Velours > Aurore > Nuit), wave ribbon "DANGEROUSLY SMOOTH", Review-card stack
(Figma style, same photo avatar on all four for now), Shop (sliding panels, Nuit open, Helios jar stand-in), Brew Bar
(profile card + 3x3 recipe poster grid + jar), Closing (boarding-pass ticket), wave "GRAND CRU COFFEE", Footer.
Reduced motion respected; basic phone stacking below 900px (not a designed mobile pass).

## 7. v2 experiment (what changed, vs main v1)
Inspired by the user's reference site **heist.co** (specialty decaf; dark + cream + one red-orange accent; mono labels;
proof/"receipts"; method comparison table; story; FAQ). We took *presentation structure*, not their brand or copy:
- **Facts strip** (dark band, big gold numerals 03 blends / 01 gift box / 04 brew methods / 00 rush, mono labels + ticker) before the Shop.
- **Method comparison table** under the Brew Bar, driven by the cup stepper, active method highlighted.
- **"Which tin is yours?"** comparison table (roast, notes, best for, price) + **FAQ accordion** (5 questions) before the Closing.
- **DM Mono** for small labels (brew card, poster tile labels). All new copy is derived from existing content. No invented proof,
  scores or reviews (Valden is a concept). FAQ says prices are sample prices / demo checkout.
Open: v2 phone view looked OK at 400px in tests but only roughly checked; not yet approved, not on main.

## 8. Heist vs Valden (summary of the comparison already given to the user)
Heist = real DTC specialty **decaf / 1/4-caf** brand ("Coffee Without a Curfew"), Shopify, bags ~$30, instant 4/6-pack,
bundles, free-gift ladder, wholesale + affiliates; proof (water process 99.9%, lab tests, 93-pt review, 67 reviews), founder
story, FAQ; dark/cream/orange, mono + sans, 2-7px corners, "heist/newspaper" voice, lots of video + marquee strips.
Valden = concept, warmer/playful, very round shapes, richer interactions, but weak on promise, proof, story, FAQ.
Ideas still available to take: one-line promise + defined customer, real proof numbers (when real), story block with a named
human, gift ladder tied to Le Coffret, review score, a dark contrast section.

## 9. Pending decisions / next steps (ask the user)
1. **Pick a direction for the Shop**: sliding panels (main) vs **profile card** (experiments) vs profile card **on a shape**
   (user liked shape ideas S1 *hill* and S5 *layered hills*; polished version in shop-shapes).
2. Try **Hero background shape** (maroon hill/arch behind the jar) as a separate experiment (user suggested it).
3. Decide Valden's **niche + one-line promise** (needed before real copy).
4. Approve/trim v2 sections, then promote to main (build main from `v2/build.py` logic).
5. **Mobile pass** at 390px for every section, then **sync approved changes to Figma** in one go.
   Figma is behind the HTML on: boarding-pass size + fine print, sharp doodle arrow, wave text, Helios jar in shop panel,
   v2 sections, profile-card shop. Figma file already has variables (colour, space/radius), 12 text styles, 3 shadow styles,
   components (Button, Tape label, Add button, Shop panel, Poster tile) and pages `Valden / Components`, `Valden / Home (1920 current)`,
   `Valden / Archive` (old Brew Bar). Old Brew bar was archived, not deleted.
6. Replace placeholder images (user will make final jar/tin/avatar images) and the `[ADDRESS]` footer text.

## 10. Environment notes
- Network allowed hosts (Default env): `www.figma.com` (Figma image downloads), `www.heist.co` (added for the reference; can be removed).
- Skill **figma-expert** installed at `.claude/skills/figma-expert/SKILL.md` (this branch) and on branch
  `claude/vigilant-ramanujan-yihv1h` (Elena Varga Atelier). General Figma advice only.
- Artifact watch limit: 10 webhook triggers per session already used, so new artifacts do not get comment wake-ups. Ask the user to reply in chat.
- Figma MCP: call `create_session` first; load skills `figma-use` + `figma-generate-design` resources before `use_figma`.
- The Stop hook asks to commit untracked files: commit + push to `claude/gifted-planck-eie5g2` (never open a PR unless asked).

## 11. Latest iteration: bean + Brew Bar merge (added 2026-11-08)
User screenshot compared our Brew Bar (left) with Heist's "Roasted in Small Batches with Big Standards" (right: 3 claims
each side of one hero object, dividing lines, a red outlined image with a tag, a lab-report callout). Ask: merge them, use the
**coffee bean** (our primary ingredient) as the hero, in Valden's style; 5 variants; keep separate.
Built `experiments/bean-merge/index.html` (split bean = two clipped copies of `img/bean-crop.webp`, outlined, tagged "WHOLE BEAN"):
B1 bean + claims, calculator strip below; B2 controls left / recipe tiles right, bean grows with cups; B3 dark hill section;
B4 annotated bean with numbered leader lines; B5 poster bento. All have a working method/cups calculator.
Claims are DRAFT copy from existing Valden content (Grand cru coffee, Small lots, Roasted to order, Sealed by hand,
Whole bean always, Brewed by weight): no invented proof. Next: user picks one, then tighten it, then fold into v2/main.
Typography notes from Heist (for a possible type-token experiment): Inter body 400 / subheading 500 / heading 700,
Adobe Fonts Aro (UI) + forma-djr-mono (labels); tokens for letter-spacing (-0.03/0/0.03/0.06/0.13/0.25em) and line-height
(display 1/1.1/1.2, heading 1.15/1.25/1.35, body 1.2/1.4). Valden could add the same token scale + named roles.

## 12. Latest iteration: bean panel with text background (added 2026-11-08)
User picked **B3 (dark hill)** from the bean merge. Asked: bean placeholder should have **text as a background** like their
"SMALL LOTS / SMALL LOTS / SMALL LOTS" fading poster, but more stylish; keep the (abstract) hill for now; wanted Pinterest research.
Note: **no browser tool exists in this session** (only Figma + WebFetch, Pinterest needs login), so no Pinterest browsing was possible;
styles were designed from standard typographic-poster techniques. If the user sends Pinterest screenshots, match them.
Source: `experiments/bean-text-bg/index.html`: panel `.bp` with 4 switchable text styles: Echo fade (default, closest to the poster),
Outline fade, Orbit rings (rotating SVG textPath), Tilted bands. Bean = `bean-crop.webp` split in two clipped halves (drop-shadow on the parent).
Gotcha: a grid item with `margin:auto` and only absolute children collapses to 0 width; use `width:100%` + `justify-self:center`.
Next: user picks a text style (or sends references), then fold this section into v2/main (replace or sit beside the Brew Bar).

## 13. MAIN page updated (2026-11-08): Brew Bar replaced by the bean section
User feedback on the text-background panel: "too clumsy and busy, the placeholder competes with the text, hierarchy unclear, too tight".
Decision: go back to the plain outlined bean frame, make the **bean bigger**, add space, clearer hierarchy (claim title in Titan One,
description in DM Sans sentence case, mono eyebrow/labels), then **put it on MAIN** (user explicitly asked).
- Main now has the new `#brew` section = "The bean": dark section with the abstract hill, headline "Roasted in small lots. Brewed to a number.",
  3 claims left / split outlined bean centre (grows slightly with cups) / 3 claims right, calculator below (pills, stepper, 4 numbers).
- `valden-handoff/main-current/` = the build script + published HTML of this version. `snapshot-v1-main/` is the frozen version BEFORE
  (sliding-panel shop + profile-card Brew Bar). To go back, republish `snapshot-v1-main/index.html` (+ img) to the main link.
- Not on main (still experiments): v2 facts strip / comparison table / FAQ, profile-card shop, text-background bean panel.
- Open: user to review main; decide shop direction; v2 sections; mobile pass; sync to Figma.

- Update (2026-11-08): user commented "remove this part" on the hill shape. The abstract hill behind the bean section was REMOVED from main (flat dark #3A1410 background now).
- Update (2026-11-08): user commented on the calculator block (`#brew > div:nth-of-type(3)`). The **calculator (method pills, cup stepper, 4 numbers) was REMOVED from the main bean section**. The page now has NO brew calculator on main. To restore it: use `scratchpad/build_valden.before-calc-removal.py` or the calculator markup in `main-current/build.py` history / `experiments/bean-merge`, `experiments/bean-text-bg`.

## 14. Experiment: Heist-style header + cleaner hero (2026-11-08) - NOT on main
User (dictated, a bit unclear): hero like Heist: "Shop now" button in the header, beside/instead of the bag; cart as a card shown on hover
("special cursor pair" on hover/interaction); remove the hero body text and the FIND YOUR TIN button; keep "Less rush. More roast." for now.
Built `experiments/hero-heist/` (build.py = main build + patch): header = red **SHOP NOW** pill + mono **CART (n)**; hovering/focusing CART shows a card
(empty message + "Shop the tins", or line items + subtotal + "Open bag"); touch devices skip the hover card; hero body copy + CTA removed.
Open question: "cursor pair" may mean a custom cursor that changes on hover (not built). Ask the user. Move to main only when approved.
Also pending from comments: user said my removal of the calculator (v29) may not match the area they marked (`#brew > div:nth-of-type(3)`, "2 elements");
ask what they marked or offer to restore v28 (before-calc-removal build kept in scratchpad `build_valden.before-calc-removal.py`).
