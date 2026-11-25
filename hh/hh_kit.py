"""Happy Homes image kit: the TR kit restyled in Happy Homes colours (cream, navy, orange, mint, peach)."""
import os, sys, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(os.path.dirname(HERE), "kit")
NAVY = "#0B1446"; ORANGE = "#F4A340"; MINT = "#E3ECE3"; PEACH = "#FCEBD3"; CREAM = "#FFFAF2"; GREEN = "#3B8C5A"; GREY = "#8C93AD"; LGREY = "#D9DDEA"
INK = NAVY
css = open(os.path.join(KIT, "tr_style.css")).read()
for a, b in [("#F6F6F4", CREAM), ("#D7261E", ORANGE), ("#FBE4E2", PEACH), ("#C1211A", "#A85F05"), ("#1C1D20", NAVY), ("#2B2E33", NAVY),
             ("#E7ECEF", MINT), ("#686D75", "#4A5070"), ("#FAFAF9", "#FFFDF8"), ("#F3F4F5", "#FBF6EC")]:
    css = css.replace(a, b)
css += f"""
.box {{ background: {GREEN}; }}
.mark svg {{ display:block }}
.cover {{ background: {CREAM} !important; }}
.chk {{ background: {MINT}; border-color: #CFDCCF; }}
.panel {{ background: #fff; }}
.price {{ display:grid; grid-template-columns: 1.35fr 1fr; border-radius:10px; overflow:hidden; border:1px solid #E8DCC7; background:#fff }}
.price div {{ padding:10px 14px; font-size:12.5px; border-bottom:1px solid #F1E7D6 }}
.price .k {{ font-weight:700; color:{NAVY} }}
.price .v {{ font-weight:800; color:{NAVY}; background:{PEACH}; text-align:right }}
.price .hd {{ background:{NAVY}; color:#fff; font-weight:700; font-size:11px; letter-spacing:.6px; text-transform:uppercase }}
.bars {{ display:grid; gap:9px }}
.bar {{ display:grid; grid-template-columns: 210px 1fr; align-items:center; gap:12px; font-size:12px; color:{NAVY}; font-weight:700 }}
.track {{ position:relative; height:22px; background:#F1EADC; border-radius:6px }}
.fill {{ position:absolute; top:0; bottom:0; border-radius:6px; background:{ORANGE} }}
.fill span {{ position:absolute; right:8px; top:3px; font-size:10.5px; color:{NAVY}; font-weight:800 }}
.axis {{ display:grid; grid-template-columns: 210px 1fr; gap:12px; font-size:10px; color:#6B7090 }}
.axis div:last-child {{ display:flex; justify-content:space-between }}
"""
def page(inner):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{inner}</body></html>"
HOUSE = f'<svg width="20" height="20" viewBox="0 0 20 20"><path d="M3 9.5 L10 3.5 L17 9.5 V17 H3 Z" fill="{NAVY}"/><rect x="8.2" y="11.5" width="3.6" height="5.5" fill="{ORANGE}"/></svg>'
def foot(src):
    return f"<div class='foot'><div class='src'>{src}</div><div class='mark'>{HOUSE}happyhomes.sg</div></div>"
def card(pill, title, sub, body, callout=None, note=None, src=""):
    c = f"<div class='card'><span class='pill'>{pill}</span><h1>{title}</h1><div class='sub'>{sub}</div><div class='body'>{body}</div>"
    if callout: c += f"<div class='callout'>{callout}</div>"
    if note: c += f"<div class='note'>{note}</div>"
    return page(c + foot(src) + "</div>")
def cover(svg):
    return page(f"<div class='card cover' style='border:0;padding:0;width:800px;height:545px;display:flex;align-items:center;justify-content:center'>{svg}</div>")
S = f'stroke="{NAVY}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"'
def checklist(items):
    return "<div class='checks'>" + "".join(f"<div class='chk'><div class='box'>✓</div><div><b>{a}</b><span>{b}</span></div></div>" for a, b in items) + "</div>"
def save_and_render(pages, outdir):
    os.makedirs(outdir, exist_ok=True)
    jobs = []
    for stem, html in pages.items():
        p = os.path.join(outdir, stem + ".html"); open(p, "w").write(html)
        jobs.append({"html": p, "out": os.path.join(outdir, stem + ".png"), "width": 800})
    spec = os.path.join(outdir, "_jobs.json"); json.dump(jobs, open(spec, "w"))
    subprocess.run([sys.executable, os.path.join(KIT, "render.py"), spec], check=True)
