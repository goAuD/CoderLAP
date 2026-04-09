# Next Thread Handoff

## Active Repository

- Local path: `C:\GitHub\CoderLAP`
- GitHub repo: `https://github.com/goAuD/CoderLAP`
- Owner / code owner: `goAuD` / Viktor Halupka
- Default branch: `main`
- Working branch: `dev`

## Current State

- The content corpus is complete.
- There are `18` main topic folders.
- There are `233` canonical subtopic `README.md` files.
- The metadata registry exists:
  - `LAP_CONTENT_REGISTRY.json`
  - `LAP_CONTENT_REGISTRY.csv`
- The practical reference implementation exists under:
  - `18_Uebungsbeispiel/Musterloesung_Minimal`

## Read These First In A New Thread

1. `AGENTS.md`
2. `README.md`
3. `LAP_DEPLOY_STRATEGY.md`

Read only when relevant:

- `LAP_ARCHITECTURE_ADOPTION.md`
- `LAP_CONTENT_ARCHITECTURE.md`
- `LAP_CONTENT_REGISTRY.json`

## Most Likely Next Work

- frontend/static-site scaffold
- i18n structure
- deployment preparation
- Debian + Caddy setup
- server-side Git workflow

## Deployment Context

Assume the next deployment-oriented thread may happen on another PC because:

- that machine has SSH access to the Debian server
- deployment work should continue from this repository state
- the site should remain static-first and low-complexity
- Caddy is the intended web server

## Registry Rule

If canonical topic content changes, regenerate the registry:

```powershell
python .\scripts\generate_content_registry.py
```

## Do Not Change By Default

- the numbered German folder structure
- the PDF-based topic hierarchy
- Hungarian content as the primary source language
- Markdown as the source of truth
