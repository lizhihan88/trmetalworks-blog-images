import json, os
CSS = open("/home/claude/tr/tr_style.css").read()
OUT = "/home/claude/tr/img"
os.makedirs(OUT, exist_ok=True)
INK = "#262626"; RED = "#D7261E"; STEEL = "#9AA5AE"; LSTEEL = "#D5DBE0"; PALE = "#EEF1F3"

def page(inner):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{inner}</body></html>"

def foot(src):
    return f"<div class='foot'><div class='src'>{src}</div><div class='mark'><div class='seal'>TR</div>trmetalworks.com</div></div>"

def card(pill, title, sub, body, callout=None, note=None, src=""):
    c = f"<div class='card'><span class='pill'>{pill}</span><h1>{title}</h1><div class='sub'>{sub}</div><div class='body'>{body}</div>"
    if callout: c += f"<div class='callout'>{callout}</div>"
    if note: c += f"<div class='note'>{note}</div>"
    c += foot(src) + "</div>"
    return page(c)

def cover(svg):
    return page(f"<div class='card cover' style='border:0;padding:0'>{svg.replace('width=\"800\" height=\"545\"', 'width=\"800\" height=\"545\" style=\"transform:translateY(-20px)\"')}</div>")

S = f'stroke="{INK}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"'

# ---------- COVERS ----------
gate_bars_l = "".join(f'<line x1="{x}" y1="250" x2="{x}" y2="448" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>' for x in range(262, 392, 26))
gate_bars_r = "".join(f'<line x1="{x}" y1="250" x2="{x}" y2="448" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>' for x in range(434, 562, 26))
cover_gate = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="470" x2="700" y2="470" {S}/>
<rect x="150" y="160" width="84" height="310" rx="6" fill="{LSTEEL}" {S}/>
<rect x="134" y="128" width="116" height="36" rx="6" fill="{STEEL}" {S}/>
<rect x="566" y="160" width="84" height="310" rx="6" fill="{LSTEEL}" {S}/>
<rect x="550" y="128" width="116" height="36" rx="6" fill="{STEEL}" {S}/>
{gate_bars_l}{gate_bars_r}
<rect x="240" y="200" width="154" height="252" rx="4" fill="none" {S}/>
<rect x="406" y="200" width="154" height="252" rx="4" fill="none" {S}/>
<rect x="240" y="200" width="154" height="50" rx="4" fill="{RED}" {S}/>
<rect x="406" y="200" width="154" height="50" rx="4" fill="{RED}" {S}/>
<circle cx="290" cy="225" r="9" fill="#fff" stroke="{INK}" stroke-width="6"/><circle cx="345" cy="225" r="9" fill="#fff" stroke="{INK}" stroke-width="6"/>
<circle cx="456" cy="225" r="9" fill="#fff" stroke="{INK}" stroke-width="6"/><circle cx="511" cy="225" r="9" fill="#fff" stroke="{INK}" stroke-width="6"/>
<rect x="380" y="320" width="16" height="44" rx="6" fill="{RED}" stroke="{INK}" stroke-width="7"/>
<rect x="404" y="320" width="16" height="44" rx="6" fill="{RED}" stroke="{INK}" stroke-width="7"/>
</svg>'''

btns = ""
for r in range(4):
    for c in range(3):
        x = 477 + c * 56; y = 238 + r * 50
        fill = RED if (r == 3 and c == 2) else "#fff"
        btns += f'<rect x="{x}" y="{y}" width="40" height="34" rx="8" fill="{fill}" stroke="{INK}" stroke-width="7"/>'
cover_cost = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<rect x="440" y="110" width="226" height="340" rx="24" fill="{LSTEEL}" {S}/>
<rect x="466" y="140" width="174" height="70" rx="10" fill="{STEEL}" stroke="{INK}" stroke-width="8"/>
<line x1="560" y1="176" x2="618" y2="176" stroke="#fff" stroke-width="10" stroke-linecap="round"/>
{btns}
<path d="M150 170 L238 170 L238 352 L404 352 L404 440 L150 440 Z" fill="{STEEL}" {S}/>
<circle cx="194" cy="232" r="15" fill="#fff" stroke="{INK}" stroke-width="7"/>
<circle cx="194" cy="306" r="15" fill="#fff" stroke="{INK}" stroke-width="7"/>
<circle cx="300" cy="396" r="15" fill="#fff" stroke="{INK}" stroke-width="7"/>
<circle cx="360" cy="396" r="15" fill="#fff" stroke="{INK}" stroke-width="7"/>
<line x1="110" y1="470" x2="700" y2="470" {S}/>
</svg>'''

cover_kitchen = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<path d="M520 186 L520 118 Q520 92 548 92 L566 92 Q594 92 594 120 L594 142" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
<rect x="500" y="176" width="40" height="18" rx="4" fill="{STEEL}" stroke="{INK}" stroke-width="7"/>
<rect x="112" y="192" width="576" height="40" rx="4" fill="{PALE}" {S}/>
<rect x="430" y="258" width="190" height="86" rx="16" fill="{STEEL}" {S}/>
<rect x="140" y="258" width="24" height="206" rx="4" fill="{STEEL}" stroke="{INK}" stroke-width="8"/>
<rect x="636" y="258" width="24" height="206" rx="4" fill="{STEEL}" stroke="{INK}" stroke-width="8"/>
<rect x="388" y="258" width="24" height="206" rx="4" fill="{STEEL}" stroke="{INK}" stroke-width="8"/>
<rect x="100" y="228" width="600" height="34" rx="5" fill="{LSTEEL}" {S}/>
<rect x="126" y="394" width="548" height="20" rx="4" fill="{LSTEEL}" stroke="{INK}" stroke-width="9"/>
<rect x="196" y="338" width="120" height="56" rx="10" fill="{RED}" stroke="{INK}" stroke-width="9"/>
<line x1="178" y1="352" x2="196" y2="352" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<line x1="316" y1="352" x2="334" y2="352" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<rect x="132" y="462" width="40" height="14" rx="4" fill="{RED}" stroke="{INK}" stroke-width="7"/>
<rect x="628" y="462" width="40" height="14" rx="4" fill="{RED}" stroke="{INK}" stroke-width="7"/>
<rect x="380" y="462" width="40" height="14" rx="4" fill="{RED}" stroke="{INK}" stroke-width="7"/>
<line x1="90" y1="484" x2="710" y2="484" {S}/>
</svg>'''

# ---------- INFOGRAPHICS ----------
def dots(n, label=""):
    d = "".join(f"<span class='dot{' on' if i < n else ''}'></span>" for i in range(3))
    return f"<span class='dots'>{d}</span>" + (f"<span class='dl'>{label}</span>" if label else "")

rows = [
    ("Strength and stiffness", [dots(3), dots(2, "needs deeper sections on wide gates"), dots(3)]),
    ("Light weight", [dots(1), dots(3, "about a third of steel"), dots(1)]),
    ("Rust resistance", [dots(2, "only as good as its coating"), dots(3, "no red rust"), dots(3, "316 near the sea")]),
    ("Relative cost", ["<b>Lowest</b>", "<b>Medium</b>", "<b>Highest</b>"]),
    ("Best for", ["Wide, heavy or high-security gates", "Sliding and auto gates, homes near the coast", "A clean modern look with no paint to fail"]),
]
g = "<div class='grid' style='grid-template-columns: 1.05fr 1.3fr 1.3fr 1.3fr'>"
g += "<div class='h' style='background:#3A3E44'>Compare</div><div class='h'>Mild steel<small>hot-dip galvanised + powder coated</small></div><div class='h'>Aluminium<small>powder coated or wood-grain</small></div><div class='h'>Stainless steel<small>grade 304 or 316</small></div>"
for i, (lab, cells) in enumerate(rows):
    alt = " row-alt" if i % 2 else ""
    g += f"<div class='l{alt}'>{lab}</div>" + "".join(f"<div class='c{alt}'>{c}</div>" for c in cells)
g += "</div>"
info_gate_materials = card("Metal gates", "Which gate material suits your home?",
    "How the three main gate metals compare in Singapore's heat, rain and humidity.", g,
    callout="A mild steel gate is only as good as its coating: ask for hot-dip galvanising under the powder coat, and drain holes so water can't sit inside the frame.",
    src="TR Metalworks guide. Ratings are relative, for typical landed-home gates.")

swing_svg = f'''<svg viewBox="0 0 340 250" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="0" y="200" width="340" height="50" fill="#E3E6E9"/><text x="170" y="231" text-anchor="middle" font-size="12" font-weight="700" fill="#6B7078">ROAD</text>
<text x="170" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#6B7078">COMPOUND</text>
<line x1="0" y1="192" x2="70" y2="192" stroke="{INK}" stroke-width="8"/><line x1="270" y1="192" x2="340" y2="192" stroke="{INK}" stroke-width="8"/>
<rect x="62" y="182" width="16" height="20" fill="{STEEL}" stroke="{INK}" stroke-width="3"/><rect x="262" y="182" width="16" height="20" fill="{STEEL}" stroke="{INK}" stroke-width="3"/>
<path d="M78 192 A96 96 0 0 1 170 96" fill="rgba(215,38,30,0.08)" stroke="{RED}" stroke-width="2.5" stroke-dasharray="6 5"/>
<path d="M262 192 A96 96 0 0 0 170 96" fill="rgba(215,38,30,0.08)" stroke="{RED}" stroke-width="2.5" stroke-dasharray="6 5"/>
<line x1="78" y1="192" x2="108" y2="104" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<line x1="262" y1="192" x2="232" y2="104" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<line x1="78" y1="192" x2="262" y2="192" stroke="{STEEL}" stroke-width="3" stroke-dasharray="3 4"/>
<text x="170" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="{RED}">keep this arc clear</text>
</svg>'''
slide_svg = f'''<svg viewBox="0 0 340 250" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="0" y="200" width="340" height="50" fill="#E3E6E9"/><text x="170" y="231" text-anchor="middle" font-size="12" font-weight="700" fill="#6B7078">ROAD</text>
<text x="170" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#6B7078">COMPOUND</text>
<line x1="0" y1="192" x2="30" y2="192" stroke="{INK}" stroke-width="8"/><line x1="160" y1="192" x2="340" y2="192" stroke="{INK}" stroke-width="8"/>
<rect x="22" y="182" width="16" height="20" fill="{STEEL}" stroke="{INK}" stroke-width="3"/><rect x="152" y="182" width="16" height="20" fill="{STEEL}" stroke="{INK}" stroke-width="3"/>
<line x1="40" y1="178" x2="150" y2="178" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<line x1="170" y1="170" x2="300" y2="170" stroke="{STEEL}" stroke-width="7" stroke-linecap="round" stroke-dasharray="10 7"/>
<path d="M120 150 L215 150" stroke="{RED}" stroke-width="3" marker-end="url(#a)"/>
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{RED}"/></marker></defs>
<line x1="170" y1="120" x2="300" y2="120" stroke="{RED}" stroke-width="2"/><line x1="170" y1="113" x2="170" y2="127" stroke="{RED}" stroke-width="2"/><line x1="300" y1="113" x2="300" y2="127" stroke="{RED}" stroke-width="2"/>
<text x="235" y="106" text-anchor="middle" font-size="11" font-weight="700" fill="{RED}">side run ≥ opening</text>
<text x="95" y="167" text-anchor="middle" font-size="10" font-weight="600" fill="#4A4E55">gate closed</text>
</svg>'''
panels = f"""<div class='panels'>
<div class='panel'><h3>Swing gate</h3>{swing_svg}<p>Leaves usually open inwards, so they never swing over the road. Each leaf needs a clear arc behind the opening, free of cars, steps and plants.</p></div>
<div class='panel'><h3>Sliding gate</h3>{slide_svg}<p>The leaf slides behind the wall or fence, so you need a straight run beside the opening at least as long as the gate, plus a level track kept clear of leaves and grit.</p></div>
</div>"""
info_gate_space = card("Swing or sliding", "How much space does each gate need?",
    "Plan view of a driveway, seen from above.", panels,
    callout="Before you choose, measure the opening width at the top and the bottom, the height, which way the ground slopes, and the space behind and beside the opening.",
    src="TR Metalworks guide. Simplified diagram, not to scale.")

# cost: setup share chart
qty = [1, 5, 10, 50, 100]; S_ = 150.0; P = 42.0
maxv = S_ + P
bars = ""
W = 680; H = 230; x0 = 40; bw = 70; gap = (W - x0 - 5 * bw) / 5
for i, q in enumerate(qty):
    s = S_ / q; tot = s + P
    hp = P / maxv * 190; hs = s / maxv * 190
    x = x0 + gap / 2 + i * (bw + gap)
    ybase = 205
    bars += f'<rect x="{x:.1f}" y="{ybase-hp:.1f}" width="{bw}" height="{hp:.1f}" fill="{STEEL}"/>'
    if hs > 1.5:
        bars += f'<rect x="{x:.1f}" y="{ybase-hp-hs:.1f}" width="{bw}" height="{hs:.1f}" fill="{RED}"/>'
    lab = "1 piece" if q == 1 else f"{q} pieces"
    bars += f'<text x="{x+bw/2:.1f}" y="225" text-anchor="middle" font-size="12" font-weight="700" fill="#2B2E33">{lab}</text>'
chart = f'''<div class='fig' style='padding:14px 14px 6px'>
<svg viewBox="0 0 {W} {H+10}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<line x1="{x0}" y1="205" x2="{W}" y2="205" stroke="#C9CED3" stroke-width="1.5"/>
<text x="10" y="110" font-size="11" fill="#6B7078" transform="rotate(-90 14 110)" text-anchor="middle">price per piece</text>
{bars}
</svg>
<div style='display:flex;gap:22px;justify-content:center;font-size:11.5px;color:#3B3E44;margin-top:2px'>
<span><span style='display:inline-block;width:11px;height:11px;background:{RED};border-radius:2px;margin-right:6px;vertical-align:-1px'></span>Setup share: programming, nesting, tooling, jigs</span>
<span><span style='display:inline-block;width:11px;height:11px;background:{STEEL};border-radius:2px;margin-right:6px;vertical-align:-1px'></span>Material, machine time and labour</span>
</div></div>'''
info_cost_qty = card("Metal fabrication cost", "Why the price per piece falls as quantity rises",
    "Setup is paid once per job and shared across the batch, so a single part carries all of it.", chart,
    callout="Order spares and related parts in the same batch: the setup has already been paid for.",
    src="TR Metalworks guide. Illustrative proportions only, not a price list; real setup costs vary by job.")

items = [
    ("Material grade and thickness", "e.g. 1.2 mm grade 304 vs 1.5 mm grade 316"),
    ("Finish", "mill, brushed, painted, powder coated, or galvanised + powder coated"),
    ("Quantity", "including the spares you'll need"),
    ("Delivery and installation", "lifting, access and after-hours work"),
    ("Site measurement", "checked on site before fabrication starts"),
    ("Making good", "hacking, patching and touch-up after installation"),
    ("Drawings and changes", "who prepares them, and how changes are charged"),
    ("Validity", "how long the price holds as metal prices move"),
]
chk = "<div class='checks'>" + "".join(f"<div class='chk'><div class='box'>✓</div><div><b>{a}</b><span>{b}</span></div></div>" for a, b in items) + "</div>"
info_cost_compare = card("Comparing quotes", "8 things to check before you compare totals",
    "Big gaps between metal fabrication quotes usually come from different assumptions, not different margins.", chk,
    callout="If two quotes still differ after this check, ask each fabricator what they assumed for thickness, finish and installation.",
    src="TR Metalworks guide to comparing metal fabrication quotes in Singapore.")

def n(cx, cy, k):
    return f'<circle cx="{cx}" cy="{cy}" r="12" fill="{RED}"/><text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">{k}</text>'
table_svg = f'''<svg viewBox="0 0 380 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="34" y="62" width="312" height="30" rx="2" fill="{PALE}" stroke="{INK}" stroke-width="4"/>
<path d="M262 64 L262 34 Q262 24 272 24 L284 24 Q294 24 294 34 L294 44" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<rect x="28" y="90" width="324" height="16" rx="2" fill="{LSTEEL}" stroke="{INK}" stroke-width="4"/>
<line x1="28" y1="90" x2="28" y2="82" stroke="{INK}" stroke-width="4"/><line x1="352" y1="90" x2="352" y2="82" stroke="{INK}" stroke-width="4"/>
<rect x="206" y="106" width="104" height="44" rx="9" fill="{STEEL}" stroke="{INK}" stroke-width="4"/>
<rect x="44" y="106" width="11" height="148" fill="{STEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="326" y="106" width="11" height="148" fill="{STEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="40" y="206" width="300" height="9" fill="{LSTEEL}" stroke="{INK}" stroke-width="3"/>
<rect x="40" y="254" width="19" height="7" rx="2" fill="{RED}" stroke="{INK}" stroke-width="2.5"/>
<rect x="322" y="254" width="19" height="7" rx="2" fill="{RED}" stroke="{INK}" stroke-width="2.5"/>
<line x1="20" y1="265" x2="360" y2="265" stroke="{INK}" stroke-width="3"/>
<line x1="12" y1="98" x2="12" y2="263" stroke="{STEEL}" stroke-width="2"/><line x1="7" y1="98" x2="17" y2="98" stroke="{STEEL}" stroke-width="2"/><line x1="7" y1="263" x2="17" y2="263" stroke="{STEEL}" stroke-width="2"/>
{n(130, 50, 1)}{n(20, 74, 2)}{n(150, 120, 3)}{n(258, 172, 4)}{n(190, 192, 5)}{n(76, 282, 6)}{n(12, 180, 7)}
</svg>'''
li = [
    ("Upstand at the wall", "stops spills running down behind the table"),
    ("Raised edge", "keeps water on the table in wet areas"),
    ("1.2–1.5 mm top with stiffeners", "reinforce where heavy equipment sits"),
    ("Welded-in sink bowl", "one continuous top, fewer joints to trap dirt"),
    ("Undershelf", "set to clear your containers and the mop"),
    ("Adjustable feet", "kitchen floors slope towards the drains"),
    ("Working height", "most work tables are about 850–900 mm"),
]
nl = "<ul class='nl'>" + "".join(f"<li><div class='num'>{i+1}</div><div><b>{a}</b><span>{b}</span></div></li>" for i, (a, b) in enumerate(li)) + "</ul>"
info_kitchen_anatomy = card("F&amp;B kitchen fabrication", "Anatomy of a custom stainless steel work table",
    "The details that keep an F&amp;B prep table clean, level and solid.",
    f"<div class='split'><div class='fig'>{table_svg}</div>{nl}</div>",
    callout="Confirm the plumbing points, floor traps and grease trap position before the sink run is fabricated.",
    src="TR Metalworks guide. Simplified diagram, not to scale. Common trade dimensions; confirm them for your kitchen.")

cards = [
    ("304", "The kitchen standard", "#2B2E33", "Prep tables, sinks, shelving, splashbacks and wall cladding.", "Can pit with long exposure to salt, brine or chlorine-based cleaners."),
    ("316", "For salt and brine", RED, "Brine and seafood areas, salty marinades, coastal and outdoor kitchens.", "Costs more than 304; only needed where chlorides are a real problem."),
    ("201", "Budget, dry use", "#8C969F", "Light, dry storage and display.", "Less nickel and lower corrosion resistance; may stain with salty or acidic food and strong cleaners."),
]
c3 = "<div class='cards3'>" + "".join(f"<div class='gcard'><div class='top' style='background:{bg}'><div class='g'>{g_}</div><div class='t'>{t}</div></div><div class='in'><div class='k'>Use it for</div><div class='v'>{u}</div><div class='k'>Watch out</div><div class='v'>{w}</div></div></div>" for g_, t, bg, u, w in cards) + "</div>"
info_kitchen_grades = card("Stainless steel grades", "304, 316 or 201: which grade goes where?",
    "Match the grade to what will touch the steel every day.", c3,
    callout="Not sure which grade you're being offered? Ask for the grade to be written on the quote and the invoice.",
    src="TR Metalworks guide to stainless steel grades for F&amp;B kitchens in Singapore.")

files = {
    "cover-metal-gates-singapore": (cover(cover_gate), 800),
    "metal-gate-materials-compared-singapore": (info_gate_materials, 800),
    "swing-vs-sliding-gate-space-plan": (info_gate_space, 800),
    "cover-metal-fabrication-cost-singapore": (cover(cover_cost), 800),
    "metal-fabrication-price-per-piece-quantity": (info_cost_qty, 800),
    "compare-metal-fabrication-quotes-checklist": (info_cost_compare, 800),
    "cover-stainless-steel-kitchen-fabrication": (cover(cover_kitchen), 800),
    "stainless-steel-work-table-anatomy": (info_kitchen_anatomy, 800),
    "stainless-steel-grades-304-316-201-kitchen": (info_kitchen_grades, 800),
}
jobs = []
for name, (html, w) in files.items():
    p = f"{OUT}/{name}.html"
    open(p, "w").write(html)
    jobs.append({"html": p, "out": f"{OUT}/{name}.png", "width": w})
json.dump(jobs, open(f"{OUT}/jobs.json", "w"))
print(len(jobs))
