# CoderLAP `v0.1.0-private-beta.1`

Release date: `2026-04-12`

## Release Intent

First stable private beta milestone for the bilingual static study platform.

This is not a public launch.

## Included State

- bilingual static site is live on `coderlap.com`
- German is the default language at `/`
- Hungarian is available at `/hu/`
- all `233` canonical Hungarian topic files exist
- all `233` German translation sidecars exist
- search, filter, topic navigation, language routing, and print views are
  working
- legal pages exist for `de`, `hu`, and editorial fallback `en`

## Delivery State

- Cloudflare proxy enabled
- SSL/TLS mode `Full (strict)`
- Caddy serves the site behind Cloudflare
- temporary `basic_auth` protects the private rollout
- `robots.txt` currently blocks indexing
- `.well-known/security.txt` is shipped from the repo

## Notable Quality Work

- static site generator and bilingual routing stabilized
- topic-page language switching keeps the active topic context
- topic action bar alignment and button behavior polished
- legal and privacy pages aligned with the actual deploy model
- editorial and private-rollout process docs added

## Known Follow-Ups

- optional Cloudflare Authenticated Origin Pull hardening
- final Austrian legal pass before broader sharing
- repo metadata and release hygiene to be kept in sync with live state
- separate `MD013` cleanup program for the Markdown corpus

## Audience

Restricted private use only.

Do not treat this tag as a public announcement marker.
