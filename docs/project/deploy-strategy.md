# CoderLAP Deploy Strategy

Last updated: `2026-04-12`

## Current State

- Repository: `goAuD/CoderLAP`
- Stable branch: `main`
- Active branch: `dev`
- Static output: `dist/`
- Registered domain: `coderlap.com`
- Intended web server: `Caddy`
- Intended host shape: Debian + static files

The project is already in the right form for static deployment. The next phase is no longer “design deployment later”, but “deploy the existing static site cleanly”.

## Deployment Target

The deploy target should be the **generated static site**, not the raw working tree as a web root.

That means:

- build from the repository
- serve the generated `dist/` directory
- keep the Markdown corpus and scripts outside the public web root when possible

## Recommended Delivery Model

Use one clean path only:

```text
dev review -> merge to main -> build -> publish dist/ -> Caddy serves dist/
```

Do not mix multiple competing deploy paths.

## Recommended First Production Shape

```text
/srv/coderlap/
  repo/         # git checkout
  current/      # optional deployment symlink or active release dir
  dist/         # generated static output if separated
```

Two acceptable operational shapes:

### Option A: build in repo checkout on server

- pull `main`
- run `python scripts/build_site.py`
- point Caddy to the resulting `dist/`

### Option B: build elsewhere and sync `dist/`

- build locally or in CI
- upload/sync only `dist/`
- point Caddy to the synced static directory

For the first deployment, **Option A** is usually the simplest if the server already has Python installed.

## Caddy Direction

Recommended baseline:

```caddy
coderlap.com, www.coderlap.com {
    root * /srv/coderlap/repo/dist
    encode zstd gzip
    file_server
}
```

If temporary access protection is still desired during private rollout, add `basic_auth` here instead of building app-level auth.

## DNS Direction

The domain is registered at Dynadot.

Practical next step:

- point `coderlap.com` to the Debian host with the chosen A/AAAA records
- optionally point `www.coderlap.com` as well
- let Caddy handle certificate issuance after DNS resolves correctly

## Security Baseline

Keep the attack surface low:

- static hosting only
- no database
- no backend auth system
- no secrets committed to the repository
- optional temporary `basic_auth` during staged rollout

## Recommended Release Discipline

Use this sequence:

1. review and polish on `dev`
2. merge into `main`
3. build the site from `main`
4. verify output locally or on server
5. switch Caddy to the verified static output

## Commands

Local verification:

```powershell
python .\scripts\build_site.py
python -m unittest discover -s tests -v
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

## Immediate Next Deploy Tasks

1. final UI/content QA on `dev`
2. merge approved state into `main`
3. prepare Debian target path
4. configure Caddy for `coderlap.com`
5. point Dynadot DNS
6. verify live HTTPS delivery
