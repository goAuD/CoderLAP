# CoderLAP Content and Build Architecture

Last updated: `2026-04-16`

## Purpose

This document describes the **current** content architecture of `CoderLAP`.

It reflects the repository after:

- the Hungarian source corpus was completed
- all `235` registered topic documents were translated to German as
  `README.de.md`
- the static frontend and i18n layer were implemented

## Canonical Sources

The project has four distinct source layers:

1. **PDF hierarchy source**
   - `themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`
   - Defines the canonical topic tree.

2. **Canonical learning content**
   - `README.md` inside each numbered subtopic folder
   - Hungarian remains the canonical source language.

3. **Translation sidecars**
   - `README.de.md` next to the Hungarian `README.md`
   - German is the translated delivery language, not the canonical authoring
     source.

4. **Machine-readable metadata**
   - `LAP_CONTENT_REGISTRY.json`
   - `LAP_CONTENT_REGISTRY.csv`
   - Used for indexing, navigation, build input, and stable IDs.

## Current Repository Model

Relevant layout:

```text
CoderLAP/
  01_.../
    01_.../
      README.md
      README.de.md
  ...
  18_.../
  LAP_CONTENT_REGISTRY.json
  LAP_CONTENT_REGISTRY.csv
  scripts/
    build_site.py
    generate_content_registry.py
    review_content.py
    site_builder/
      build.py
      loaders.py
      navigation.py
      render.py
      settings.py
  site/
    assets/
    content/legal/
      de/
      en/
      hu/
    i18n/
      de.json
      en.json
      hu.json
    templates/
  docs/
    project/
    process/
    plans/
    superpowers/
```

## Language Model

### Content authoring

- `README.md` = Hungarian canonical content
- `README.de.md` = German translation sidecar

### Site output

- German is the default published language at `/`
- Hungarian is published at `/hu/`

### UI layer

- `site/i18n/de.json`
- `site/i18n/hu.json`

English files can exist as editorial fallback material, but the active published
site is currently `de + hu`.

## Static Build Model

Build entrypoint:

```powershell
python .\scripts\build_site.py
```

Build characteristics:

- Jinja2 templates + Markdown rendering
- static output only
- no database
- no runtime backend
- local font assets bundled in the repo
- output written to `dist/`

Generated output shape:

```text
dist/
  index.html        # German default
  topics/...
  module-packs/...
  imprint/
  privacy/
  robots.txt
  .well-known/
    security.txt
  hu/
    index.html      # Hungarian
    topics/...
    module-packs/...
    imprint/
    privacy/
  assets/
  data/
```

The site builder prefers a language-specific Markdown file when it exists:

- German build prefers `README.de.md`
- Hungarian build falls back to `README.md`

## Registry Model

Registry generator:

```powershell
python .\scripts\generate_content_registry.py
```

Current ID format:

```text
LAP-<MAIN>-<SUB>
```

Examples:

- `LAP-01-01`
- `LAP-11-43`
- `LAP-18-05`

Important rule:

- regenerate the registry if canonical topic files are added, removed, renamed,
  or structurally moved

The registry is intentionally external. The project still does **not** depend on
front matter embedded into all topic files.

Current metadata semantics worth remembering:

- `review_status` is still a coarse editorial field and currently remains
  `draft`
- `translation_status` is generated from the file system
- `de_complete` means the German sidecar exists
- `de_missing` means the German sidecar is missing

## What Is Intentionally Preserved

- the numbered German folder tree
- the PDF-aligned hierarchy
- Hungarian canonical source content
- Markdown-first authoring
- static-site delivery

## What Is Intentionally Deferred

- migration into `content/hu` / `content/de`
- full front matter across all topic files
- database-backed authoring or publishing
- CMS/editor backend
- any runtime app architecture beyond static delivery

## Current Technical Direction

The architecture is now stable enough for:

1. content/UI QA and maintenance
2. restricted live delivery at `coderlap.com`
3. Debian + Caddy delivery behind Cloudflare
4. low-attack-surface hosting with a single deploy path
5. public-safe repository visibility without changing the static-first model

This document should be updated whenever the on-disk structure, language
routing, or build pipeline changes.
