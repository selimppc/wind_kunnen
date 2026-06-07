# Wind kunnen we pakken — De Kerkhovense Molen

T-shirt / merchandise artwork for **De Kerkhovense Molen**, a working windmill and
monument in Oisterwijk run by volunteers. The shirts are sold in the shop to help
fund upkeep of the monument.

The whole design hinges on the mill's wordplay:

> **"Brood en lucht kun je bakken. Wind kunnen we _pakken_!"**
> _Bread and air you can bake — but only a mill can catch the wind._

So the central image is **the mill catching the wind**: the breeze is drawn as flowing
lines that curl into the turning sails (wieken).

The mill in the artwork is **the organisation's own official logo mill**, vectorized
from their master logo file so it prints razor-sharp at any size (the raw logo is a
small raster JPEG) — see [Official logo](#official-logo-vectorized) below.

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
| `assets/DKM-logo-master.jpg` | The org's high-res master logo (source for the vectorized mill). |
| `tools/` | Regeneration scripts: `build_art.py` (compose artwork), `outline.py` (text→outlines), `millA.svg`/`millB.svg` (the traced mill). |
| `kerkhovense-molen-tshirt-concepts.html` | Earlier draft, kept for reference. |
| `2026-02-14 … Brandbook.pdf` | Official huisstijl: logo, palette, voice & tone, do's/don'ts. |
| `Horrible.jpeg` / `worse.jpeg` | The earlier AI attempts (off-brand) — kept as "before" references. |
| `session_prompts.txt` | Full brief / conversation history that produced this work. |

## Official logo (vectorized)

The artwork uses the **real De Kerkhovense Molen logo**, not a redrawn lookalike —
people are attached to it (the mill is ~100 years old). Because the only available
logo files are small raster JPEGs (the website's is 300×160), the mill was
**vectorized** so it prints crisp at any size:

1. Downloaded the high-res master (`…basisbestand-2048×1095.jpg`) → `assets/DKM-logo-master.jpg`.
2. Cropped the mill (dropping the wordmark + tagline bar).
3. Built two masks — **black linework** and the **grey tower tone** — and traced each
   with `potrace` → `tools/millA.svg` (tower) + `tools/millB.svg` (lines).
4. Composed as a two-tone mill: tower at 42 % ink tint, linework at full ink, both
   drawn with `currentColor` so it takes the shirt's brand colour like the rest of the art.

Proportions are preserved (uniform scale); only the colour is mapped to the brand
palette per shirt.

> **Note — logo usage:** the brandbook says the logo may only be used "in originele
> kleuren en proporties" and not be modified/combined without permission. Here it's
> the org's own merchandise, proportions are kept, and only brand colours are used —
> but recolouring + combining with the slogan is worth a quick **bestuur OK** before print.

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
- [x] **Official logo mill vectorized & integrated** (both variants, front + shirts)
- [ ] Pick the direction with the chairman / bestuur
- [ ] Confirm logo-usage OK with bestuur (recolour/combine — see note above)
- [ ] Confirm front/back, quantities, deadline

### Regenerating the files

- **Artwork:** `python3 tools/build_art.py` → rewrites `art-adults.svg` / `art-kids.svg`
  from the traced mill (`tools/millA.svg` + `tools/millB.svg`) plus text/wind.
- **Print versions:** `python3 tools/outline.py` → converts `<text>` to glyph outlines
  and strips the font `@import`, writing each `*-print.svg`. Needs `fonttools`; fonts
  are fetched to `/tmp/fonts` (Playfair Display, Fredoka, Arimo≈Arial).
- Always verify a regenerated `*-print.svg` has `<text>:0` and no `@import`.
