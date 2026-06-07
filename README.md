# Wind kunnen we pakken — De Kerkhovense Molen

T-shirt / merchandise artwork for **De Kerkhovense Molen**, a working windmill and
monument in Oisterwijk run by volunteers. The shirts are sold in the shop to help
fund upkeep of the monument.

The whole design hinges on the mill's wordplay:

> **"Brood en lucht kun je bakken. Wind kunnen we _pakken_!"**
> _Bread and air you can bake — but only a mill can catch the wind._

So the central image is **a mill catching the wind**: the breeze is drawn as flowing
lines that curl into the turning sails (wieken).

## The brief

| | |
|---|---|
| **Purpose** | Merchandise sold in the mill shop (income for monument upkeep) |
| **Variants** | Two — one for **adults / mill-fanatics**, one for **kids** |
| **Phase 1** | Design **the image** ("how do you show a mill catching wind?") |
| **Phase 2** | Place the image on the shirt: print position, sizes, photo mockups |
| **Brand** | Must follow the brandbook — palette only, no neon, logo-consistent |
| **Open** | Front-only vs front+back, quantities, deadline (Phase 2, non-blocking) |

This is also a trial: doing it well is meant to lead to a follow-on **website project**.

## What's in this repo

| File | Description |
|---|---|
| [`index.html`](index.html) | **Main deliverable.** Both concepts as clean vector (SVG): Fase 1 (the image) + Fase 2 (on the shirt, with interactive shirt-colour preview) + Achterkant option + download links. |
| `art-adults.svg` / `art-kids.svg` | Front artwork — **editable source** (live text, needs the fonts). |
| `art-adults-back.svg` / `art-kids-back.svg` | Back artwork (typographic) — editable source. |
| `*-print.svg` (×4) | **Hand-to-printer versions** — text converted to vector outlines, transparent background, no font dependency. These are what the page links to download. |
| `kerkhovense-molen-tshirt-concepts.html` | Earlier draft, kept for reference. |
| `2026-02-14 … Brandbook.pdf` | Official huisstijl: logo, palette, voice & tone, do's/don'ts. |
| `Horrible.jpeg` / `worse.jpeg` | The earlier AI attempts (off-brand) — kept as "before" references. |
| `session_prompts.txt` | Full brief / conversation history that produced this work. |

## Brand palette (from the brandbook)

| Name | HEX |
|---|---|
| Wit | `#FFFFFF` |
| Graanbeige | `#E5D4B3` |
| Tuingroen | `#7B9B6F` |
| Molenbruin | `#412F26` |

Tagline: **"Natuurlijk gezond · sinds 1369"**. Logo = a *stellingmolen* (gallery
tower mill) in an engraving line-style.

> **Note — brandbook inconsistency:** the palette page lists Molenbruin as
> HEX `#412F26` **but** RGB `121 96 67` (which is actually `#796043`). These don't
> match. We use `#412F26` here; worth confirming the canonical brown with the
> bestuur before any print run.

## Viewing

Open [`index.html`](index.html) in any browser — no build step, no dependencies
(fonts load from Google Fonts).

```sh
open index.html
```

## Status & next steps

- [x] Phase 1 — the image, both variants, on-brand
- [x] Print-ready standalone SVGs per variant (front)
- [x] Text converted to vector outlines — `*-print.svg` need no fonts
- [x] Back-print option (typographic), both variants, outlined
- [x] Refined mill: engraving detail for adults (`#mill-detail`), clean mill kept for kids
- [ ] Pick the direction with the chairman / bestuur
- [ ] Confirm front/back, quantities, deadline

### Regenerating the outlined `*-print.svg`

The outliner script lives at `/tmp/outline.py` (uses `fonttools`; fonts cached in
`/tmp/fonts`). It reads each editable `art-*.svg`, converts `<text>` to glyph paths,
strips the font `@import`, and writes the matching `*-print.svg`. Re-run after editing
any source artwork's text.
