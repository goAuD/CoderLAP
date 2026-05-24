# CoderLAP `v0.2.1-maintenance.1`

Release date: `2026-05-24`

## Release Intent

Operational maintenance and hardening checkpoint for CoderLAP.

This release is not a new public-launch milestone. It exists to stabilize the
delivery pipeline, align the live monitoring logic with the current Cloudflare
edge behavior, and clear repository-side security noise before the next larger
content or rollout milestone.

## Included State

- bilingual static study site remains live at `coderlap.com`
- German default at `/`, Hungarian secondary at `/hu/`
- static build and deploy flow revalidated on both `dev` and `main`
- daily site monitor aligned with the current Cloudflare protected-edge setup
- CodeQL findings cleared for the JavaScript and Python monitor paths
- repository ignore rules tightened for local-only runtime and tooling artifacts

## Security And Operations

- site monitor now accepts the real protected-edge response shape used by
  Cloudflare for automated traffic
- TLS checks in the monitor now explicitly require modern protocol minimums
- client-side internal link building was hardened to avoid unsafe slug/path use
- registry loader now validates slug format more strictly before build-time use
- no open CodeQL alerts remain after the release validation pass

## Delivery State

- `main` still represents the stable release line
- `main` push CI/CD passed and deploy promotion completed
- manual monitor run from GitHub Actions passed after the monitor fix
- `dev` and `main` were resynchronized after release preparation

## Repository Hygiene

- `.gitignore` now covers additional local Python, coverage, cache, log, and
  environment noise that should not be published to GitHub
- release notes remain stored under `docs/releases/` as historical milestone
  records

## What This Release Does Not Mean

- not a new public rollout phase
- not a removal of `basic_auth`
- not a search-indexing or SEO launch change
- not the next major content-review milestone

## Immediate Follow-Ups

- keep the monitor logic in sync if the Cloudflare protection mode changes again
- consider a dedicated allowlisted health endpoint if origin-level checks become
  more important than edge-only verification
- use the next release milestone for material content, legal, or rollout
  changes rather than routine maintenance
