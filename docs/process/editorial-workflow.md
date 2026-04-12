# CoderLAP Editorial Workflow

Last updated: `2026-04-12`

## Purpose

This document defines the normal maintenance workflow for CoderLAP content after the initial corpus build.

It exists to keep the Hungarian canonical source, the German live translation, and the generated static site in sync without introducing unnecessary process overhead.

## Source Of Truth

- `README.md` in each numbered subtopic folder remains the canonical Hungarian source.
- `README.de.md` next to it remains the German translation sidecar used for the default frontend language.
- `LAP_CONTENT_REGISTRY.json` and `LAP_CONTENT_REGISTRY.csv` remain the machine-readable metadata layer.
- Legal pages, static root files, and UI strings live under `site/`.

## Normal Change Flow

1. Edit the canonical Hungarian `README.md` first.
2. Update the matching `README.de.md` in the same folder if the visible content changed.
3. Update project docs if the change affects workflow, legal text, deploy shape, or launch readiness.
4. Regenerate the registry if files were added, removed, renamed, or if registry metadata logic changed.
5. Rebuild the static site.
6. Run the test suite.
7. Review the rendered result in the browser if the change affects visible output, print behavior, navigation, or legal text.

## Review Gates

Every meaningful content batch should be checked against these gates:

- factual correctness against primary or official sources where relevant
- Hungarian canonical text still readable, concise, and exam-oriented
- German translation still matches the Hungarian source closely enough for live delivery
- source lists still contain live and relevant URLs
- print output still remains usable on representative topic pages
- legal pages still reflect the actual live deployment model

## Registry Notes

Current registry behavior:

- `review_status` is still a coarse editorial field and currently remains `draft` unless a later workflow expands it
- `translation_status` is generated from the actual file state
- `de_complete` means `README.de.md` exists
- `de_missing` means the German sidecar is missing

The registry should be treated as generated output, not hand-edited state.

## Review Tools

Useful commands:

```powershell
python .\scripts\review_content.py
python .\scripts\review_content.py --module 05
python .\scripts\generate_content_registry.py
python .\scripts\build_site.py
python -m unittest discover -s tests -v
```

The existing reusable AI review prompt remains here:

- [review-workflow.md](./review-workflow.md)

## When To Update Docs In Parallel

Update documentation in the same change when any of these move:

- legal wording
- deploy model
- access model
- language routing
- registry semantics
- build pipeline shape
- release/public-launch criteria

## What To Avoid

- editing German translation sidecars without checking the Hungarian canonical source
- hand-editing generated registry files without changing the generator or rerunning it
- mixing unrelated cosmetic Markdown cleanups into legal or deploy commits
- treating the site as public while `basic_auth`, restrictive `robots.txt`, and private rollout assumptions are still in place
