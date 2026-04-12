# CoderLAP MD013 Cleanup Strategy

Last updated: `2026-04-12`

## Purpose

This document defines how to reduce the remaining `MD013` (`line-length`) warnings without mixing formatting churn into normal content, frontend, legal, or deploy work.

The warning volume is currently large enough that a single global reflow pass would create noisy diffs and make real content review harder.

## Current Rule

- `MD013` stays enabled
- cleanup happens in dedicated batches
- cleanup should improve readability, not just satisfy the linter mechanically

## What Counts As Success

- warning count trends down in predictable batches
- topic meaning does not change
- blame noise stays contained
- long URLs, tables, and code snippets are only wrapped when it is clearly safe

## What Not To Do

- do not mass-reflow all `233` topic files in one commit
- do not combine `MD013` cleanup with legal, deploy, search, or frontend changes
- do not rewrite exam wording just to shorten lines
- do not aggressively wrap Markdown tables or code fences if that hurts readability

## Recommended Order

### Phase 1: Shared project docs

Clean first:

- root `README.md`
- `AGENTS.md`
- `docs/project/**/*.md`
- `docs/process/**/*.md`
- legal source files under `site/content/legal/`

Reason:

- these files are short, high-visibility, and easier to review safely

### Phase 2: Topic corpus by module

Clean the learning content in small batches:

- one main module at a time
- or at most `10-20` topic files per batch

Recommended batch naming:

- `style: wrap md013 in module 01`
- `style: wrap md013 in module 02`

Reason:

- keeps review scope understandable
- limits merge conflicts against ongoing content edits

### Phase 3: Exception review

After the bulk of real prose is cleaned up, review the remaining warnings.

Typical acceptable leftovers may include:

- very long source URLs
- compact tables that become worse when split
- literal command examples
- legal citations that are clearer on one line

If these leftovers are frequent and justified, only then consider a narrow config adjustment. Do not weaken the rule before the easy cleanup is done.

## Safe Editing Rules

- preserve wording unless a line break requires a tiny punctuation-safe rewrite
- prefer breaking bullet items at logical clauses
- prefer breaking paragraphs into shorter sentences instead of arbitrary hard wraps
- keep source lists readable and explicit
- keep Hungarian canonical topic files and German sidecars structurally aligned when both are touched

## Operational Workflow

For each cleanup batch:

1. pick a narrow scope
2. run the Markdown linter for that scope
3. fix only `MD013` unless another warning is trivial and local
4. build the site if shared docs, legal files, or templates were touched
5. keep the commit message style-only and explicit

## Suggested Commands

Repository-wide inspection:

```powershell
markdownlint "**/*.md" --config .markdownlint.json
```

Scoped inspection example:

```powershell
markdownlint "docs/**/*.md" --config .markdownlint.json
```

Module-scoped inspection example:

```powershell
markdownlint "01_Grundlagen_in_der_Informationstechnik/**/*.md" --config .markdownlint.json
```

## Decision Rule

If the work changes meaning, tone, or translation alignment, it is no longer a style-only cleanup and should be handled as a separate content review.
