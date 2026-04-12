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
- Tailscale SSH access to the Debian host is available
- Debian deploy root prepared: `/srv/www/coderlap`
- Repo-scoped self-hosted runner registered and online: `debian-coderlap`

The project is already in the right form for static deployment. The next phase is no longer “design deployment later”, but “deploy the existing static site cleanly”.

## Deployment Target

The deploy target should be the **generated static site**, not the raw working tree as a web root.

That means:

- build from the repository
- serve the generated `dist/` directory
- keep the Markdown corpus and scripts outside the public web root when possible

## Current Delivery Model

Use one clean path only:

```text
dev review -> merge to main -> GitHub Actions build -> self-hosted deploy -> Caddy serves dist/
```

Do not mix multiple competing deploy paths.

## Current Server Target Shape

```text
/srv/www/coderlap/
  dist/
  dist.backup/
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

For CoderLAP, the current preferred path is:

- CI on GitHub-hosted runners
- deploy on a repo-scoped self-hosted runner on the Debian host
- local copy from workflow workspace into `/srv/www/coderlap/dist`
- let Caddy serve the promoted `dist/` directory once DNS and host config are ready

## GitHub Actions Deployment

Workflow file:

- `.github/workflows/coderlap-static-cicd.yml`

Deploy target:

- `/srv/www/coderlap/dist`

Runner expectation:

- labels include `self-hosted`, `Linux`, `X64`, `coderlap`
- current runner name: `debian-coderlap`
- current runner host path: `/home/goaud/actions-runner-coderlap`

Current deploy behavior:

- CI runs on `push` to `dev` and `main`, plus PRs into `main`
- deploy runs only on `push` to `main` or manual `workflow_dispatch`
- deploy promotes a staged release from `dist.incoming/` to `dist/`
- previous live release is kept temporarily as `dist.backup/`

## Caddy Direction

Recommended baseline:

```caddy
coderlap.com, www.coderlap.com {
    root * /srv/www/coderlap/dist
    encode zstd gzip
    file_server
}
```

If temporary access protection is still desired during private rollout, add `basic_auth` here instead of building app-level auth.

This block should only be enabled once:

- `coderlap.com` resolves to the correct origin
- the Caddy config can be edited with sudo on the server
- Cloudflare is in the intended DNS/proxy mode

Current blocker:

- the Debian host requires sudo for `/etc/caddy/Caddyfile`, and passwordless sudo is not available for the current SSH session

## DNS Direction

The domain is registered at Dynadot.

Practical next step:

- point `coderlap.com` to the Debian host with the chosen A/AAAA records
- optionally point `www.coderlap.com` as well
- let Caddy handle certificate issuance after DNS resolves correctly
- if Cloudflare proxy is enabled, use Full (strict) once the origin serves a valid certificate

Current blocker:

- `coderlap.com` is not yet resolving to the Debian origin, so live cutover should not be attempted yet

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
3. let GitHub Actions build and upload `dist`
4. let GitHub Actions sync `dist` to `/srv/www/coderlap/dist`
5. enable or update the Caddy site once DNS and sudo-side config are ready

## Commands

Local verification:

```powershell
python .\scripts\build_site.py
python -m unittest discover -s tests -v
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

## Immediate Next Deploy Tasks

1. commit and push the CI/CD workflow on `dev`
2. run a manual `workflow_dispatch` deploy to validate `/srv/www/coderlap/dist`
3. configure Caddy for `coderlap.com` once sudo access is available
4. point Cloudflare/DNS to the Debian origin
5. verify live HTTPS delivery
