# CoderLAP `v0.3.1-workshop.1`

Release date: `2026-09-11`

## Changes

- Hide standalone exam-mistake sections from rendered topics, their navigation
  and module print packs. All 460 source sections and existing URLs remain.
- Align the header and footer with the shared CoderQuiz Workshop identity,
  retaining legal links, mobile safe areas and space for the floating button.
- Bind all four local Manrope / Source Sans 3 subsets so Hungarian accented
  letters use the same families as the surrounding text.
- Use a centered brand logo in the README and retain the refreshed homepage
  screenshot in `docs/assets/images/`.
- Preserve the earlier design prototypes in Git. They are built only on explicit
  invocation and do not ship in the standard production artifact.
- Preserve reviewed local maintenance: consistent line endings, machine-neutral
  setup docs, Dependabot version-update cooldown and main-only manual deployment.
- Keep Semgrep scans local; the prepared cloud workflow is excluded.

## Validation and delivery

The release gate is the full Python and JavaScript test suites, bilingual build,
release-PR CI, main deployment and authenticated site monitor. Browser checks
cover the shared layout; a fresh physical iOS check remains useful.
The GitHub Release records the final deployed commit and Actions evidence.

German `/`, Hungarian `/hu/`, all 235 registered topics and locally stored
progress remain. Caddy Basic Auth and the existing Debian delivery path remain.
CoderQuiz and CoderCoaster source PRs are being integrated separately; this
release does not provision their future authenticated hosting.

## Recovery

The pre-release production commit is
`c30a30119fdd0f31ea17d21489b3845dc6f8d08d`.
Use a reviewed recovery/revert PR into `main` and the normal deployment pipeline;
manual dispatch from a temporary recovery branch is now intentionally blocked.
See the [backup and restore playbook](../project/backup-restore-playbook.md).
