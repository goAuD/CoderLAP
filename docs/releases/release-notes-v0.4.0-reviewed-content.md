# CoderLAP `v0.4.0-reviewed-content`

Release date: `2026-10-14`

## Release Intent

All 18 modules and 235 topics have been reviewed and expanded in Hungarian and
German. This milestone improves the existing exam preparation material with
clearer explanations, factual corrections, worked examples and primary sources.
It is an editorial and technical review, not official exam-board certification.

## Changes

- Update all 470 HU/DE topic documents, preserving their stable IDs and routes.
- Correct explanations of encoding and units, JavaScript parameter passing,
  SQL constraints and transactions, network protocols, security, Scrum and
  Austrian/EU legal requirements. Align the self-check answers as well.
- Add topic-specific cases and 37 new executable JavaScript console examples.
  Keep standalone exam-mistake sections out of the revised source material.
- Expand database topics with SQL/PDO examples, and web topics with HTML/CSS,
  browser APIs and technology-specific examples with explicit prerequisites.
- Align the practical SV/QR exercise with the official exam PDF: reject
  malformed input without silently repairing it, clear stale results and retain
  the QR quiet zone. Formal validity does not prove an insurance entitlement.
- Test marked examples directly from Markdown and hide editorial markers in
  the generated site. Include the module 18 overview in the content checker
  and count both numbered and bulleted bibliography entries in the registry.
- Run the static CI workflow on PRs into both `dev` and `main`; deployment
  remains restricted to `main`.

The content changes are recorded in [PR #42](https://github.com/goAuD/CoderLAP/pull/42).
The validation below records coverage and execution limits; each reviewed topic
retains its own source list.

## Validation

- 87 Python and 122 Node tests passed in the content PR, including the 37 new
  bilingual console examples and 13 SV/QR regression tests.
- All 235 topics passed structural review. Both languages have matching
  counts of 1164 self-check questions and answers.
- The bilingual build produced 512 HTML pages with no missing local target
  files or visible editorial test markers in the link/marker scan.
- An isolated local MySQL environment passed 14 HU/DE SQL executions and
  14 additional database checks, including rollback, locking and dump restore.
  That test server was shut down normally.
- PowerShell examples, browser forms/layout, RxJS and PHP examples received
  separate execution checks. Both QR outputs were independently decoded.

The release gate is the current release-PR CI, the main build/deploy workflow
and post-deployment checks. The GitHub Release records the deployed commit and
links the final Actions evidence. The HTTP source-link scan is not a substitute
for reading the source. Full Spring/.NET server integrations and physical iOS
testing were not performed in this content review.

## Access And Delivery

German remains at `/`, Hungarian at `/hu/`. The site continues to use the
existing Debian/Caddy/Cloudflare delivery path and Caddy Basic Auth. There is
no new tracking, database, shared-login rollout or production dependency in
the content update. Markdown 3.11.1 was delivered separately in the preceding
maintenance release. Semgrep remains local.

CoderQuiz and CoderCoaster hosting are outside this milestone. SkillDisplay
waits for teacher feedback; subsequent quiz content can use the corrected LAP
material. A teacher's subject review remains a useful independent check.

## Recovery

The pre-release production commit is
`ae3f957a364d2c714323ff21362db9d917575a5d`.
Use a reviewed recovery/revert PR into `main` and the normal deployment
pipeline. The previous deployed files are retained in `dist.backup` until the
next deployment. Verify the selected backup before restoring it.
