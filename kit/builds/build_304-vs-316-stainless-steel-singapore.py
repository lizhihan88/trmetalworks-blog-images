import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tr_kit import *

SLUG = "304-vs-316-stainless-steel-singapore"

# ---------- Cover: stainless steel railing on a seafront deck ----------
waves = ""
for y, x0 in [(262, 80), (330, 130), (404, 90)]:
    d = f"M{x0} {y}"
    for k in range(9):
        x = x0 + k * 66
        d += f" Q{x + 16} {y - 12} {x + 33} {y} T{x + 66} {y}"
    waves += f'<path d="{d}" fill="none" stroke="{STEEL}" stroke-width="6" stroke-linecap="round"/>'
spray = ""
for (cx, cy, r) in [(96, 158, 7), (124, 128, 5), (72, 118, 4), (708, 150, 6), (736, 122, 4)]:
    spray += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="4"/>'
posts = ""
for x in (170, 340, 510, 680):
    posts += f'<rect x="{x - 11}" y="246" width="22" height="196" rx="4" fill="{LSTEEL}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
    posts += f'<line x1="{x - 3}" y1="262" x2="{x - 3}" y2="428" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    posts += f'<rect x="{x - 26}" y="434" width="52" height="14" rx="3" fill="{STEEL}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
rails = ""
for y in (316, 376):
    rails += f'<line x1="170" y1="{y}" x2="680" y2="{y}" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>'
    rails += f'<line x1="170" y1="{y}" x2="680" y2="{y}" stroke="{LSTEEL}" stroke-width="7" stroke-linecap="round"/>'
cover_svg = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<circle cx="560" cy="200" r="74" fill="{RED}" stroke="{INK}" stroke-width="9"/>
<path d="M60 200 L740 200 L740 448 L60 448 Z" fill="{PALE}" stroke="none"/>
<line x1="60" y1="200" x2="740" y2="200" stroke="{STEEL}" stroke-width="6" stroke-linecap="round"/>
{waves}
{spray}
<path d="M60 448 L740 448 L740 478 L60 478 Z" fill="{STEEL}" {S}/>
{rails}
{posts}
<rect x="140" y="226" width="570" height="30" rx="15" fill="{LSTEEL}" {S}/>
<line x1="164" y1="236" x2="684" y2="236" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
</svg>'''

# ---------- Infographic 1: which grade goes where ----------
cards = [
    ("304", "PRE about 19 · inland level", "#6E7882",
     "Indoor kitchens, sinks and shelving; indoor railings and trims; outdoor items away from the sea that are cleaned regularly",
     "Will probably tea-stain near the sea. Outdoors it needs a smooth finish and regular cleaning, with some staining between cleans"),
    ("316", "PRE about 24.6 · marine level", "#2B2E33",
     "Seafront homes and outlets; outdoor parts rain can't wash, such as under eaves; brine and seafood preparation",
     "Still stains if the finish is rough or salt sits in crevices. Ask for below 0.5 µm Ra and a design that drains"),
    ("2205", "Duplex · ASSDA's next step up", RED,
     "Splash zones, unwashed areas and rough surfaces where no staining is acceptable",
     "For more corrosive sites, IMOA advises a review by a metallurgical engineer"),
]
info_grades = card("304 vs 316", "Which stainless steel grade goes where?",
    "Choosing between 304, 316 and duplex 2205 for Singapore's heat, humidity and sea air.",
    cards3(cards),
    callout="ASSDA: tea staining is most likely within 5 km of a surf beach and 1 km of still sea water, and can reach 20 km or more in hot, windy, sheltered conditions. On a small island, many sites fall inside that zone.",
    src="TR Metalworks guide. Sources: ASSDA, Preventing Coastal Corrosion (Tea Staining); IMOA, Selecting Stainless Steel for Optimum Performance. PRE = %Cr + 3.3×%Mo + 16×%N, from nominal compositions.")

# ---------- Infographic 2: details that stop tea staining ----------
rain = ""
for (x, y) in [(262, 44), (300, 70), (338, 40), (284, 118), (326, 132), (356, 96), (270, 186), (344, 200)]:
    rain += f'<line x1="{x}" y1="{y}" x2="{x - 6}" y2="{y + 18}" stroke="{STEEL}" stroke-width="3" stroke-linecap="round"/>'
grain = "".join(f'<line x1="{x}" y1="142" x2="{x}" y2="226" stroke="{STEEL}" stroke-width="1.6"/>' for x in range(132, 314, 9))
diag_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="34" y="66" width="200" height="186" fill="rgba(215,38,30,0.07)"/>
<text x="134" y="88" font-size="10" font-weight="700" fill="#C1211A" text-anchor="middle">rain shadow</text>
<rect x="14" y="40" width="20" height="212" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<path d="M6 46 L240 30 L240 46 L6 62 Z" fill="{STEEL}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
{rain}
<rect x="10" y="252" width="360" height="16" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="122" y="138" width="200" height="92" fill="#fff" stroke="{INK}" stroke-width="2.5"/>
{grain}
<rect x="112" y="108" width="12" height="144" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="320" y="108" width="12" height="144" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="104" y="244" width="28" height="8" fill="{STEEL}" stroke="{INK}" stroke-width="2.5"/>
<rect x="312" y="244" width="28" height="8" fill="{STEEL}" stroke="{INK}" stroke-width="2.5"/>
<rect x="98" y="100" width="242" height="12" rx="6" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<circle cx="326" cy="113" r="7" fill="none" stroke="{RED}" stroke-width="2.5"/>
{num_marker(118, 176, 1)}{num_marker(222, 186, 2)}{num_marker(352, 128, 3)}{num_marker(326, 230, 4)}{num_marker(64, 214, 5)}
</svg>'''
details = [
    ("Grade for the site", "316 at minimum within 5 km of surf, and in rain-sheltered spots outdoors"),
    ("Roughness below 0.5 µm Ra", "state the roughness, not just \"No. 4\"; run brushed grain vertically"),
    ("Welds finished properly", "ground flush and polished to 320 grit or finer; wire brushing is not adequate"),
    ("A design that drains", "no crevices, intermittent welds, deep grooves or flat ledges that hold water"),
    ("Wash what rain can't reach", "when the windows need washing; mild detergent, never bleach or chloride cleaners"),
]
info_details = card("Finish and design", "Five details that stop tea staining",
    "Where salt collects on an outdoor railing, and what to specify so 304 or 316 stays clean.",
    f"<div class='split'><div class='fig'>{diag_svg}</div>{numbered(details)}</div>",
    callout="IMOA: \"Specifying the surface roughness is as important as selecting the right stainless steel.\"",
    src="Sources: ASSDA, Preventing Coastal Corrosion (Tea Staining); IMOA, Selecting Stainless Steel for Optimum Performance. Simplified diagram, not to scale.")

out = save_and_render({
    "cover-304-vs-316-stainless-steel-singapore": cover(cover_svg),
    "304-vs-316-stainless-steel-grade-guide-singapore": info_grades,
    "stainless-steel-tea-staining-prevention-singapore": info_details,
}, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "posts", SLUG))
print(out)
