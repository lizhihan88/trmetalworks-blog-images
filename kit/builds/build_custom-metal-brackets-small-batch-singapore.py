import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tr_kit import *

SLUG = "custom-metal-brackets-small-batch-singapore"

# ---------- Cover: L-bracket with red bolts, a slotted flat plate and a small Z clip ----------
def hexagon(cx, cy, r):
    import math
    pts = " ".join(f"{cx + r * math.cos(math.radians(30 + 60 * k)):.1f},{cy + r * math.sin(math.radians(30 + 60 * k)):.1f}" for k in range(6))
    return f'<polygon points="{pts}" fill="{RED}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'

cover_svg = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<!-- base flange (horizontal, receding to the lower left) -->
<path d="M290 372 L500 372 L410 462 L200 462 Z" fill="{STEEL}" {S}/>
<path d="M200 462 L410 462 L410 478 L200 478 Z" fill="{LSTEEL}" {S}/>
<path d="M410 462 L500 372 L500 388 L410 478 Z" fill="{LSTEEL}" {S}/>
<ellipse cx="292" cy="428" rx="20" ry="11" fill="#fff" stroke="{INK}" stroke-width="7"/>
<ellipse cx="402" cy="428" rx="20" ry="11" fill="#fff" stroke="{INK}" stroke-width="7"/>
<!-- upright flange -->
<rect x="290" y="96" width="210" height="276" fill="{LSTEEL}" {S}/>
<path d="M500 96 L516 96 L516 372 L500 388 Z" fill="{STEEL}" {S}/>
{hexagon(345, 170, 24)}{hexagon(445, 170, 24)}
<circle cx="345" cy="170" r="8" fill="{INK}"/><circle cx="445" cy="170" r="8" fill="{INK}"/>
<!-- slotted flat plate, standing -->
<rect x="572" y="356" width="158" height="138" rx="8" fill="{LSTEEL}" {S}/>
<rect x="596" y="386" width="60" height="22" rx="11" fill="#fff" stroke="{INK}" stroke-width="7"/>
<rect x="596" y="428" width="60" height="22" rx="11" fill="#fff" stroke="{INK}" stroke-width="7"/>
<circle cx="694" cy="418" r="15" fill="#fff" stroke="{INK}" stroke-width="7"/>
<!-- small Z clip -->
<path d="M70 478 L126 478 L126 422 L200 422 L200 438 L142 438 L142 494 L70 494 Z" fill="{STEEL}" {S}/>
<line x1="50" y1="494" x2="750" y2="494" {S}/>
</svg>'''

# ---------- Infographic 1 (early): bracket materials and finishes ----------
rows = [
    ("Mild steel, hot-dip galvanised", "Outdoor and hidden brackets, base plates and supports", "Plain grey finish; cut and drill before galvanising where possible"),
    ("Mild steel, powder coated", "Indoor visible brackets in a colour, shelving and display parts", "Outdoors without zinc underneath, rust starts at chips"),
    ("Mild steel, galvanised + powder coated", "Outdoor brackets that must match a colour scheme", "Tell the coating shop the steel is galvanised"),
    ("304 stainless steel", "Kitchens, wet areas and indoor fixtures", "Can stain in salty outdoor air"),
    ("316 stainless steel", "Outdoor brackets near the sea, pool areas and exposed façades", "Usually costs more than 304"),
    ("Aluminium", "Light-duty brackets, signage and display parts where weight matters", "Stiffer alloys such as 6061 need a larger bend radius and can crack if bent tightly"),
]
g = "<div class='grid' style='grid-template-columns: 1.25fr 1.6fr 1.6fr'>"
g += "<div class='h' style='background:#3A3E44'>Material and finish</div><div class='h'>Usually suits</div><div class='h'>Watch out for</div>"
for i, (a, b, c) in enumerate(rows):
    alt = " row-alt" if i % 2 else ""
    g += f"<div class='l{alt}'>{a}</div><div class='c{alt}'>{b}</div><div class='c{alt}'>{c}</div>"
g += "</div>"
info_materials = card("Bracket materials", "Which material and finish suit your bracket?",
    "Choose the material for where the bracket will live, then the finish for how it must look and last.", g,
    callout="Outdoor air-con units: BCA requires them to sit on a stainless steel bracket or a concrete ledge or casing designed to hold the unit.",
    src="TR Metalworks guide. Sources: BCA, Air-conditioning Unit Structural Supporting System; The Fabricator, Design tips for sheet metal; American Galvanizers Association.")

# ---------- Infographic 2 (mid): design rules for a bendable bracket ----------
grain = ""
diag_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="20" y="22" font-size="10" font-weight="800" fill="#6B7078">SIDE VIEW</text>
<path d="M60 34 L60 112 A22 22 0 0 0 82 134 L250 134 L250 122 L82 122 A10 10 0 0 1 72 112 L72 34 Z" fill="{LSTEEL}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
<line x1="150" y1="122" x2="150" y2="134" stroke="{INK}" stroke-width="1.5" stroke-dasharray="2 2"/>
<line x1="170" y1="122" x2="170" y2="134" stroke="{INK}" stroke-width="1.5" stroke-dasharray="2 2"/>
<rect x="150" y="121" width="20" height="14" fill="rgba(255,255,255,0.7)"/>
<line x1="82" y1="150" x2="150" y2="150" stroke="{RED}" stroke-width="2"/>
<line x1="82" y1="144" x2="82" y2="156" stroke="{RED}" stroke-width="2"/><line x1="150" y1="144" x2="150" y2="156" stroke="{RED}" stroke-width="2"/>
<text x="116" y="166" font-size="10.5" font-weight="800" fill="#C1211A" text-anchor="middle">≥ 2t</text>
<line x1="60" y1="102" x2="250" y2="102" stroke="{STEEL}" stroke-width="1.5"/>
<line x1="250" y1="96" x2="250" y2="108" stroke="{STEEL}" stroke-width="1.5"/>
<text x="196" y="96" font-size="10.5" font-weight="800" fill="#2B2E33" text-anchor="middle">flange ≥ 4t</text>
<line x1="40" y1="44" x2="60" y2="44" stroke="{STEEL}" stroke-width="1.5"/><line x1="72" y1="44" x2="92" y2="44" stroke="{STEEL}" stroke-width="1.5"/>
<text x="100" y="48" font-size="10.5" font-weight="800" fill="#2B2E33">t</text>
<text x="96" y="118" font-size="10" font-weight="800" fill="#2B2E33">r</text>
<text x="20" y="196" font-size="10" font-weight="800" fill="#6B7078">FLAT BLANK</text>
<path d="M40 208 L144 208 L144 218 A6 6 0 0 0 156 218 L156 208 L340 208 L340 284 L156 284 L156 274 A6 6 0 0 0 144 274 L144 284 L40 284 Z" fill="{LSTEEL}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
<line x1="150" y1="226" x2="150" y2="266" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4"/>
<circle cx="96" cy="232" r="8" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
<circle cx="96" cy="262" r="8" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
<rect x="232" y="226" width="44" height="14" rx="7" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
<rect x="232" y="254" width="44" height="14" rx="7" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
<text x="166" y="250" font-size="9.5" font-weight="700" fill="#4A4E55">bend line</text>
{num_marker(42, 138, 1)}{num_marker(116, 182, 2)}{num_marker(286, 92, 3)}{num_marker(150, 196, 4)}{num_marker(300, 247, 5)}
</svg>'''
rules = [
    ("Inside radius r at least the thickness t", "in air bending, commonly one to two times the thickness"),
    ("Holes at least 2t from the bend", "measured from the hole's edge to the start of the bend radius"),
    ("Flanges at least 4t long", "shorter flanges tend to be marked by the tooling"),
    ("Bend relief at least t + r", "where a bend meets an edge; rounded ends stop tearing"),
    ("Slots where it must adjust", "so the bracket can be lined up on site"),
]
info_rules = card("Design rules", "Five rules for a bracket that bends cleanly",
    "Rules of thumb for bending mild steel sheet. Your fabricator will confirm them for your material and thickness.",
    f"<div class='split'><div class='fig'>{diag_svg}</div>{numbered(rules)}</div>",
    callout="Put a general tolerance in the title block, such as ISO 2768-m (±0.3 mm over 30 up to 120 mm), and tighten only the dimensions that matter.",
    src="Sources: The Fabricator, Design tips for sheet metal; ISO 2768-1. Simplified diagram, not to scale.")

out = save_and_render({
    "cover-custom-metal-brackets-singapore": cover(cover_svg),
    "bracket-materials-finishes-compared-singapore": info_materials,
    "bracket-bending-design-rules-singapore": info_rules,
}, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "posts", SLUG))
print(out)
