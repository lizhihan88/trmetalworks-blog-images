import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tr_kit import *

# Cover: staircase with balustrade and red handrail
steps = "M130 470 L130 424 L210 424 L210 378 L290 378 L290 332 L370 332 L370 286 L450 286 L450 240 L530 240 L530 194 L680 194 L680 470 Z"
def hy(x):
    return 330 - 0.6 * (x - 150)
bal = ""
for i in range(5):
    for dx in (20, 60):
        x = 130 + i * 80 + dx
        base = 424 - i * 46
        bal += f'<line x1="{x}" y1="{base}" x2="{x}" y2="{hy(x):.0f}" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
for x in (575, 615, 655):
    bal += f'<line x1="{x}" y1="194" x2="{x}" y2="102" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
cover_svg = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<path d="{steps}" fill="{LSTEEL}" {S}/>
{bal}
<line x1="140" y1="424" x2="140" y2="{hy(140):.0f}" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
<line x1="680" y1="194" x2="680" y2="96" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
<path d="M140 {hy(140):.0f} L530 102 L680 102" fill="none" stroke="{INK}" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M140 {hy(140):.0f} L530 102 L680 102" fill="none" stroke="{RED}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="100" y1="470" x2="710" y2="470" {S}/>
</svg>'''

# Infographic A: BCA barrier rules, side elevation
bars = "".join(f'<line x1="{x}" y1="236" x2="{x}" y2="96" stroke="{INK}" stroke-width="4"/>' for x in range(96, 276, 22))
barrier_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="20" y="248" width="270" height="22" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<line x1="290" y1="270" x2="290" y2="296" stroke="{STEEL}" stroke-width="2" stroke-dasharray="4 4"/>
<text x="300" y="290" font-size="10" font-weight="700" fill="#6B7078">drop</text>
<rect x="82" y="236" width="196" height="12" fill="{RED}" stroke="{INK}" stroke-width="2.5"/>
{bars}
<line x1="82" y1="248" x2="82" y2="88" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<line x1="278" y1="248" x2="278" y2="88" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<line x1="76" y1="90" x2="284" y2="90" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="151" cy="160" r="15" fill="rgba(215,38,30,0.12)" stroke="{RED}" stroke-width="2.5" stroke-dasharray="4 3"/>
<line x1="48" y1="248" x2="48" y2="90" stroke="{STEEL}" stroke-width="2"/><line x1="42" y1="90" x2="54" y2="90" stroke="{STEEL}" stroke-width="2"/><line x1="42" y1="248" x2="54" y2="248" stroke="{STEEL}" stroke-width="2"/>
<text x="40" y="174" font-size="11" font-weight="800" fill="#2B2E33" text-anchor="middle" transform="rotate(-90 40 174)">≥ 1.0 m</text>
<line x1="82" y1="222" x2="278" y2="222" stroke="{STEEL}" stroke-width="6"/>
<line x1="306" y1="222" x2="306" y2="90" stroke="{STEEL}" stroke-width="2"/><line x1="300" y1="90" x2="312" y2="90" stroke="{STEEL}" stroke-width="2"/><line x1="300" y1="222" x2="312" y2="222" stroke="{STEEL}" stroke-width="2"/>
<text x="322" y="160" font-size="10.5" font-weight="800" fill="#2B2E33" text-anchor="middle" transform="rotate(-90 322 160)">≥ 850 mm</text>
<text x="350" y="226" font-size="9.5" font-weight="700" fill="#4A4E55" text-anchor="middle">toehold</text>
{num_marker(180, 70, 1)}{num_marker(151, 192, 2)}{num_marker(236, 262, 3)}{num_marker(350, 200, 4)}
</svg>'''
rules = [
    ("At least 1.0 m high", "from the finished floor, or from the pitch line on stairs, where the drop is 1.0 m or more"),
    ("No gap a 100 mm sphere can pass", "150 mm in industrial buildings; on stairs, the tread-riser triangle must not pass 150 mm"),
    ("Bottom 75 mm closed", "no gap at all at the foot of the barrier"),
    ("Nothing to climb", "the top must be at least 850 mm above the last climbable toehold, such as a low horizontal rail or kerb"),
    ("Glass must be laminated", "to SS 341; glass panel barriers follow BS 6180 Section 8"),
]
info_rules = card("Railing safety rules", "BCA's safety barrier rules at a glance",
    "What a staircase or balcony railing must do in Singapore, from Clause H of BCA's Approved Document.",
    f"<div class='split'><div class='fig'>{barrier_svg}</div>{numbered(rules)}</div>",
    callout="Landed houses built for the owner's own use are exempt from the height, gap and climbing rules, but not from the laminated glass rule. Confirm your project with your QP or architect.",
    src="Source: BCA, Understanding the Approved Document v3.0, Clause H, Safety from Falling. Simplified diagram, not to scale.")

# Infographic B: railing materials compared
rows = [
    ("304 stainless steel", "Indoor staircases and sheltered balconies", "Wipe down; no coating to maintain", "Less resistant than 316 to salt outdoors"),
    ("316 stainless steel", "Exposed balconies, pool decks, homes near the sea", "Wipe down; no coating to maintain", "Usually costs more than 304"),
    ("Mild steel, galvanised + powder coated", "Outdoor railings in any colour, or to match a gate", "Touch up chips before rust starts", "Painted-only steel needs repainting more often"),
    ("Aluminium, powder coated", "Lighter railings where weight matters", "Low; aluminium doesn't rust red", "Agree post sizes and fixings early"),
    ("Laminated glass + metal", "Open views on balconies and modern stairs", "Clean the glass; check fixings", "Must be laminated glass to SS 341"),
]
g = "<div class='grid' style='grid-template-columns: 1.15fr 1.35fr 1.1fr 1.2fr'>"
g += "<div class='h' style='background:#3A3E44'>Railing option</div><div class='h'>Usually suits</div><div class='h'>Upkeep</div><div class='h'>Watch out for</div>"
for i, (a, b, c, d) in enumerate(rows):
    alt = " row-alt" if i % 2 else ""
    g += f"<div class='l{alt}'>{a}</div><div class='c{alt}'>{b}</div><div class='c{alt}'>{c}</div><div class='c{alt}'>{d}</div>"
g += "</div>"
info_materials = card("Railing materials", "Which railing material goes where?",
    "How the common staircase and balcony railing options compare in Singapore's rain, sun and sea air.", g,
    callout="Powder coat over hot-dip galvanising (a duplex system) protects outdoor mild steel railings better than either coating alone.",
    src="TR Metalworks guide. Sources: BCA Approved Document (glass); ASSDA on grade 316; American Galvanizers Association on duplex systems.")

out = save_and_render({
    "cover-staircase-balcony-railing-singapore": cover(cover_svg),
    "bca-safety-barrier-rules-railing-singapore": info_rules,
    "railing-materials-compared-singapore": info_materials,
}, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "posts", "staircase-balcony-railing-fabrication-singapore"))
print(out)
