# CoderLAP Next Improvements Checklist

Last updated: `2026-04-16`

This document tracks the next improvements that are still worth doing after the
static site, deploy path, and restricted-access production setup became stable.

The goal is not to add complexity for its own sake. The goal is to protect the
current system, make maintenance easier, and improve the parts that matter most
for teachers and students.

## Priority Order

1. ~~Backup and restore playbook~~ Done
2. ~~Access hygiene for the private rollout~~ Done
3. ~~Lightweight feedback loop for teachers and students~~ Done
4. ~~Search quality improvements~~ Done
5. ~~Module-level print packs~~ Done
6. ~~Simple uptime and expiry monitoring~~ Done
7. Final Austrian legal review before wider release

## 1. Backup And Restore Playbook

Why this matters:

- the project is already used by real teachers and students
- the deploy path is no longer disposable
- infra recovery should not depend on memory

What to capture:

- repository restore from GitHub
- `dev` / `main` release flow
- Debian paths and ownership expectations
- `/srv/www/coderlap/dist` deploy target
- `/etc/caddy/Caddyfile` restore steps
- Cloudflare essentials
- certificate and key file locations
- `basic_auth` rotation steps
- CrowdSec and Caddy logging checkpoints

Done when:

- a new machine or rebuilt server can be restored from the document alone
- the recovery steps have been tested at least once in a dry run

Current document:

- [backup-restore-playbook.md](./backup-restore-playbook.md)

## 2. Access Hygiene

Why this matters:

- the site is intentionally private for now
- shared access needs a clean reset path if the password leaks or spreads too
  far

What to add:

- who currently has access
- when the current password was issued
- when to rotate it
- how to generate a new `bcrypt` hash
- how to reload Caddy safely after password rotation

Done when:

- password rotation can be done in a few minutes without guesswork
- the reset steps are documented in one place

Current document:

- [access-hygiene-playbook.md](./access-hygiene-playbook.md)

## 3. Lightweight Feedback Loop

Why this matters:

- real users will find content errors, wording issues, and navigation friction
- small feedback is more valuable than a heavier backend feature

Good enough options:

- GitHub issue template
- dedicated feedback mail address later
- a simple “report issue” link from the site

Suggested categories:

- content error
- translation issue
- typo / wording
- print problem
- frontend / navigation issue

Done when:

- at least one low-friction reporting path exists
- feedback can be triaged without ad hoc chat history

Current document:

- [feedback-loop-playbook.md](./feedback-loop-playbook.md)

## 4. Search Quality Improvements

Why this matters:

- the corpus is already large
- better search is more useful than adding more UI features

Best next step:

- alias and synonym support across German and Hungarian terminology

Examples:

- `API` <-> `Schnittstelle`
- `Datentyp` <-> `adattípus`
- `Vererbung` <-> `öröklődés`
- common abbreviations and exam shorthand

Done when:

- representative cross-language and shorthand queries reliably find the intended
  topics

Current state:

- done via generated topic `search_terms`
- topic-specific headings from `README.md` and `README.de.md` are indexed
- curated alias groups cover common German, Hungarian, and shorthand terminology

## 5. Module-Level Print Packs

Why this matters:

- teachers may want grouped printable material
- the current per-topic print view is already useful, but not enough for some
  classroom workflows

Possible shape:

- one combined printable view per module
- or a simple generated “module pack” page using the existing static build

Done when:

- at least one module can be exported in a teacher-friendly printable format

Current state:

- done via generated module pack routes for all `18` main modules
- topic pages link directly to the current module pack
- sidebar groups expose the same print-pack entry point
- module pack pages keep the existing surface/button/layout language instead of
  introducing a separate visual pattern

## 6. Simple Uptime And Expiry Monitoring

Why this matters:

- silent infra drift is more dangerous than missing small frontend polish

Minimum useful checks:

- domain resolves
- Cloudflare edge responds
- `basic_auth` still protects the site
- authenticated request still returns the app
- origin certificate and domain expiry are not near failure

Done when:

- someone gets notified before the site silently fails or an expiry becomes
  urgent

Current state:

- done via `scripts/check_site_health.py`
- scheduled workflow: `.github/workflows/coderlap-site-monitor.yml`
- checks:
  - DNS resolve
  - unauthenticated `401`
  - authenticated `200`
  - Basic auth challenge
  - edge certificate lifetime

Current document:

- [uptime-expiry-monitoring.md](./uptime-expiry-monitoring.md)

## 7. Final Austrian Legal Review

Why this matters:

- the current legal texts are good working documents, but not the final public
  release sign-off
- once broader access matters, legal correctness becomes a release gate

Scope:

- imprint
- privacy notice
- access model
- logging model
- direct contact path
- media-law disclosure threshold

Done when:

- the legal texts are reviewed against the actual publication model in force at
  release time

Current review baseline:

- [final-austrian-legal-review.md](./final-austrian-legal-review.md)
- current result: acceptable working baseline for the restricted-access rollout
- still not a public-launch sign-off until the wider-release access model is
  frozen

## What Not To Add Right Now

These are intentionally out of scope unless requirements change:

- database
- user account system
- backend rewrite
- React rewrite
- custom admin panel
- AI assistant inside the site

Reason:

- they increase complexity faster than they increase value for the current
  school-focused use case

## Decision Rule

If a proposed improvement adds significant runtime or operational complexity,
the burden of proof is on that improvement. The current static architecture
should stay the default unless there is a clear, concrete benefit for actual
teachers or students.
