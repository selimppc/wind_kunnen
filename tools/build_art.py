#!/usr/bin/env python3
"""
Rebuild art-adults.svg / art-kids.svg from the vectorized official mill.

Pipeline (one-time): assets/DKM-logo-master.jpg  -> crop mill -> 2 masks
(black linework + grey tower) -> potrace -> tools/millA.svg, tools/millB.svg.
This script then composes those traces with the catchphrase, wind and wordmark.
After running, re-run tools/outline.py to refresh the *-print.svg files.
"""
import os, re
HERE=os.path.dirname(os.path.abspath(__file__))
PROJ=os.path.dirname(HERE)

def paths(f): return ''.join(re.findall(r'<path d="[^"]*"/>', open(os.path.join(HERE,f)).read(), re.S))
A=paths('millA.svg'); B=paths('millB.svg')
TR='translate(0,1962) scale(0.1,-0.1)'
# two-tone: grey tower as 42% ink tint, black linework at full ink (both currentColor)
MILL=(f'  <g id="mill-logo" fill="currentColor" stroke="none">\n'
      f'    <g opacity="0.42" transform="{TR}">{A}</g>\n'
      f'    <g transform="{TR}">{B}</g>\n  </g>')
MT='translate(34 132) scale(0.235)'   # fit 1580x1962 mill into the 440x660 artwork

WM1='DE KERKHOVENSE MOLEN'
WM2='OISTERWIJK &#183; NATUURLIJK GEZOND &#183; SINDS 1369'

WIND_ADULT='''  <g class="wind">
    <path d="M8 138 C66 118 116 150 152 126"/>
    <path d="M152 126 c14 -10 6 -28 -10 -22"/>
    <path d="M20 172 C72 158 104 178 134 160"/>
    <path d="M432 138 C374 118 324 150 288 126"/>
    <path d="M288 126 c-14 -10 -6 -28 10 -22"/>
    <path d="M420 172 C368 158 336 178 306 160"/>
  </g>'''

WIND_KIDS='''  <g class="wind">
    <path d="M10 150 C70 116 120 156 150 124 c18 -16 -2 -40 -22 -24 c-10 8 -3 24 9 20"/>
    <path d="M430 150 C370 116 320 156 290 124 c-18 -16 2 -40 22 -24 c10 8 3 24 -9 20"/>
    <circle cx="66" cy="110" r="5" class="dot"/>
    <circle cx="374" cy="110" r="5" class="dot"/>
    <circle cx="108" cy="90" r="3.4" class="dot"/>
    <circle cx="332" cy="90" r="3.4" class="dot"/>
  </g>'''

def build(kind):
    if kind=='adults':
        head='VOLWASSENEN / molenfanaten'; aria='volwassenen'
        font="Playfair+Display:ital,wght@0,600;1,700"
        style=('.ph{fill:#412F26;font-family:"Playfair Display",Georgia,serif;}'
               '.ph1{font-size:21px;font-weight:600;}'
               '.ph2{font-size:27px;font-weight:700;font-style:italic;}')
        ph2y=97; wind=WIND_ADULT
        windcss='.wind{fill:none;stroke:#5E7E54;stroke-width:2;stroke-linecap:round;}'
    else:
        head='KIDS'; aria='kinderen'
        font="Fredoka:wght@600;700"
        style=('.ph{font-family:"Fredoka","Trebuchet MS",sans-serif;}'
               '.ph1{fill:#412F26;font-size:20px;font-weight:600;}'
               '.ph2{fill:#7B9B6F;font-size:26px;font-weight:700;}')
        ph2y=98; wind=WIND_KIDS
        windcss=('.wind{fill:none;stroke:#7B9B6F;stroke-width:4;stroke-linecap:round;stroke-linejoin:round;}'
                 '.wind .dot{fill:#7B9B6F;stroke:none;}')
    svg=f'''<?xml version="1.0" encoding="UTF-8"?>
<!--
  De Kerkhovense Molen - "Wind kunnen we pakken" - {head}
  Officiele molen uit het logo, gevectoriseerd (drukklaar, schaalbaar). Brandkleuren.
  NB drukker: zet tekst om naar outlines.
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 660" width="440" height="660" role="img" aria-label="De Kerkhovense Molen vangt de wind - {aria}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family={font}&amp;display=swap');
      {style}
      .wm{{fill:#412F26;font-family:"Helvetica Neue",Arial,sans-serif;}}
      .wm1{{font-size:14px;font-weight:700;letter-spacing:1.6px;}}
      .wm2{{font-size:8.4px;letter-spacing:.8px;opacity:.85;}}
      {windcss}
    </style>
{MILL}
  </defs>
  <text x="220" y="56" text-anchor="middle" class="ph ph1">Brood en lucht kun je bakken</text>
  <text x="220" y="{ph2y}" text-anchor="middle" class="ph ph2">Wind kunnen we pakken!</text>

  <g style="color:#412F26"><use href="#mill-logo" transform="{MT}"/></g>

{wind}

  <text x="220" y="624" text-anchor="middle" class="wm wm1">{WM1}</text>
  <text x="220" y="642" text-anchor="middle" class="wm wm2">{WM2}</text>
</svg>'''
    open(os.path.join(PROJ,f'art-{kind}.svg'),'w').write(svg)
    print(f'art-{kind}.svg', len(svg),'bytes')

if __name__=='__main__':
    build('adults'); build('kids')
    print('done. now run tools/outline.py to refresh *-print.svg')
