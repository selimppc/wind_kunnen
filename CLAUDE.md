# CLAUDE.md

Guidance for Claude Code when working in this repo. See [README.md](README.md) for
the human-facing overview.

## What this is

A small, **static design project** — t-shirt / merchandise artwork for *De
Kerkhovense Molen* (a volunteer-run windmill monument in Oisterwijk). No build
system, no framework, no dependencies. The deliverable is hand-authored HTML + inline
SVG that renders crisp at any size and hands straight to a printer.

The whole design exists to land one wordplay:

> "Brood en lucht kun je bakken. Wind kunnen we **pakken**!"
> (Bread and air you can bake — but a mill _catches_ the wind.)

So the recurring visual is **a mill whose sails scoop up flowing wind lines.**

## Main file

- **`index.html`** is the working file — keep iterating here.
  - Structure: topbar → hero (catchphrase) → palette → **Fase 1 (het beeld)** → **Fase 2 (op het shirt)** → footer notes.
  - Two mill symbols: `#mill` (clean/simple — used by kids + topbar) and `#mill-detail` (same silhouette plus engraving shading: tower hatching, cap boarding, gallery brackets — used by the **adults** front only). Both draw with `currentColor`, so colour comes from the `--ink` CSS var on the nearest `.adult`/`.kids` ancestor. If you change one mill's base geometry, change both. The adult standalone `art-adults.svg` inlines the detailed version (its shading group lives just before the mill `</g>`).
  - Two concepts share styling via ancestor classes: **`.adult`** (heritage, Playfair, thin engraving lines) and **`.kids`** (Fredoka, thick lines, smiling mill). The same artwork markup appears in both the Fase 1 panels and the Fase 2 shirt cards.
  - The shirt-colour swatches are wired in the `<script>` at the bottom (`.card .swatch`); the Fase 1 panels are intentionally fixed-colour (no swatches).
- `kerkhovense-molen-tshirt-concepts.html` is the older draft — leave it; `index.html` supersedes it.

## Export / print files

- Front: `art-adults.svg` / `art-kids.svg`. Back (typographic): `art-adults-back.svg` / `art-kids-back.svg`. These are the **editable sources** (live `<text>`, reference Google Fonts).
- `*-print.svg` are the **hand-to-printer** copies: text converted to vector outlines, no font dependency, transparent background. `index.html` download links point to these.
- To regenerate the `*-print.svg` after editing any source's text, re-run `/tmp/outline.py` (needs `fonttools`; fonts cached in `/tmp/fonts` — Playfair Display, Fredoka, Arimo≈Arial). It maps each `art-*.svg` → `art-*-print.svg`, replacing `<text>` in document order, so keep the four text blocks (ph1, ph2, wm1, wm2) in that order. Always verify a regenerated file has `<text>:0` and no `@import`.

## Hard brand rules (from the brandbook — do not break)

- **Only these four colours. No neon, nothing off-palette** — this is an explicit
  brandbook "don't", and exactly what the rejected AI attempts got wrong.
  - Wit `#FFFFFF` · Graanbeige `#E5D4B3` · Tuingroen `#7B9B6F` · Molenbruin `#412F26`
  - Helper shades already in use: `--green-dk:#5E7E54`, `--cream:#F4ECDB`, off-white bg `#FBF7EF`.
- Tagline is **"Natuurlijk gezond · sinds 1369"**; full wordmark "DE KERKHOVENSE MOLEN · OISTERWIJK".
- Keep the mill reading as a **stellingmolen** (tower mill with a gallery/stelling), in the spirit of the logo's engraving style.
- Warm, friendly, heritage tone — never corporate/cold.
- Brandbook quirk: Molenbruin is listed as HEX `#412F26` **and** RGB `121 96 67` (=`#796043`) — contradictory. We standardise on `#412F26`. Flag, don't silently switch.

## Two phases (the client thinks in these terms)

1. **Fase 1 — het beeld:** get the image right (mill catching wind), both adult + kids variants. This is what's approved first.
2. **Fase 2 — op het shirt:** placement, sizes, front/back, photo mockups, print-ready export (each design as its own SVG/PDF, text converted to outlines).

## Conventions

- Stay dependency-free and offline-friendly (only Google Fonts is remote). No npm, no bundler.
- Keep everything **vector** — never rasterise the artwork.
- Match the existing terse SVG-coordinate style; reuse `#mill` rather than redrawing.
- Dutch is the content language; keep copy in Dutch.

## Inspecting the brandbook PDF

`pdftotext`/`pdftoppm` are **not** installed. To read the brandbook, use `pypdf`
(`python3 -m pip install pypdf`) for text, and `page.images` to dump the embedded
logo/photos to inspect them.
