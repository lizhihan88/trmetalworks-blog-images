from hh_kit import *
OUT = os.path.join(HERE, "posts")

def wood(x, y, w, h, n=5, col="#E9C9A0"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/>'
    for i in range(1, n):
        yy = y + i * h / n
        s += f'<path d="M{x+8} {yy:.0f} C{x+w*0.3:.0f} {yy-10:.0f}, {x+w*0.6:.0f} {yy+10:.0f}, {x+w-8} {yy:.0f}" fill="none" stroke="#C99A66" stroke-width="3" stroke-linecap="round"/>'
    return s

# Cover 1: wrapped door + clock (lifespan)
c1 = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<rect x="200" y="70" width="250" height="420" rx="6" fill="{PEACH}" {S}/>
{wood(212, 82, 226, 300, 6)}
<path d="M212 382 L438 382 L438 478 L212 478 Z" fill="#F3EFE6"/>
<path d="M438 382 C400 400, 380 420, 372 470 L438 478 Z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>
<path d="M212 382 L438 382" stroke="{NAVY}" stroke-width="5" stroke-dasharray="10 9"/>
<rect x="200" y="70" width="250" height="420" rx="6" fill="none" {S}/>
<circle cx="410" cy="285" r="14" fill="{NAVY}"/>
<line x1="150" y1="490" x2="660" y2="490" {S}/>
<circle cx="575" cy="190" r="92" fill="{MINT}" {S}/>
<line x1="575" y1="190" x2="575" y2="132" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>
<line x1="575" y1="190" x2="618" y2="212" stroke="{ORANGE}" stroke-width="10" stroke-linecap="round"/>
<circle cx="575" cy="190" r="9" fill="{NAVY}"/>
</svg>'''

# Cover 2: door + cabinet + magnifier with tick (choosing an installer)
c2 = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<rect x="110" y="90" width="210" height="390" rx="6" fill="{PEACH}" {S}/>
{wood(122, 102, 186, 366, 7)}
<rect x="110" y="90" width="210" height="390" rx="6" fill="none" {S}/>
<circle cx="285" cy="290" r="12" fill="{NAVY}"/>
<rect x="360" y="250" width="300" height="230" rx="6" fill="#FFFFFF" {S}/>
<rect x="374" y="264" width="130" height="200" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<rect x="516" y="264" width="130" height="200" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<line x1="490" y1="320" x2="490" y2="380" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<line x1="530" y1="320" x2="530" y2="380" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<line x1="70" y1="480" x2="720" y2="480" {S}/>
<circle cx="560" cy="160" r="78" fill="#FFFFFF" {S}/>
<path d="M522 162 L550 190 L602 134" fill="none" stroke="{ORANGE}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="616" y1="216" x2="680" y2="280" stroke="{NAVY}" stroke-width="22" stroke-linecap="round"/>
</svg>'''

# Cover 3: kitchen cabinet with a peeling corner + roller (peeling laminate)
c3 = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<rect x="140" y="160" width="400" height="320" rx="6" fill="#FFFFFF" {S}/>
<rect x="156" y="176" width="176" height="288" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<rect x="348" y="176" width="176" height="288" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<line x1="315" y1="230" x2="315" y2="290" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<line x1="365" y1="230" x2="365" y2="290" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<path d="M524 176 L524 260 C500 250, 470 232, 452 176 Z" fill="#F3EFE6" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>
<path d="M452 176 C470 232, 500 250, 524 260 C512 226, 486 196, 452 176 Z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>
<rect x="140" y="120" width="400" height="40" rx="6" fill="{PEACH}" {S}/>
<line x1="100" y1="480" x2="700" y2="480" {S}/>
<rect x="590" y="300" width="110" height="46" rx="23" fill="{ORANGE}" {S}/>
<path d="M645 346 L645 380 L610 380 L610 450" fill="none" stroke="{NAVY}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="596" y="440" width="28" height="44" rx="8" fill="{NAVY}"/>
</svg>'''

# Infographic 1: lifespan bars (facts from the post + 3M TDS)
def bar(label, lo, hi, txt):
    l = lo / 12 * 100; w = (hi - lo) / 12 * 100
    return f"<div class='bar'><div>{label}</div><div class='track'><div class='fill' style='left:{l:.1f}%;width:{w:.1f}%'><span>{txt}</span></div></div></div>"
bars = "<div class='bars'>" + bar("3M DI-NOC, rated life<br><small style='font-weight:500;color:#4A5070'>indoor, vertical surfaces</small>", 0, 12, "up to 12 years") + bar("3M DI-NOC E-Series, rated life", 0, 8, "8 years") + bar("Typical in Singapore homes<br><small style='font-weight:500;color:#4A5070'>with good preparation</small>", 5, 10, "5 to 10 years") + "</div><div class='axis' style='margin-top:6px'><div></div><div><span>0</span><span>3</span><span>6</span><span>9</span><span>12 years</span></div></div>"
i1 = card("Vinyl wrap lifespan", "How long vinyl wrap lasts indoors", "Rated life from the film maker, and what Singapore homes typically see.", bars,
    callout="Panels beside the hob, oven or sink, and surfaces in direct sun, wear faster. Edges that are cleaned and primed last longest.",
    src="Sources: 3M DI-NOC Architectural Finishes Technical Data Sheet; Happy Homes guide. \"Interior\" means no direct sunlight.")

# Infographic 2: price ranges (same figures as the post)
rows = [("Bedroom, toilet or study door", "$190 – $280"), ("Door frame only", "$120 – $180"), ("HDB main door, single leaf", "$190 – $480"), ("Main door, double leaf", "$290 – $580"), ("Kitchen cabinet door fronts", "$36 – $42 / ft run, per tier"), ("Wardrobe door fronts", "$70 – $80 / ft run"), ("Whole HDB kitchen (3- to 5-room)", "$1,000 – $2,000")]
pr = "<div class='price'><div class='hd'>Item, installed</div><div class='hd' style='text-align:right'>Market range</div>" + "".join(f"<div class='k'>{a}</div><div class='v'>{b}</div>" for a, b in rows) + "</div>"
i2 = card("Vinyl wrap prices", "What vinyl wrap costs in Singapore", "Typical installed prices published by Singapore wrap installers, November 2026.", pr,
    callout="These are market ranges, not fixed prices. A quote far below them usually leaves out preparation, edges or a named film.",
    src="Source: published price lists of Singapore wrap installers, checked Nov 2026. Happy Homes guide.")

# Infographic 3: which fix does peeling laminate need
fixes = [("Edge lifting, board flat and dry", "Re-glue with contact adhesive, clamp or roll, replace edge banding."),
         ("Bubbles mid-panel, board flat", "Re-glue, or re-laminate or vinyl wrap the panel."),
         ("Board edge puffed up or soft", "Water-swollen board: repair or replace the panel first."),
         ("Damp, black spots or musty smell", "Fix the leak, dry out, then replace the damaged panel."),
         ("Many doors peeling, boxes sound", "Re-laminate or vinyl wrap all the fronts in one go."),
         ("Layout no longer works", "Replace: new carpentry, not a new finish.")]
i3 = card("Peeling laminate", "Which fix does your peeling laminate need?", "Press the area gently: firm and flat means the board is usually sound.", checklist(fixes),
    callout="Never wrap or re-glue over a swollen board or an active leak. The new finish will fail too.",
    src="Happy Homes guide. Simplified checklist; ask for a site check if unsure.")

save_and_render({"cover-how-long-does-vinyl-wrap-last-singapore": cover(c1), "vinyl-wrap-lifespan-singapore": i1}, os.path.join(OUT, "how-long-does-vinyl-wrap-last-singapore"))
save_and_render({"cover-choose-vinyl-wrap-company-singapore": cover(c2), "vinyl-wrap-price-singapore-2026": i2}, os.path.join(OUT, "how-to-choose-vinyl-wrap-company-singapore"))
save_and_render({"cover-peeling-laminate-repair-singapore": cover(c3), "peeling-laminate-which-fix": i3}, os.path.join(OUT, "peeling-laminate-door-cabinet-repair-singapore"))
