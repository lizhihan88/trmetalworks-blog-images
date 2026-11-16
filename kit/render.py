import sys, asyncio, json
from playwright.async_api import async_playwright
# usage: python3 render.py spec.json  -> renders each {html, out, width} to PNG at 2x
async def main(spec):
    jobs = json.load(open(spec))
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        for j in jobs:
            pg = await b.new_page(viewport={"width": j.get("width", 800), "height": 400}, device_scale_factor=2)
            await pg.set_content(open(j["html"]).read(), wait_until="networkidle")
            el = await pg.query_selector(".card")
            await el.screenshot(path=j["out"])
            await pg.close()
            print("ok", j["out"])
        await b.close()
asyncio.run(main(sys.argv[1]))
