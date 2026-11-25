from hh_kit import *
from build_vinyl_wrap import wood  # reuse helper
c = f'''<svg viewBox="0 0 800 545" width="800" height="545" xmlns="http://www.w3.org/2000/svg">
<rect x="110" y="70" width="580" height="130" rx="6" fill="#FFFFFF" {S}/>
<rect x="124" y="84" width="176" height="102" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<rect x="312" y="84" width="176" height="102" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<rect x="500" y="84" width="176" height="102" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<rect x="110" y="290" width="580" height="190" rx="6" fill="#FFFFFF" {S}/>
<rect x="96" y="262" width="608" height="30" rx="6" fill="{PEACH}" {S}/>
<rect x="124" y="306" width="176" height="158" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<rect x="312" y="306" width="176" height="158" rx="4" fill="{MINT}" stroke="{NAVY}" stroke-width="6"/>
<g>{wood(503, 309, 170, 152, 5)}</g>
<rect x="500" y="306" width="176" height="158" rx="4" fill="none" stroke="{NAVY}" stroke-width="6"/>
<path d="M312 306 L400 306 L400 464 L312 464 Z" fill="#E9C9A0" opacity="0.95"/>
<path d="M400 306 C392 340, 392 420, 404 464" fill="none" stroke="{ORANGE}" stroke-width="9" stroke-linecap="round"/>
<rect x="312" y="306" width="176" height="158" rx="4" fill="none" stroke="{NAVY}" stroke-width="6"/>
<line x1="470" y1="350" x2="470" y2="410" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<line x1="282" y1="350" x2="282" y2="410" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<line x1="658" y1="350" x2="658" y2="410" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>
<line x1="60" y1="480" x2="740" y2="480" {S}/>
</svg>'''
save_and_render({"cover-kitchen-cabinet-wrap-singapore": cover(c)}, os.path.join(HERE, "posts", "kitchen-cabinet-wrap-singapore-cost"))
