import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tr_kit import *

SLUG = "why-metal-gates-rust-singapore"

# ---------- Cover: steel swing gate in the rain, rust starting at the bottom rail ----------
bars = ""
for x in range(238, 600, 48):
    bars += f'<line x1="{x}" y1="196" x2="{x}" y2="410" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>'
    bars += f'<line x1="{x}" y1="196" x2="{x}" y2="410" stroke="{LSTEEL}" stroke-width="4" stroke-linecap="round"/>'
rain = ""
for (x, y) in [(150, 70), (230, 104), (310, 62), (390, 98), (470, 58), (550, 96), (630, 66), (700, 108), (90, 96), (740, 150)]:
    rain += f'<path d="M{x} {y} q-9 16 0 22 q9 -6 0 -22 Z" fill="{PALE}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
rust = ""
for (cx, cy, r) in [(258, 420, 8), (300, 425, 6), (420, 418, 9), (470, 424, 6), (560, 420, 7)]:
    rust += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{RED}" stroke="{INK}" stroke-width="3"/>'
drips = ""
for (x, y) in [(300, 436), (470, 436)]:
    drips += f'<path d="M{x} {y} q-6 11 0 15 q6 -4 0 -15 Z" fill="{RED}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
cover_svg = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
{rain}
<rect x="120" y="150" width="46" height="326" rx="4" fill="{STEEL}" {S}/>
<rect x="112" y="136" width="62" height="20" rx="4" fill="{LSTEEL}" {S}/>
<rect x="634" y="150" width="46" height="326" rx="4" fill="{STEEL}" {S}/>
<rect x="626" y="136" width="62" height="20" rx="4" fill="{LSTEEL}" {S}/>
<rect x="190" y="180" width="430" height="250" rx="6" fill="none" stroke="{INK}" stroke-width="30" stroke-linejoin="round"/>
<rect x="190" y="180" width="430" height="250" rx="6" fill="none" stroke="{LSTEEL}" stroke-width="14" stroke-linejoin="round"/>
{bars}
<rect x="182" y="404" width="446" height="34" rx="6" fill="{LSTEEL}" {S}/>
{rust}
{drips}
<rect x="160" y="218" width="34" height="22" rx="4" fill="{STEEL}" stroke="{INK}" stroke-width="7"/>
<rect x="160" y="362" width="34" height="22" rx="4" fill="{STEEL}" stroke="{INK}" stroke-width="7"/>
<rect x="590" y="284" width="30" height="44" rx="5" fill="{STEEL}" stroke="{INK}" stroke-width="7"/>
<line x1="70" y1="476" x2="730" y2="476" {S}/>
</svg>'''

# ---------- Infographic 1 (early): where rust starts on a gate ----------
gbars = "".join(f'<line x1="{x}" y1="86" x2="{x}" y2="224" stroke="{INK}" stroke-width="5"/>' for x in range(112, 290, 26))
gate_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="34" y="50" width="22" height="210" fill="{STEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="314" y="50" width="22" height="210" fill="{STEEL}" stroke="{INK}" stroke-width="3"/>
<line x1="20" y1="262" x2="352" y2="262" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<rect x="72" y="72" width="226" height="164" fill="none" stroke="{INK}" stroke-width="12"/>
<rect x="72" y="72" width="226" height="164" fill="none" stroke="{LSTEEL}" stroke-width="5"/>
{gbars}
<rect x="66" y="222" width="238" height="20" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<circle cx="120" cy="232" r="4" fill="{RED}"/><circle cx="200" cy="234" r="3" fill="{RED}"/><circle cx="262" cy="231" r="4" fill="{RED}"/>
<path d="M150 252 q20 -6 40 0 q20 6 40 0" fill="none" stroke="{STEEL}" stroke-width="3" stroke-linecap="round"/>
<rect x="52" y="96" width="22" height="14" fill="{STEEL}" stroke="{INK}" stroke-width="2.5"/>
<rect x="52" y="196" width="22" height="14" fill="{STEEL}" stroke="{INK}" stroke-width="2.5"/>
<rect x="284" y="140" width="16" height="26" fill="{STEEL}" stroke="{INK}" stroke-width="2.5"/>
<circle cx="292" cy="158" r="3" fill="#fff" stroke="{INK}" stroke-width="1.5"/>
<circle cx="138" cy="84" r="9" fill="none" stroke="{RED}" stroke-width="2.5" stroke-dasharray="3 3"/>
<rect x="234" y="40" width="64" height="24" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
<rect x="241" y="46" width="50" height="12" fill="rgba(215,38,30,0.15)" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 2"/>
<line x1="266" y1="64" x2="262" y2="74" stroke="{INK}" stroke-width="1.5"/>
<text x="266" y="34" font-size="9.5" font-weight="700" fill="#4A4E55" text-anchor="middle">inside the tube</text>
<line x1="216" y1="140" x2="228" y2="152" stroke="{INK}" stroke-width="2"/><line x1="228" y1="140" x2="216" y2="152" stroke="{INK}" stroke-width="2"/>
{num_marker(186, 278, 1)}{num_marker(30, 103, 2)}{num_marker(138, 60, 3)}{num_marker(272, 153, 4)}{num_marker(214, 52, 5)}{num_marker(222, 170, 6)}
</svg>'''
spots = [
    ("Bottom rail and gate foot", "rain collects; splashback, soil and plants keep it wet"),
    ("Hinges, pivots and wheels", "movement wears the coating off and dirt holds water"),
    ("Welds and joints", "harder to coat evenly; gaps between parts trap water"),
    ("Cut edges and drilled holes", "locks and latches fitted after painting leave bare steel"),
    ("Inside hollow sections", "brush or spray paint gives no protection inside tubes"),
    ("Chips and scratches", "once water is under the paint, rust spreads sideways"),
]
info_spots = card("Rust hotspots", "Where rust starts on a metal gate",
    "The six places to check first on a steel gate in Singapore's humid, salty air.",
    f"<div class='split'><div class='fig'>{gate_svg}</div>{numbered(spots)}</div>",
    callout="A small blister in the paint often hides a larger patch: rust undercuts the coating around the point where water got in.",
    src="TR Metalworks guide. Source: American Galvanizers Association, Performance of Hot-Dip Galvanized Steel Products. Simplified diagram, not to scale.")

# ---------- Infographic 2 (mid): gate finishes compared ----------
rows = [
    ("Paint on bare steel", "Barrier only", "Rust starts at the chip and creeps under the paint", "Most frequent: touch up and repaint"),
    ("Powder coat on bare steel", "Barrier only, oven-cured in a coating shop", "Rust starts at the chip and spreads under the coating", "Touch up chips promptly"),
    ("Hot-dip galvanised only", "Zinc barrier plus sacrificial protection", "The surrounding zinc protects small exposed areas", "Low, but the finish is plain grey"),
    ("Galvanised + powder coat (duplex)", "Colour coat over zinc", "No rust creep under the coating", "Lowest; touch up the colour for looks"),
]
g = "<div class='grid' style='grid-template-columns: 1.2fr 1.15fr 1.45fr 1.2fr'>"
g += "<div class='h' style='background:#3A3E44'>Finish</div><div class='h'>How it protects</div><div class='h'>When it is chipped</div><div class='h'>Upkeep</div>"
for i, (a, b, c, d) in enumerate(rows):
    alt = " row-alt" if i % 2 else ""
    hl = " style='color:#C1211A'" if i == 3 else ""
    g += f"<div class='l{alt}'{hl}>{a}</div><div class='c{alt}'>{b}</div><div class='c{alt}'>{c}</div><div class='c{alt}'>{d}</div>"
g += "</div>"
info_finishes = card("Gate finishes", "Which finish stops a steel gate rusting?",
    "Paint and powder coat are barriers. Zinc from hot-dip galvanising also protects the steel where the coating is damaged.", g,
    callout="American Galvanizers Association: a duplex system protects steel for 1.5 to 2.3 times the sum of the lives of the zinc and the paint used alone. Tell the galvaniser the steel will be coated afterwards.",
    src="TR Metalworks guide. Sources: American Galvanizers Association, Painting over Hot-Dip Galvanized Steel (Duplex Systems) and Performance of Hot-Dip Galvanized Steel Products.")

out = save_and_render({
    "cover-metal-gate-rust-singapore": cover(cover_svg),
    "metal-gate-rust-hotspots-singapore": info_spots,
    "gate-finishes-compared-rust-singapore": info_finishes,
}, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "posts", SLUG))
print(out)
