# Next Thread Handoff

Last updated: `2026-10-14`

## Active Repository

- Local path: machine-specific; use the active clone's repository root
- GitHub repo: `https://github.com/goAuD/CoderLAP`
- Stable branch: `main`
- Integration branch: `dev`

## Current Project State

- `18` main topic folders complete
- `235` canonical Hungarian topic files complete as `README.md`
- `235` German translation sidecars complete as `README.de.md`
- metadata registry present:
  - `LAP_CONTENT_REGISTRY.json`
  - `LAP_CONTENT_REGISTRY.csv`
- static site generator working
- generated search index now includes bilingual topic-specific search terms
- curated alias groups support shorthand and cross-language search queries
- module-level print pack pages are generated for all `18` modules:
  - German at `/module-packs/<module-slug>/`
  - Hungarian at `/hu/module-packs/<module-slug>/`
- language routing working:
  - German default at `/`
  - Hungarian at `/hu/`
- legal pages exist for `de`, `hu`, and editorial fallback `en`
- registered domain: `coderlap.com`
- live delivery is active behind Cloudflare + Caddy
- Cloudflare proxy is enabled
- SSL/TLS mode is `Full (strict)`
- Caddy serves a Cloudflare Origin Certificate for `coderlap.com`
- temporary `basic_auth` protects the site during private rollout
- repo-facing docs are being kept safe for public visibility
- uptime/expiry monitoring now exists through `scripts/check_site_health.py`
  and `.github/workflows/coderlap-site-monitor.yml`
- Semgrep remains local; the prepared cloud workflow is intentionally excluded
  from this rollout (decision: 2026-09-11).
- `robots.txt` currently blocks indexing
- `.well-known/security.txt` is shipped from the repo

## Quiz Rollout: 2026-10-14

- CoderQuiz [v0.1.0](https://github.com/goAuD/CoderQuiz/releases/tag/v0.1.0)
  is deployed at `https://quiz.coderlap.com/` on the existing Debian/Caddy origin.
  Four packages contain 135 DE/HU questions covering 27 LAP topics.
- Temporary Basic Auth reuses the existing LAP access configuration. DNS,
  HTTPS, rejected missing/wrong credentials and all deployed artifact files were
  verified. No application accounts, result database or shared sign-in were added.
- LAP #45/#46 deployed the updated DE/HU/EN privacy and imprint pages plus
  configurable Quiz entry links. [Deployment verification](https://github.com/goAuD/CoderLAP/actions/runs/38546816683)
  passed 89 Python tests, 122 Node tests and the 512-page build; the updated
  Hungarian privacy page was also checked on the live site.
- `BuildSettings.quiz_url` remains empty. Automated production Quiz navigation
  hit Vivaldi `ERR_BLOCKED_BY_CLIENT`; manual sign-in has been requested.
  Complete authenticated production UI/mobile verification before setting
  `quiz_url` to `https://quiz.coderlap.com/` and deploying the LAP entry links.
- Coaster hosting and shared invitation login remain separate later tasks.
  Keep the central [roadmap](../plans/2026-09-30-learning-platform-roadmap.md)
  current; SkillDisplay still awaits the teacher's reply.

## Content Milestone: 2026-10-14

- All 235 topics in HU/DE were reviewed and expanded through
  [PR #42](https://github.com/goAuD/CoderLAP/pull/42), now merged into `dev`.
- Milestone: [v0.4.0-reviewed-content](../releases/release-notes-v0.4.0-reviewed-content.md).
  Its [GitHub Release](https://github.com/goAuD/CoderLAP/releases/tag/v0.4.0-reviewed-content)
  records the final deployed `main` commit and Actions verification. Verify that
  live record before treating a local branch or prepared release note as deployed.
- Content-PR CI passed 87 Python tests, 122 Node tests and the bilingual build.
  The milestone notes record the additional local checks and their limits.

## Previous Maintenance Delivery: 2026-10-14

- Markdown is updated to 3.11.1 through [PR #40](https://github.com/goAuD/CoderLAP/pull/40).
  Dependabot #39 was closed as superseded. [PR #41](https://github.com/goAuD/CoderLAP/pull/41)
  carried main back into dev.
- Production commit: `ae3f957a364d2c714323ff21362db9d917575a5d`.
  [Build and deployment](https://github.com/goAuD/CoderLAP/actions/runs/38526462950)
  succeeded with 83 Python and 35 Node tests and the bilingual build.
- This maintenance deployment preceded the larger October content milestone.
  Its commit and run above describe maintenance only.
- CoderQuiz documentation PR #14 and CoderCoaster documentation PR #5 were
  already merged. Their inspected local branches matched their remotes.

## Content Review: 2026-10-14

The completed content review covers all 235 topics in Hungarian and German, including
factual corrections, worked examples, self-check answers and primary sources.
The authoritative coverage and validation record is
[the content review](../plans/2026-10-14-content-review.md).

- Preserve topic IDs, the numbered tree, and bilingual routes.
- Marked console examples run directly from Markdown; SQL/PDO and framework
  examples have separate prerequisites and validation notes.
- The build hides editorial run markers. The registry counts numbered and
  bulleted source entries. The content checker includes the module 18 overview.
- The SV exercise validates malformed input without silently repairing it,
  clears stale QR results and keeps the QR quiet zone. It proves formal
  consistency only, not an actual insurance entitlement.
- Semgrep remains local. Do not stage the user's untracked cloud workflow.
- SkillDisplay waits for the teacher's reply. Quiz hosting is recorded above;
  shared authentication remains planned work. The next content batch belongs
  to CoderQuiz.

## Previous Frame Delivery: 2026-09-11

- The shared Műhely header/footer and local Lucide navigation icons are merged
  through PR #34 into `dev` and PR #35 into `main`.
- Deployed commit: `6d6343b6848713e0d559831e04a9eda34eb6ba97`.
  [Build and deployment](https://github.com/goAuD/CoderLAP/actions/runs/34623457337)
  succeeded with 83 Python and 35 JavaScript tests and the bilingual build.
- The refreshed production browser loaded the new `workshop-frame.css`;
  no horizontal overflow or console errors were observed.
- [Site monitoring](https://github.com/goAuD/CoderLAP/actions/runs/34623565032)
  passed DNS/TLS checks and received Cloudflare challenges on both hostnames.
  That monitor run did not exercise authenticated page access.
- The frame source is `site/assets/css/workshop-frame.css`; keep the Quiz and
  Coaster copies byte-identical. See the frame maintenance section in
  [architecture-adoption.md](architecture-adoption.md).
- CoderQuiz and CoderCoaster frame changes are approved and merged in their own
  repositories. Neither has a production hosting target yet. Hosting, DNS and
  shared sign-in remain separately planned work; do not infer
  that publishing source code has deployed either app.

## Previous Planning Checkpoint: 2026-09-30

The documentation PRs are now merged: LAP #36, Quiz #13, Coaster #4.
At that checkpoint, LAP `origin/dev` (`aa366ba`) differed from `origin/main`
(`6d6343b`) only in this handoff document; the website code was identical.
The October maintenance has since synchronized these branches.

The canonical cross-project order and acceptance checks are in
[the learning-platform roadmap](../plans/2026-09-30-learning-platform-roadmap.md).
Follow the dated current priority in that roadmap. SkillDisplay begins with
teacher questions and an active-skill mapping, without learner-data sync,
after the pending teacher feedback arrives.

## Read These First In A New Thread

1. `AGENTS.md`
2. `README.md`
3. `docs/project/deploy-strategy.md`
4. `docs/project/content-architecture.md`

Read only when relevant:

- `docs/project/architecture-adoption.md`
- `docs/project/private-rollout-access.md`
- `docs/project/access-hygiene-playbook.md`
- `docs/project/pre-public-checklist.md`
- `docs/project/public-repo-flip-checklist.md`
- `docs/project/github-security-settings-checklist.md`
- `docs/project/next-improvements-checklist.md`
- `docs/project/backup-restore-playbook.md`
- `docs/project/feedback-loop-playbook.md`
- `docs/project/uptime-expiry-monitoring.md`
- `docs/project/final-austrian-legal-review.md`
- `docs/project/github-release-hygiene.md`
- `docs/releases/README.md`
- `docs/releases/release-notes-v0.1.0-private-beta.1.md`
- `docs/releases/release-notes-v0.2.0-public-repo.1.md`
- `site/content/search/search_aliases.json`
- `docs/process/editorial-workflow.md`
- `docs/process/md013-cleanup-strategy.md`
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
node --test tests/*.test.cjs
python scripts/review_content.py
```

Local preview:

```powershell
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

If `8000` is busy or returns an empty response, retry with another free port
such as `8001` and use the matching URL.

## Most Likely Next Work

- follow the ordered [learning-platform roadmap](../plans/2026-09-30-learning-platform-roadmap.md)
  for the content review handoff, the next Quiz batch and later infrastructure work
- final Austrian legal/imprint pass before public launch
- switch `robots.txt` to an indexable version when `basic_auth` is removed
- optional MX/mail routing for `coderlap.com`
- GitHub repo metadata and private-beta release hygiene maintenance
- dedicated `MD013` cleanup in narrow batches, not mixed with feature work
- normal review/polish flow on `dev`, then merge to `main`

## Rules To Preserve

- keep the numbered German folder tree
- keep the PDF hierarchy as the structural source
- keep Hungarian `README.md` as canonical content
- keep German `README.de.md` as the translation sidecar
- keep Markdown as the authoring source of truth
- keep the delivery model static-first

## Deploy Notes Worth Remembering

- current Caddy `basic_auth` expects a `bcrypt` hash generated by
  `caddy hash-password --algorithm bcrypt`
- do not switch the site back to direct public origin mode while the Cloudflare
  Origin Certificate is active
- the stricter Caddy `client_auth` block for Cloudflare Authenticated Origin
  Pulls is not active at the moment
- GitHub monitoring secrets expected by the health-check workflow:
  - `CODERLAP_BASIC_AUTH_USER`
  - `CODERLAP_BASIC_AUTH_PASSWORD`
