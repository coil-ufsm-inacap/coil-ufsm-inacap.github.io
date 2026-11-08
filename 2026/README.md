# COIL UFSM–INACAP 2026 — Hugo gallery

This directory is a self-contained Hugo site, using a copy of the repository's existing Creative Portfolio theme. The 2024 site is unchanged.

## Preview

From the repository root, with Hugo 0.137.1 installed:

```bash
hugo server --source 2026 --baseURL http://localhost:1313/2026/
```

Open http://localhost:1313/2026/portfolio/. Each project is under `/2026/portfolio/group1/` through `/group5/`.

## Build

```bash
hugo --source 2026 --gc --minify
```

The generated site is in `2026/public/`. Do not commit that directory.

## Integrate this revision

Replace the existing `2026/` folder with the one in this archive. All files are inside `2026/`; no deployment workflow is included or changed. The archive does not contain any 2024 files.

The original theme's Masonry initialization and image-load relayout are restored, with the revised teal/navy typography and card styling. Hover overlays are also preserved.

Publishing remains a separate step using your existing deployment setup. Keep `.github/workflows/deploy.yml` as it is unless you intentionally update it.

## Editing

- `content/portfolio/groupN/index.md`: bilingual project content, team, technology table, links and captions.
- `content/portfolio/groupN/cover.jpg`: card image with its natural proportions for the Masonry mosaic.
- `content/portfolio/groupN/access.jpg`: real public entry screen captured 2026-11-08.
- `content/portfolio/groupN/demo.gif`: original team animations where available (groups 1–4). Group 2's GIF was recovered from repository history; group 5 currently uses a static entry-screen fallback.
- `content/about/_index.md`: shared experience description.
- `config.toml`: title and sidebar navigation.
- `static/css/custom.css`: 2026 visual adjustments.
- `projects.json`: structured project inventory and source revisions used during preparation. The Markdown pages are authoritative for Hugo; this JSON is used by the capture tool and is not an automatic content generator.

The page content follows the existing bilingual PT-BR/ES approach. Project names follow the actual app labels. Group 4 and group 5 both use SOSTENPYME, so the group number stays in each title.

## Refresh screenshots

Use a local Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r 2026/tools/requirements.txt
python -m playwright install chromium
python 2026/tools/capture.py
```

This refreshes entry screens without changing covers. Add `--cover` to replace covers too.

For useful internal screenshots, open a visible browser, sign in manually with a demo account, navigate to the desired screen and enter an image name at the terminal prompt:

```bash
python 2026/tools/capture.py --group 1 --interactive
```

Suggested names: `diagnosis`, `results`, `plan`. Add the resulting images to the project's Markdown, for example `![Resultados / Resultados](results.jpg)`.

The script keeps authentication only in memory and closes it after each project. It does not create accounts, populate company data or save credentials. Use demonstration data; avoid personal information. The screenshot tool needs direct network access from your computer and may take longer when a Render service is asleep. Review captures before publishing.

## Credits

Original theme: https://github.com/kishaningithub/hugo-creative-portfolio-theme (MIT; license included in `themes/portfolio/LICENSE`). Project interfaces and the group 4 demo belong to their respective student teams; source links are on each page.
