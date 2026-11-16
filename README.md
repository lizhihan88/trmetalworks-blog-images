# TR Metalworks blog images

Images for the trmetalworks.com blog. Wix imports each PNG from its raw GitHub URL:
`https://raw.githubusercontent.com/lizhihan88/trmetalworks-blog-images/main/posts/<slug>/<file>.png`

## Layout
- `kit/` — the image kit: `tr_style.css`, `tr_kit.py` (helpers), `render.py` (HTML → 1600 px PNG with Chrome via Playwright).
- `kit/examples/` — the build scripts used for the first posts. Copy their patterns.
- `posts/<slug>/` — one folder per blog post: `cover-<slug>.png` plus 2 infographics.

## The style (matches the Happy Homes blog, in TR colours)
- **Cover**: a flat icon illustration of the topic on white, thick charcoal outlines (`INK`), steel greys (`STEEL`, `LSTEEL`, `PALE`) and one red accent (`RED`). 800×545 SVG viewBox, drawn in code with `cover(svg)`. No text, no photos, no logos.
- **Infographics** (2 per post) with `card(pill, title, sub, body, callout, src)`: red top bar, red pill label, bold title, grey subtitle, one visual (comparison grid, labelled diagram with numbered markers, checklist, chart or three cards), a grey callout with the one thing to remember, and a footer with the source and the trmetalworks.com mark.
- Helpers: `dots(n, label)` for 1–3 ratings, `numbered(items)` and `num_marker(cx, cy, k)` for labelled diagrams, `checklist(items)`, `cards3(cards)`; CSS classes `.grid`, `.panels`, `.split`, `.fig`, `.cards3`.
- Words on images: only facts that are in the post and its sources. Never TR prices, lead times or capacities. Footer names the source (e.g. "Source: BCA …") or says "TR Metalworks guide", and "Simplified diagram, not to scale" for diagrams.
- Look at every PNG before using it (nothing cut off, labels not overlapping, markers on the right thing).

## Build and publish
```bash
cd kit && python3 my_build.py          # uses save_and_render({...}, "../posts/<slug>")
cd .. && rm -f posts/*/*.html posts/*/_jobs.json
git add posts && git commit -m "Images for <slug>" && git push
```
Needs Chrome at /usr/bin/google-chrome and the Python `playwright` package.
