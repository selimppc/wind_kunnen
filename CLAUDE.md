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
  - **The mill is the org's real, official logo mill** — vectorized from `assets/DKM-logo-master.jpg` (their hand-drawn lookalike `#mill`/`#mill-detail` are retired; `#mill` survives only as the tiny topbar icon). The vector mill lives as `<g id="mill-logo">`: two stacked tone layers — grey tower at `opacity="0.42"` + black linework at full ink, both `fill="currentColor"`, so it takes the `--ink` colour of the nearest `.adult`/`.kids` ancestor and recolours per shirt. It is placed into the 440×660 artwork with `transform="translate(34 132) scale(0.235)"`.
  - **Fase 1 panels** just `<img src="art-adults.svg">` / `art-kids.svg` (fixed colour, always matches the print files). **Fase 2 shirt cards** inline `<use href="#mill-logo">` so the colour-swatch script can recolour them. Don't hand-edit the mill paths — regenerate via `tools/build_art.py`.
  - Two concepts share styling via ancestor classes: **`.adult`** (heritage, Playfair, thin green wind swirls) and **`.kids`** (Fredoka, green `pakken!`, bold green gusts + dots). Same official mill in both; the kid/adult difference is type + wind treatment, not the mill.
  - The shirt-colour swatches are wired in the `<script>` at the bottom (`.card .swatch`); the Fase 1 panels are intentionally fixed-colour (no swatches).
- `kerkhovense-molen-tshirt-concepts.html` is the older draft — leave it; `index.html` supersedes it.

## Export / print files

- Front: `art-adults.svg` / `art-kids.svg`. Back (typographic): `art-adults-back.svg` / `art-kids-back.svg`. These are the **editable sources** (live `<text>`, reference Google Fonts).
- `*-print.svg` are the **hand-to-printer** copies: text converted to vector outlines, no font dependency, transparent background. `index.html` download links point to these.
- Regeneration pipeline (scripts in `tools/`):
  - `python3 tools/build_art.py` rebuilds `art-adults.svg`/`art-kids.svg` from the traced mill (`tools/millA.svg` = tower tone, `tools/millB.svg` = linework) + catchphrase + wind + wordmark. Edit copy/wind/placement there, not in the generated SVGs.
  - `python3 tools/outline.py` maps each `art-*.svg` → `art-*-print.svg`, replacing `<text>` in document order (keep the four blocks ph1, ph2, wm1, wm2 in that order) and stripping the font `@import`. Needs `fonttools`; fonts cached in `/tmp/fonts` (Playfair Display, Fredoka, Arimo≈Arial).
  - Always verify a regenerated `*-print.svg` has `<text>:0` and no `@import`.
- The mill was vectorized once from `assets/DKM-logo-master.jpg` with `potrace` (two masks: black linework + grey tower). To re-trace, see the "Official logo" section in README.md.
- **Logo-usage caveat:** the brandbook forbids modifying/combining the logo without permission. We recolour it (brand palette, per shirt) and pair it with the slogan, keeping proportions. It's the org's own merch, but flag for bestuur sign-off before print.

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
