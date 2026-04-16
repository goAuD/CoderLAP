# CoderLAP MD013 Cleanup Strategy

Last updated: `2026-04-16`

## Purpose

This document defines how to reduce the remaining `MD013` (`line-length`)
warnings without mixing formatting churn into normal content, frontend, legal,
or deploy work.

The warning volume is currently large enough that a single global reflow pass
would create noisy diffs and make real content review harder.

## Current Rule

- `MD013` stays enabled
- the active repository rule is pragmatic:
  - `line_length = 120`
  - headings ignored
  - tables ignored
  - code blocks ignored
- cleanup happens in dedicated batches
- cleanup should improve readability, not just satisfy the linter mechanically

## Why The Rule Was Tuned

The original `80` character rule produced too much noise for this project.

The main reasons were:

- visual study tables with longer labels
- explicit source URLs
- short technical headings and comparison lines that are readable as-is
- bilingual content with many inline code terms and legal citations

For this corpus, the stricter rule created churn faster than it created value.

The current policy keeps `MD013` useful by focusing it on genuinely overlong
running prose.

Historical planning/spec notes under `docs/plans/` and
`docs/superpowers/specs/` are intentionally excluded from the default
repository-wide lint scope. They are archival continuity documents, not active
runtime, corpus, or delivery docs.

## What Counts As Success

- warning count trends down in predictable batches
- topic meaning does not change
- blame noise stays contained
- long URLs, tables, and code snippets are only wrapped when it is clearly safe

## What Not To Do

- do not mass-reflow all `235` topic files in one commit
- do not combine `MD013` cleanup with legal, deploy, search, or frontend changes
- do not rewrite exam wording just to shorten lines
- do not aggressively wrap Markdown tables or code fences if that hurts
  readability

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

The config adjustment has already been made because the initial audit showed
that the old rule mostly punished the study format rather than bad prose.

## Safe Editing Rules

- preserve wording unless a line break requires a tiny punctuation-safe rewrite
- prefer breaking bullet items at logical clauses
- prefer breaking paragraphs into shorter sentences instead of arbitrary hard
  wraps
- keep source lists readable and explicit
- keep Hungarian canonical topic files and German sidecars structurally aligned
  when both are touched

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
npx --yes markdownlint-cli "**/*.md" --config .markdownlint.json
```

Scoped inspection example:

```powershell
npx --yes markdownlint-cli "docs/**/*.md" --config .markdownlint.json
```

Module-scoped inspection example:

```powershell
npx --yes markdownlint-cli "01_Grundlagen_in_der_Informationstechnik/**/*.md" --config .markdownlint.json
```

## Decision Rule

If the work changes meaning, tone, or translation alignment, it is no longer a
style-only cleanup and should be handled as a separate content review.
