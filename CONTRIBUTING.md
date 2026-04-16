# Contributing to CoderLAP

## Scope

`CoderLAP` is a structured LAP study knowledge base for `Applikationsentwicklung - Coding`.

The repository is primarily:

- a Markdown content project
- a live static-site source
- a long-running study/reference corpus

## Before you change anything

1. Read [AGENTS.md](./AGENTS.md).
2. Keep the numbered German folder structure intact.
3. Treat the topic `README.md` files as the canonical content layer.
4. Treat `LAP_CONTENT_REGISTRY.json` and `LAP_CONTENT_REGISTRY.csv` as generated metadata outputs.
5. Follow [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) in all repo interactions.

## Content rules

- Write topic content in Hungarian unless the task explicitly says otherwise.
- Keep folder names and file names in German.
- Preserve the visual-first Markdown structure already used across the project.
- Prefer current, trustworthy sources.
- Do not remove source lists from topic documents.

## Structural rules

- Do not rename topic folders casually.
- Do not migrate to a different content tree unless that change is explicitly requested and planned.
- Prefer relative links inside documentation when possible.

## Registry rule

If canonical topic content changes, regenerate the registry:

```powershell
python .\scripts\generate_content_registry.py
```

## Branching suggestion

- `main` for stable, reviewed state
- `dev` for ongoing work

## Pull requests

Keep pull requests focused.

Good examples:

- one topic block improvement
- one architecture/doc cleanup
- one frontend milestone

Avoid mixing:

- content rewrites
- deployment changes
- frontend refactors

in the same PR unless they are tightly coupled.
