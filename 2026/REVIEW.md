# Revision review

## Changes

- Original Masonry hooks, animated repositioning and hover overlays restored; current colors, typography and card styling retained.
- Collaboration description centralized in the 2026 About page.
- About page uses the same original animated map as the 2024 edition, copied byte for byte.
- Project descriptions appear once, without the redundant heading and introductory summary.
- Application and repository links grouped in a dedicated access section.
- Teams listed under institution headings, without row-wise student pairing.
- Detailed source-file links removed from public pages.
- Image sections replaced by the teams' original GIFs where available.
- No deployment files or 2024 files are included in this revision.

## Media

- Group 1: original animated GIF linked from the README (879 frames).
- Group 3: original animated GIF linked from the README (235 frames).
- Group 4: original `Sostenpyme.gif`, unmodified.
- Group 2: original `apresentacao.gif` recovered from commit `6edabfc42dd8490f072047bb2942787b8ad3a83d` (1990 frames); the current branch deleted it in commit `afdd63e`.
- Group 5: no animation found; a static entry-screen fallback is used until the team provides one.

## Still to verify

- Rafael's full name; the page uses the supplied name Rafael.
- Supply the missing animation for group 5, then replace its demo shortcode's `src` in `index.md` with the animation filename.
- Academic details for the 2026 About page can be extended with official Chilean course title, faculty and dates if desired; these are not copied from 2024.

`projects.json` retains the research inventory for maintenance only. Hugo does not publish it or the review notes.

## Validation

Hugo 0.137.1 build passed. Internal page and asset links passed. Desktop and mobile browser checks passed for all five project pages with no horizontal overflow. Masonry initializes with its original 0.4-second transition; hover overlay and icon were verified. The animated map is byte-identical to the 2024 asset.
