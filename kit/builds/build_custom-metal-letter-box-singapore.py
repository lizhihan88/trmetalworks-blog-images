import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tr_kit import *

# ---------- Cover: letter box in a gate pillar, beside a metal gate ----------
bars = "".join(f'<line x1="{x}" y1="222" x2="{x}" y2="440" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>' for x in range(420, 660, 30))
cover_svg = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<line x1="90" y1="470" x2="720" y2="470" {S}/>
<rect x="660" y="160" width="40" height="310" rx="5" fill="{LSTEEL}" {S}/>
{bars}
<rect x="396" y="212" width="266" height="236" rx="4" fill="none" {S}/>
<rect x="150" y="150" width="236" height="320" rx="6" fill="{PALE}" {S}/>
<rect x="134" y="116" width="268" height="42" rx="6" fill="{STEEL}" {S}/>
<g transform="rotate(-8 268 196)">
<rect x="238" y="172" width="62" height="44" rx="3" fill="#fff" stroke="{INK}" stroke-width="7"/>
<path d="M240 175 L269 197 L298 175" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
</g>
<rect x="196" y="204" width="144" height="190" rx="8" fill="{LSTEEL}" {S}/>
<rect x="216" y="222" width="104" height="26" rx="6" fill="{RED}" stroke="{INK}" stroke-width="7"/>
<rect x="212" y="266" width="112" height="112" rx="5" fill="none" stroke="{INK}" stroke-width="6"/>
<rect x="226" y="282" width="52" height="26" rx="4" fill="#fff" stroke="{INK}" stroke-width="5"/>
<line x1="238" y1="295" x2="250" y2="295" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<line x1="256" y1="295" x2="266" y2="295" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<circle cx="302" cy="326" r="10" fill="#fff" stroke="{INK}" stroke-width="6"/>
<line x1="302" y1="324" x2="302" y2="332" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</svg>'''

# ---------- Infographic 1: SingPost letter box requirements (diagram) ----------
dim = f'stroke="{STEEL}" stroke-width="2"'
envs = "".join(f'<rect x="{258+i*3}" y="{170-i*9}" width="40" height="7" rx="1" fill="#fff" stroke="{INK}" stroke-width="1.5"/>' for i in range(3))
spec_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="4" y1="282" x2="376" y2="282" stroke="{INK}" stroke-width="3"/>
<rect x="28" y="40" width="146" height="242" fill="{PALE}" stroke="{INK}" stroke-width="3"/>
<rect x="50" y="70" width="102" height="132" rx="3" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="64" y="78" width="74" height="13" rx="2" fill="{RED}" stroke="{INK}" stroke-width="2"/>
<rect x="60" y="100" width="82" height="92" rx="2" fill="none" stroke="{INK}" stroke-width="2"/>
<rect x="68" y="108" width="34" height="15" rx="2" fill="#fff" stroke="{INK}" stroke-width="1.5"/>
<text x="85" y="119" font-size="10" font-weight="800" fill="{INK}" text-anchor="middle">12</text>
<circle cx="130" cy="150" r="4.5" fill="#fff" stroke="{INK}" stroke-width="2"/>
<line x1="14" y1="282" x2="14" y2="78" {dim}/><line x1="8" y1="78" x2="20" y2="78" {dim}/>
<text x="24" y="166" font-size="10" font-weight="800" fill="#2B2E33" text-anchor="middle" transform="rotate(-90 24 166)">≤ 1,650 mm</text>
<line x1="50" y1="214" x2="152" y2="214" {dim}/><line x1="50" y1="208" x2="50" y2="220" {dim}/><line x1="152" y1="208" x2="152" y2="220" {dim}/>
<text x="101" y="230" font-size="10" font-weight="800" fill="#2B2E33" text-anchor="middle">≥ 270 mm wide</text>
<line x1="164" y1="70" x2="164" y2="202" {dim}/><line x1="158" y1="70" x2="170" y2="70" {dim}/><line x1="158" y1="202" x2="170" y2="202" {dim}/>
<text x="186" y="136" font-size="10" font-weight="800" fill="#2B2E33" text-anchor="middle" transform="rotate(-90 186 136)">≥ 380 mm high</text>
<text x="290" y="56" font-size="10" font-weight="700" fill="#6B7078" text-anchor="middle">side section</text>
<rect x="262" y="70" width="58" height="132" fill="#fff" stroke="none"/>
<line x1="262" y1="70" x2="320" y2="70" stroke="{INK}" stroke-width="3"/>
<line x1="320" y1="70" x2="320" y2="202" stroke="{INK}" stroke-width="3"/>
<line x1="262" y1="202" x2="320" y2="202" stroke="{INK}" stroke-width="3"/>
<line x1="262" y1="70" x2="262" y2="86" stroke="{INK}" stroke-width="3"/>
<line x1="262" y1="98" x2="262" y2="202" stroke="{INK}" stroke-width="3"/>
<line x1="262" y1="98" x2="290" y2="98" stroke="{INK}" stroke-width="3"/>
<line x1="262" y1="78" x2="250" y2="96" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>
{envs}
<line x1="262" y1="214" x2="320" y2="214" {dim}/><line x1="262" y1="208" x2="262" y2="220" {dim}/><line x1="320" y1="208" x2="320" y2="220" {dim}/>
<text x="291" y="230" font-size="10" font-weight="800" fill="#2B2E33" text-anchor="middle">≥ 150 mm deep</text>
<text x="300" y="112" font-size="9" font-weight="700" fill="#4A4E55" text-anchor="middle">ledge</text>
{num_marker(346, 92, 1)}{num_marker(236, 108, 2)}{num_marker(101, 252, 3)}{num_marker(130, 172, 4)}{num_marker(85, 140, 5)}{num_marker(14, 254, 6)}
<line x1="334" y1="92" x2="266" y2="92" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 3"/>
</svg>'''
reqs = [
    ("Slot at least 25 × 230 mm", "near the top of the box, so an A4 envelope goes in unfolded"),
    ("Slot cover", "required, to keep out rain and insects"),
    ("Inside at least 380 × 270 × 150 mm", "height × width × depth for a gate pillar or standalone box; bigger is allowed"),
    ("Lockable door", "every letter box must have one"),
    ("House number", "digits at least 12 mm high in a contrasting colour, inscribed or riveted; no \"#\" sign"),
    ("No higher than 1,650 mm", "from the ground to the top of the slot cover"),
]
info_spec = card("SingPost letter box rules", "Letter box requirements for landed homes",
    "The minimums in the Letter Box Specifications and Guidelines, which SingPost administers for IMDA.",
    f"<div class='split'><div class='fig'>{spec_svg}</div>{numbered(reqs)}</div>",
    callout="Place it at the main gate so the postman can deliver without entering. A ledge of at least 25 mm behind the slot is recommended, so mail can't be pulled back out.",
    src="Source: SingPost, Letter Box Specifications and Guidelines (approved by IDA, 2 Oct 2009), Sections 1.5, 2.1 to 2.10. Simplified diagram, not to scale.")

# ---------- Infographic 2: materials compared ----------
mats = [
    ("Stainless", "Grade 304 or 316", "#3A3E44",
     "A brushed or hairline look that matches stainless gates and railings; no coating to maintain",
     "Choose 316 near the sea or a pool; 304 is less resistant to salty air"),
    ("Aluminium", "Anodised or powder coated", "#7D8790",
     "Lighter boxes, especially on a gate leaf; any colour with powder coat",
     "Softer than steel, so large doors may need thicker sheet or stiffening"),
    ("Mild steel", "Galvanised + powder coated", RED,
     "Custom shapes and colours to match a painted steel gate",
     "Rusts where the coating is chipped; touch up scratches early"),
]
info_mats = card("Letter box materials", "Which metal suits a letter box?",
    "The SingPost guidelines accept any durable material. These three cover most landed homes in Singapore.",
    cards3(mats),
    callout="Match the letter box to the gate's metal and finish, so the two read as one design.",
    src="TR Metalworks guide. Source: SingPost Letter Box Specifications and Guidelines, Section 1.12 (durable materials).")

out = save_and_render({
    "cover-letter-box-singapore": cover(cover_svg),
    "letter-box-size-requirements-singapore": info_spec,
    "letter-box-materials-compared-singapore": info_mats,
}, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "posts", "custom-metal-letter-box-singapore"))
print(out)
