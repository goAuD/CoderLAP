# CoderLAP Deploy Strategy

Last updated: `2026-04-12`

## Current State

- Repository: `goAuD/CoderLAP`
- Stable branch: `main`
- Active branch: `dev`
- Static output: `dist/`
- Registered domain: `coderlap.com`
- Active web server: `Caddy`
- Active host shape: Debian + static files
- Tailscale SSH access to the Debian host is available
- Debian deploy root prepared: `/srv/www/coderlap`
- Repo-scoped self-hosted runner registered and online: `debian-coderlap`
- Production DNS is now managed through Cloudflare
- Cloudflare proxy is enabled for `coderlap.com` and `www.coderlap.com`
- SSL/TLS mode is `Full (strict)`
- Caddy currently serves the static site through a Cloudflare Origin Certificate
- Temporary `basic_auth` is enabled for restricted access during private rollout
- `robots.txt` and `.well-known/security.txt` are generated from the repository
  and shipped with the static build

The project is already deployed in a restricted-access production shape. The
next phase is no longer first deployment, but controlled hardening and
public-launch preparation.

## Deployment Target

The deploy target should be the **generated static site**, not the raw working
tree as a web root.

That means:

- build from the repository
- serve the generated `dist/` directory
- keep the Markdown corpus and scripts outside the public web root when possible

## Current Delivery Model

Use one clean path only:

```text
dev review
-> merge to main
-> GitHub Actions build
-> self-hosted deploy
-> Caddy serves dist/
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
- let Caddy serve the promoted `dist/` directory behind Cloudflare

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

Current live shape:

```caddy
coderlap.com, www.coderlap.com {
    basic_auth {
        admin <bcrypt_hash>
    }

    tls /etc/ssl/certs/cf-origin-coderlap.pem /etc/ssl/private/cf-origin-coderlap.key

    root * /srv/www/coderlap/dist
    encode zstd gzip
    file_server
}
```

Operational notes:

- `basic_auth` is intentionally kept at the Caddy layer during private rollout
- use `caddy hash-password --algorithm bcrypt` for future password rotation
- do not use `argon2id` hashes with the current Caddy `basic_auth` setup
- the stricter `client_auth` block for Cloudflare Authenticated Origin Pulls is
  intentionally not active right now
- if Authenticated Origin Pulls is enabled later in Cloudflare, the matching
  `client_auth` block can be restored in Caddy after explicit verification

## DNS Direction

The domain is registered at Dynadot, with nameservers delegated to Cloudflare.

Current DNS shape:

- proxied `A` record for `coderlap.com`
- proxied `CNAME` record for `www.coderlap.com`
- edge TLS handled by Cloudflare
- origin TLS handled by the Cloudflare Origin Certificate in Caddy

Deferred DNS tasks:

- optional MX/mail routing later
- optional final DNS cleanup once public launch requirements are frozen

## Security Baseline

Keep the attack surface low:

- static hosting only
- no database
- no backend auth system
- no secrets committed to the repository
- temporary `basic_auth` during staged rollout
- Cloudflare proxy in front of origin
- `Full (strict)` between Cloudflare and origin
- Caddy-level security headers
- Cloudflare Bot Fight Mode enabled
- `robots.txt` currently blocks indexing during private rollout

## Recommended Release Discipline

Use this sequence:

1. review and polish on `dev`
2. merge into `main`
3. let GitHub Actions build and upload `dist`
4. let GitHub Actions sync `dist` to `/srv/www/coderlap/dist`
5. let Caddy continue serving the updated static release behind Cloudflare

## Commands

Local verification:

```powershell
python .\scripts\build_site.py
python -m unittest discover -s tests -v
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

If `8000` is unavailable locally or returns an empty response, choose another
free port such as `8001` and adjust the URL used for manual verification.

## Current Hardening And Launch Follow-ups

1. Re-introduce Cloudflare Authenticated Origin Pulls only after explicit
   end-to-end verification.
2. Keep the site health workflow wired with current `basic_auth` secrets:
   - `CODERLAP_BASIC_AUTH_USER`
   - `CODERLAP_BASIC_AUTH_PASSWORD`
3. Do one final Austrian legal/imprint review before removing `basic_auth` for
   public access.
4. Replace the restrictive `robots.txt` with an indexable version once the site
   is ready for search engines.
5. Add MX/mail routing later if the domain should receive operational or contact
   email.

Related documents:

- [private-rollout-access.md](./private-rollout-access.md)
- [pre-public-checklist.md](./pre-public-checklist.md)
- [uptime-expiry-monitoring.md](./uptime-expiry-monitoring.md)
- [final-austrian-legal-review.md](./final-austrian-legal-review.md)
