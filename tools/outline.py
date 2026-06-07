#!/usr/bin/env python3
import re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.varLib.instancer import instantiateVariableFont

FONTS = "/tmp/fonts"

def load(path, axes):
    f = TTFont(f"{FONTS}/{path}")
    if "fvar" in f:
        have = {a.axisTag for a in f["fvar"].axes}
        pin = {k: v for k, v in axes.items() if k in have}
        if pin:
            instantiateVariableFont(f, pin, inplace=True)
    return f

def outline(font, text, size, x, y, fill, anchor="middle", ls=0.0, opacity=None):
    upem = font["head"].unitsPerEm
    s = size / upem
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    names, advs = [], []
    for ch in text:
        gn = cmap.get(ord(ch), ".notdef")
        names.append(gn)
        advs.append(hmtx[gn][0] * s)
    total = sum(advs) + ls * len(text)
    penx = x - total / 2 if anchor == "middle" else (x - total if anchor == "end" else x)
    op = f' fill-opacity="{opacity}"' if opacity is not None else ""
    out = [f'<g fill="{fill}"{op}>']
    for gn, adv, ch in zip(names, advs, text):
        if ch != " ":
            pen = SVGPathPen(gs)
            gs[gn].draw(pen)
            d = pen.getCommands()
            if d:
                out.append(
                    f'<path transform="translate({penx:.2f} {y:.2f}) '
                    f'scale({s:.5f} {-s:.5f})" d="{d}"/>'
                )
        penx += adv + ls
    out.append("</g>")
    return "\n  ".join(out)

playfair      = load("PlayfairDisplay.ttf", {"wght": 600})
playfair_bi   = load("PlayfairDisplay-Italic.ttf", {"wght": 700})
fredoka_sb    = load("Fredoka.ttf", {"wght": 600, "wdth": 100})
fredoka_bold  = load("Fredoka.ttf", {"wght": 700, "wdth": 100})
arimo_bold    = load("Arimo.ttf", {"wght": 700})
arimo_reg     = load("Arimo.ttf", {"wght": 400})

BROOD = "Brood en lucht kun je bakken"
WIND  = "Wind kunnen we pakken!"
WM1   = "DE KERKHOVENSE MOLEN"
WM2   = "OISTERWIJK · NATUURLIJK GEZOND · SINDS 1369"
BR    = "#412F26"
GR    = "#7B9B6F"

# four outline groups per file, in document order
JOBS = {
    "art-adults.svg": [
        outline(playfair,    BROOD, 21,  220, 56,  BR),
        outline(playfair_bi, WIND,  27,  220, 97,  BR),
        outline(arimo_bold,  WM1,   14,  220, 624, BR, ls=1.6),
        outline(arimo_reg,   WM2,   8.4, 220, 642, BR, ls=0.8, opacity=0.85),
    ],
    "art-kids.svg": [
        outline(fredoka_sb,   BROOD, 20,  220, 56,  BR),
        outline(fredoka_bold, WIND,  26,  220, 98,  GR),
        outline(arimo_bold,   WM1,   14,  220, 624, BR, ls=1.6),
        outline(arimo_reg,    WM2,   8.4, 220, 642, BR, ls=0.8, opacity=0.85),
    ],
    "art-adults-back.svg": [
        outline(playfair,    BROOD, 24,  300, 64,  BR),
        outline(playfair_bi, WIND,  42,  300, 120, BR),
        outline(arimo_bold,  WM1,   14,  300, 232, BR, ls=1.6),
        outline(arimo_reg,   WM2,   8.4, 300, 250, BR, ls=0.8, opacity=0.85),
    ],
    "art-kids-back.svg": [
        outline(fredoka_sb,   BROOD, 24,  300, 64,  BR),
        outline(fredoka_bold, WIND,  42,  300, 120, GR),
        outline(arimo_bold,   WM1,   14,  300, 232, BR, ls=1.6),
        outline(arimo_reg,    WM2,   8.4, 300, 250, BR, ls=0.8, opacity=0.85),
    ],
}

text_re = re.compile(r'<text\b[^>]*>.*?</text>', re.S)
import_re = re.compile(r'\s*@import url\(.*?\);', re.S)

for src, groups in JOBS.items():
    svg = open(f"/Users/tipu.arbeid/Sites/wind_kunnen/{src}").read()
    it = iter(groups)
    svg = text_re.sub(lambda m: next(it), svg)
    svg = import_re.sub("", svg)
    svg = svg.replace(
        "Print-ready vector.",
        "Print-ready vector. Tekst is omgezet naar outlines — geen lettertype nodig.",
    )
    dst = src.replace(".svg", "-print.svg")
    open(f"/Users/tipu.arbeid/Sites/wind_kunnen/{dst}", "w").write(svg)
    remaining = len(text_re.findall(svg))
    print(f"{dst}: replaced {len(groups)} text blocks, {remaining} <text> remaining, {len(svg)} bytes")
