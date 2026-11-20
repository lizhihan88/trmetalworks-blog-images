import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tr_kit import *

# ---------- Cover: laser head cutting a sheet ----------
sparks = ""
for (x1, y1, x2, y2) in [(452, 360, 430, 348), (450, 374, 424, 378), (458, 352, 450, 334), (488, 350, 496, 333)]:
    sparks += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
cover_svg = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<line x1="80" y1="470" x2="720" y2="470" {S}/>
<path d="M100 410 L700 410 L700 432 L100 432 Z" fill="{STEEL}" {S}/>
<path d="M160 320 L640 320 L700 410 L100 410 Z" fill="{LSTEEL}" {S}/>
<ellipse cx="250" cy="372" rx="46" ry="19" fill="#fff" stroke="{INK}" stroke-width="7"/>
<ellipse cx="322" cy="346" rx="10" ry="5" fill="#fff" stroke="{INK}" stroke-width="5"/>
<ellipse cx="356" cy="346" rx="10" ry="5" fill="#fff" stroke="{INK}" stroke-width="5"/>
<ellipse cx="390" cy="346" rx="10" ry="5" fill="#fff" stroke="{INK}" stroke-width="5"/>
<path d="M566 340 L618 340 L630 362 L578 362 Z" fill="#fff" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
<ellipse cx="524" cy="372" rx="50" ry="21" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="10 9"/>
<rect x="110" y="88" width="580" height="40" rx="8" fill="{STEEL}" {S}/>
<rect x="424" y="122" width="102" height="62" rx="8" fill="{LSTEEL}" {S}/>
<path d="M440 184 L510 184 L492 262 L458 262 Z" fill="{STEEL}" {S}/>
<path d="M462 262 L488 262 L482 284 L468 284 Z" fill="{INK}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
<line x1="475" y1="290" x2="475" y2="362" stroke="{RED}" stroke-width="9" stroke-linecap="round"/>
{sparks}
<circle cx="475" cy="370" r="11" fill="{RED}" stroke="{INK}" stroke-width="5"/>
</svg>'''

# ---------- Infographic 1: four parts of a quote ----------
def icon(kind):
    if kind == "time":
        inner = f'<circle cx="28" cy="30" r="19" fill="{PALE}" stroke="{INK}" stroke-width="4"/><line x1="28" y1="30" x2="28" y2="19" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><line x1="28" y1="30" x2="36" y2="34" stroke="{RED}" stroke-width="4" stroke-linecap="round"/><rect x="23" y="5" width="10" height="5" rx="2" fill="{INK}"/>'
    elif kind == "sheet":
        inner = f'<rect x="7" y="10" width="42" height="36" rx="3" fill="{LSTEEL}" stroke="{INK}" stroke-width="4"/><circle cx="20" cy="22" r="6" fill="#fff" stroke="{INK}" stroke-width="3"/><rect x="30" y="26" width="13" height="12" rx="2" fill="#fff" stroke="{RED}" stroke-width="3"/>'
    elif kind == "setup":
        inner = f'<rect x="8" y="8" width="40" height="40" rx="5" fill="{PALE}" stroke="{INK}" stroke-width="4"/><line x1="16" y1="20" x2="40" y2="20" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><line x1="16" y1="29" x2="34" y2="29" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><line x1="16" y1="38" x2="28" y2="38" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>'
    else:
        inner = f'<path d="M9 46 L9 12 L19 12 L19 36 L47 36 L47 46 Z" fill="{LSTEEL}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><circle cx="14" cy="22" r="3" fill="#fff" stroke="{INK}" stroke-width="2"/><circle cx="37" cy="41" r="3" fill="#fff" stroke="{INK}" stroke-width="2"/><line x1="9" y1="36" x2="19" y2="36" stroke="{RED}" stroke-width="3" stroke-dasharray="3 2"/>'
    return f'<svg viewBox="0 0 56 56" width="46" height="46" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

parts = [
    ("time", "1. Machine time", "Cut length plus every pierce, at the machine's hourly rate.", "Thick plate, many small holes, sharp corners", "Thin sheet, fewer openings, smooth curves"),
    ("sheet", "2. Material", "Grade, thickness and the share of the sheet your parts use, offcut included.", "Stainless steel or aluminium, awkward shapes", "Mild steel, parts that nest tightly"),
    ("setup", "3. Setup and programming", "Checking the file, nesting the parts and loading the machine.", "One-off pieces, messy or hand-drawn files", "Identical parts batched, a clean DXF"),
    ("bend", "4. Work after cutting", "Deburring, bending, rolling, welding and finishes such as powder coat.", "Several processes across different vendors", "Parts used as cut, or one workshop for all"),
]
panels = "<div class='panels'>"
for k, t, d, up, down in parts:
    panels += (f"<div class='panel'><div style='display:flex;gap:12px;align-items:center'>{icon(k)}<h3>{t}</h3></div>"
               f"<p>{d}</p>"
               f"<div style='margin-top:9px;font-size:11px;line-height:1.4'><b style='color:#C1211A'>Goes up with:</b> {up}</div>"
               f"<div style='margin-top:4px;font-size:11px;line-height:1.4'><b style='color:#1C1D20'>Comes down with:</b> {down}</div></div>")
panels += "</div>"
info_parts = card("Laser cutting price", "What goes into a laser cutting quote",
    "Most laser cutting prices in Singapore add up the same four parts. Here is what moves each one.", panels,
    callout="Material can weigh as much as cutting time: in one survey cited by The Fabricator, material sales made up 56% of laser job shop revenue.",
    src="TR Metalworks guide. Source: The Fabricator, Accurate quotes maximise a fabrication shop's profits on laser cutting jobs (2023).")

# ---------- Infographic 2: where the machine time goes ----------
holes = ""
for (cx, cy) in [(92, 118), (92, 196), (196, 118), (196, 196)]:
    holes += f'<circle cx="{cx}" cy="{cy}" r="11" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="{cx}" cy="{cy}" r="3" fill="{RED}"/>'
sheet_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="20" y="40" width="340" height="230" rx="4" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<path d="M60 82 L228 82 L228 160 L180 160 L180 232 L60 232 Z" fill="#fff" stroke="{INK}" stroke-width="4" stroke-linejoin="miter"/>
{holes}
<circle cx="294" cy="150" r="46" fill="#fff" stroke="{INK}" stroke-width="4"/>
<circle cx="294" cy="150" r="13" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="294" cy="150" r="3" fill="{RED}"/>
<rect x="228" y="160" width="0" height="0"/>
<text x="198" y="28" font-size="10.5" font-weight="700" fill="#6B7078" text-anchor="middle">one sheet, seen from above</text>
{num_marker(140, 82, 1)}{num_marker(92, 157, 2)}{num_marker(228, 160, 3)}{num_marker(294, 104, 4)}{num_marker(300, 236, 5)}
</svg>'''
items = [
    ("Outline length", "the laser traces every edge; longer, more detailed outlines take longer"),
    ("One pierce per hole", "every hole or slot starts by burning through the sheet; thick plate pierces more slowly"),
    ("Sharp corners", "the head slows to turn, so square corners cost time"),
    ("Smooth curves", "a circle cuts faster than a square with the same cut length"),
    ("The skeleton", "the sheet left around and between parts is still material you pay for"),
]
info_time = card("Machine time", "Where the laser's time goes",
    "What the cutting software counts when it times a job, shown on a simplified sheet with two parts.",
    f"<div class='split'><div class='fig'>{sheet_svg}</div>{numbered(items)}</div>",
    callout="A screen with 400 small holes needs 400 pierces. Fewer, larger openings save machine time and money.",
    src="Sources: The Fabricator (2023) on cut time and corners; TWI on laser cutting. Simplified diagram, not to scale.")

out = save_and_render({
    "cover-laser-cutting-cost-singapore": cover(cover_svg),
    "laser-cutting-price-four-parts-singapore": info_parts,
    "laser-cutting-machine-time-pierces-diagram": info_time,
}, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "posts", "laser-cutting-cost-singapore"))
print(out)
