# CoderLAP `v0.2.0-public-repo.1`

Release date: `2026-04-16`

## Release Intent

Public repository opening milestone for CoderLAP.

This release means the repository is ready for public visibility. It does
**not** mean the site itself is already in unrestricted public-launch mode.

## Included State

- bilingual static study site live at `coderlap.com`
- German default at `/`, Hungarian at `/hu/`
- `235` registered topic documents maintained from Hungarian canonical Markdown
- `235` German translation sidecars present
- generated bilingual search terms with curated alias support
- module-level print packs for all `18` modules
- legal pages for `de`, `hu`, and editorial fallback `en`
- uptime and expiry monitoring active through GitHub Actions

## Repository State

- root repo files reviewed for public visibility
- architecture and continuity docs aligned with the real live state
- release notes organized under `docs/releases/`
- issue templates and pull-request template already in place
- `CODE_OF_CONDUCT.md` added for public collaboration baseline

## Delivery State

- Cloudflare proxy enabled
- SSL/TLS mode `Full (strict)`
- Caddy serves the site behind Cloudflare
- temporary `basic_auth` still protects the live site
- `robots.txt` still blocks indexing
- `.well-known/security.txt` is shipped from the repo

## What This Release Does Not Mean

- not an unrestricted public site launch
- not a removal of `basic_auth`
- not an indexable/search-engine-ready release
- not the final Austrian legal sign-off for open public access

## Immediate Follow-Ups

- flip the repository visibility to public
- decide whether GitHub Discussions should stay off or be enabled later
- keep direct site-side feedback links disabled until that workflow is wanted
- complete the final Austrian legal/imprint pass before wider site access
- switch `robots.txt` and site access policy only when the rollout model changes
