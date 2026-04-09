# LAP Architecture Adoption

## Purpose

This file records how `LAP_CONTENT_ARCHITECTURE.md` was applied to the **current, already-completed** project without breaking the finished folder tree.

Date of adoption review: `2026-04-09`

## What Was Adopted Now

### 1. Markdown remains the source of truth

Adopted as-is.

Practical meaning:

- the canonical study content remains the existing `README.md` files inside the numbered topic folders
- no database is introduced
- no CMS is introduced for the learning content

### 2. The current folder tree stays unchanged

Adopted with adaptation.

The architecture draft suggests a future `content/hu/**` structure, but the repository already has:

```txt
01_.../01_.../README.md
02_.../01_.../README.md
...
18_.../05_.../README.md
```

This structure is already complete, stable, and aligned with the official PDF.

Decision:

- do **not** migrate to a new tree now
- keep the current numbered German folder structure as the canonical on-disk layout

### 3. Stable IDs are adopted via an external registry

Adopted in a low-risk way.

Instead of rewriting `233` files with front matter immediately, the project now uses a generated registry:

- `LAP_CONTENT_REGISTRY.json`
- `LAP_CONTENT_REGISTRY.csv`

ID format:

```txt
LAP-<MAIN>-<SUB>
```

Examples:

- `LAP-01-01`
- `LAP-11-43`
- `LAP-18-05`

This gives the project:

- stable identifiers
- future i18n mapping anchors
- future search/filter input
- future site-build input

without rewriting every content file right now.

### 4. Repository hygiene for GitHub/private repo use

Adopted now:

- `.gitignore`
- deployment planning doc
- machine-readable content registry

These are immediate wins for:

- moving under `C:\GitHub`
- future private repo push
- later Caddy/static-site deployment

### 5. Deployment direction is formalized

Adopted now through:

- `LAP_DEPLOY_STRATEGY.md`

This captures the current practical direction:

- private GitHub repo
- simple branch model
- static-site direction later
- Caddy hosting later
- one clean deployment path only

## What Was Explicitly Deferred

### 1. Full front matter inside all content files

Deferred.

Reason:

- rewriting all `233` topic documents now would be high-effort and high-risk
- the project is already complete and internally consistent

Future direction:

- if the web frontend needs it, front matter can be added gradually
- until then, the registry carries the stable metadata

### 2. `content/hu` and `content/de` migration

Deferred.

Reason:

- would add a large migration cost with little immediate benefit
- current structure is already PDF-aligned and stable

Future direction:

- translations can later be generated into a new parallel structure if needed
- source IDs in the registry make that possible

### 3. Full `related_ids` graph inside every document

Deferred.

Reason:

- good idea for the later site
- not necessary for the current finished Markdown corpus

Future direction:

- can be added centrally in registry/build tooling later

### 4. Validation pipeline and build pipeline

Deferred, but prepared for.

Reason:

- useful later
- not required to preserve the finished content now

Preparation done:

- registry generation script added
- repo now lives in a Git-friendly shape

## Current Practical Model

The actual adopted architecture is now:

```txt
CoderLAP/
  01_.../
    01_.../
      README.md
  ...
  18_.../
  AGENTS.md
  README.md
  LAP_CONTENT_ARCHITECTURE.md
  LAP_ARCHITECTURE_ADOPTION.md
  LAP_DEPLOY_STRATEGY.md
  LAP_CONTENT_REGISTRY.json
  LAP_CONTENT_REGISTRY.csv
  scripts/
    generate_content_registry.py
```

## Recommendation Going Forward

Use this order:

1. Keep the existing Markdown tree stable.
2. Use the registry as the metadata layer.
3. Keep the active project under `C:\GitHub\CoderLAP`.
4. Push to a private repository.
5. Build the static-site layer later from the registry + Markdown.

This preserves momentum and avoids unnecessary migration work.
