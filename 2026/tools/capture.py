#!/usr/bin/env python3
"""Capture the five real applications. Interactive mode lets you sign in yourself."""
import argparse, asyncio, json, re
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image, ImageOps
ROOT = Path(__file__).resolve().parents[1]

def cover(folder, image):
    with Image.open(image) as im:
        ImageOps.pad(im.convert('RGB'), (1200, 800), color='#f2f5f5').save(folder/'cover.jpg', quality=90)

async def run(args):
    projects = json.loads((ROOT/'projects.json').read_text())
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=not args.interactive)
        try:
            for project in projects:
                if args.group and project['group'] != args.group:
                    continue
                folder = ROOT/f'content/portfolio/group{project["group"]}'
                context = await browser.new_context(viewport={'width':1363,'height':936}, locale='es-CL', device_scale_factor=1)
                page = await context.new_page()
                print(f'Grupo {project["group"]}: {project["name"]}', flush=True)
                try:
                    await page.goto(project['url'], wait_until='domcontentloaded', timeout=120000)
                    await page.locator('input[type="password"]').first.wait_for(timeout=120000)
                    await page.evaluate('document.fonts.ready')
                    if args.interactive:
                        print('Sign in manually if needed, navigate, and hide private information before capturing.')
                        while True:
                            name = await asyncio.to_thread(input, 'Image name (e.g. diagnosis, results, plan; blank = next project): ')
                            if not name: break
                            if not re.fullmatch(r'[a-z0-9-]+', name):
                                print('Use lowercase letters, numbers and hyphens.'); continue
                            out = folder/(name+'.jpg')
                            await page.screenshot(path=str(out), type='jpeg', quality=92, full_page=args.full_page)
                            print('Saved:', out)
                            if args.cover: cover(folder, out)
                    else:
                        out = folder/'access.jpg'
                        await page.screenshot(path=str(out), type='jpeg', quality=92, full_page=args.full_page)
                        if args.cover: cover(folder, out)
                        print('Saved:', out)
                except Exception as exc:
                    print('Capture failed; existing images kept:', exc)
                finally:
                    await context.close()
        finally:
            await browser.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--group', type=int, choices=range(1,6))
    parser.add_argument('--interactive', action='store_true', help='Visible browser; navigate and sign in manually')
    parser.add_argument('--cover', action='store_true', help='Also replace cover.jpg from each captured image')
    parser.add_argument('--full-page', action='store_true')
    asyncio.run(run(parser.parse_args()))
