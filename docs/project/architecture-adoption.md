# CoderLAP Architecture Adoption Notes

Last updated: `2026-04-16`

## Purpose

This file explains how the original architecture intent was adapted to the
**actual** repository that now exists.

The original planning assumed a later translation phase and a later frontend
phase. Those phases are now complete enough that the repository model has to be
described in its current form, not in its earlier planned form.

## What Was Adopted

### Shared Műhely header and footer

`site/assets/css/workshop-frame.css` is the canonical frame stylesheet. CoderQuiz
and CoderCoaster keep identical copies at `assets/workshop-frame.css`, loaded
after app styles. Update all three copies together and compare hashes; there is
no shared runtime service, CDN or build dependency between repositories.

The frame uses full-width containers, 1rem safe-area-aware gutters, matching
brand/type/icon sizes, 44px controls and a 35rem mobile breakpoint. Footer title
rows and links align, with a license/source strip below a divider. Apps retain
their navigation and legal destinations; Coaster has no language switch until
a second language exists. Narrow screens may wrap LAP's two page links.

Navigation arrows use local inline Lucide `arrow-up` and `arrow-up-right` SVGs
from commit `a79b2d131dab2bf20cb224bd0937b439a9c4fa99`, with upstream notices in
`site/assets/LICENSE-Lucide.txt`: [Lucide license](https://lucide.dev/license).
The shared GitHub mark remains a brand SVG; [Lucide excludes brand logos](https://lucide.dev/brand-logo-statement).

Validation on 2026-09-11: 83 Python and 35 Node tests and the bilingual build pass.
Browser measurements compare all three apps at 320/390/844/1920px: matching
gutters, footer columns and typography, no page overflow or brand/GitHub collision.
At 390px all three headers have the same height and both language switchers align.
Physical iPhone review of this frame is pending.

### Markdown remains the source of truth

Adopted.

- Hungarian `README.md` files remain canonical
- German `README.de.md` files are delivery translations
- the frontend is only a rendering layer

### Stable IDs live in the registry

Adopted.

The project uses:

- `LAP_CONTENT_REGISTRY.json`
- `LAP_CONTENT_REGISTRY.csv`

This keeps metadata centralized without forcing front matter into all `235`
topic folders.

### The numbered folder tree stays unchanged

Adopted.

The repository already matches the official PDF structure, so no migration into
a new content tree was performed.

### Static frontend delivery

Adopted.

The repository now has a working static build pipeline:

- `scripts/build_site.py`
- `scripts/site_builder/*`
- `site/templates/*`
- `site/assets/*`

### Translation as sidecar files

Adopted in a practical form.

Instead of moving content into a new `content/de` tree, German translations are
stored next to the canonical source:

- `README.md`
- `README.de.md`

This keeps the numbered topic structure stable and keeps contributor workflow
simple.

## What Was Not Adopted

These earlier ideas were intentionally **not** implemented:

- `content/hu/**` and `content/de/**` migration
- full front matter in every topic file
- database-backed content management
- custom authentication backend
- runtime web app architecture

Those ideas are still unnecessary for the current project stage.

## What Changed Since The Early Plan

The following are now true and should be treated as current-state facts:

- all `235` registered topic documents exist in Hungarian
- all `235` registered topic documents exist in German translation form
- German is the default site language
- Hungarian is available under `/hu/`
- the static frontend is already built
- the current engineering phase is maintenance, hardening, and release hygiene

## Documentation Layout Decision

Internal project and engineering docs now belong under `docs/`, not the
repository root.

GitHub-facing root files should stay in the root:

- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `LICENSE`
- `.github/`
- `AGENTS.md`

Internal continuity, architecture, and deploy docs should live under:

- `docs/project/`
- `docs/process/`

## Current Recommendation

For future work, optimize for:

1. keeping the corpus stable
2. keeping the build deterministic
3. deploying only the static result
4. avoiding unnecessary structural rewrites
5. keeping repository-facing docs safe for public visibility

If the architecture changes again, update this file and
`docs/project/content-architecture.md` together.
