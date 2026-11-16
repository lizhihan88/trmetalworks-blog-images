"""TR Metalworks blog image kit (Happy Homes-style infographics in TR colours).
Usage in a build script:
    from tr_kit import *
    html = card(pill, title, sub, body_html, callout=..., src=...)   # infographic
    html = cover(svg)                                                  # cover illustration (800x545 SVG)
    save_and_render({"name": html, ...}, outdir)                       # writes HTML + 1600px PNGs
Colours: INK charcoal outlines, RED seal red accent, STEEL / LSTEEL / PALE greys. Font: Inter.
"""
import json, os, subprocess, sys
KIT = os.path.dirname(os.path.abspath(__file__))
import json, os
CSS = open(os.path.join(KIT, "tr_style.css")).read()
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


def dots(n, label=""):
    d = "".join(f"<span class='dot{' on' if i < n else ''}'></span>" for i in range(3))
    return f"<span class='dots'>{d}</span>" + (f"<span class='dl'>{label}</span>" if label else "")

def num_marker(cx, cy, k):
    return f'<circle cx="{cx}" cy="{cy}" r="12" fill="{RED}"/><text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12" font-weight="800" fill="#fff" font-family="Inter, sans-serif">{k}</text>'

def checklist(items):
    return "<div class='checks'>" + "".join(f"<div class='chk'><div class='box'>✓</div><div><b>{a}</b><span>{b}</span></div></div>" for a, b in items) + "</div>"

def numbered(items):
    return "<ul class='nl'>" + "".join(f"<li><div class='num'>{i+1}</div><div><b>{a}</b><span>{b}</span></div></li>" for i, (a, b) in enumerate(items)) + "</ul>"

def cards3(cards):
    """cards: [(big, small, bg_colour, use_for, watch_out)]"""
    return "<div class='cards3'>" + "".join(f"<div class='gcard'><div class='top' style='background:{bg}'><div class='g'>{g}</div><div class='t'>{t}</div></div><div class='in'><div class='k'>Use it for</div><div class='v'>{u}</div><div class='k'>Watch out</div><div class='v'>{w}</div></div></div>" for g, t, bg, u, w in cards) + "</div>"

def save_and_render(pages, outdir):
    """pages: {file_stem: html}. Writes <stem>.html and renders <stem>.png (1600 px wide)."""
    os.makedirs(outdir, exist_ok=True)
    jobs = []
    for stem, html in pages.items():
        p = os.path.join(outdir, stem + ".html")
        open(p, "w").write(html)
        jobs.append({"html": p, "out": os.path.join(outdir, stem + ".png"), "width": 800})
    spec = os.path.join(outdir, "_jobs.json")
    json.dump(jobs, open(spec, "w"))
    subprocess.run([sys.executable, os.path.join(KIT, "render.py"), spec], check=True)
    return [j["out"] for j in jobs]
