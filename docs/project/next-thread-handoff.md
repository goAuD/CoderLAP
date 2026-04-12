# Next Thread Handoff

Last updated: `2026-04-12`

## Active Repository

- Local path: `C:\GitHub\CoderLAP`
- GitHub repo: `https://github.com/goAuD/CoderLAP`
- Stable branch: `main`
- Active branch: `dev`

## Current Project State

- `18` main topic folders complete
- `233` canonical Hungarian topic files complete as `README.md`
- `233` German translation sidecars complete as `README.de.md`
- metadata registry present:
  - `LAP_CONTENT_REGISTRY.json`
  - `LAP_CONTENT_REGISTRY.csv`
- static site generator working
- language routing working:
  - German default at `/`
  - Hungarian at `/hu/`
- legal pages exist for `de`, `hu`, and editorial fallback `en`
- registered domain: `coderlap.com`

## Read These First In A New Thread

1. `AGENTS.md`
2. `README.md`
3. `docs/project/deploy-strategy.md`
4. `docs/project/content-architecture.md`

Read only when relevant:

- `docs/project/architecture-adoption.md`
- `docs/process/review-workflow.md`
- `LAP_CONTENT_REGISTRY.json`

## Useful Commands

Build:

```powershell
python .\scripts\build_site.py
```

Tests:

```powershell
python -m unittest discover -s tests -v
```

Local preview:

```powershell
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

## Most Likely Next Work

- final deployment prep for `coderlap.com`
- Debian + Caddy configuration
- DNS cutover on Dynadot
- merge discipline from `dev` to `main`

## Rules To Preserve

- keep the numbered German folder tree
- keep the PDF hierarchy as the structural source
- keep Hungarian `README.md` as canonical content
- keep German `README.de.md` as the translation sidecar
- keep Markdown as the authoring source of truth
- keep the delivery model static-first
