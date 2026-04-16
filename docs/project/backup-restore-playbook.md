# CoderLAP Backup And Restore Playbook

Last updated: `2026-04-16`

This playbook documents how to recover the currently working CoderLAP setup
without relying on memory.

The target is the current restricted-access production shape:

- static bilingual site
- GitHub source of truth
- GitHub Actions build and deploy flow
- Debian host
- Caddy in front of `/srv/www/coderlap/dist`
- Cloudflare proxy with `Full (strict)`
- Caddy `basic_auth`
- CrowdSec monitoring Caddy access logs

## Recovery Goal

Restore the site to a state where all of the following are true:

- the repository can be built locally
- `main` can deploy through GitHub Actions
- the Debian host serves the generated static site
- `coderlap.com` resolves through Cloudflare
- `basic_auth` still protects the site
- CrowdSec sees Caddy access logs again

## Primary Sources Of Truth

Use these in this order:

1. GitHub repository: `goAuD/CoderLAP`
2. `README.md`
3. `AGENTS.md`
4. [deploy-strategy.md](./deploy-strategy.md)
5. [private-rollout-access.md](./private-rollout-access.md)
6. [next-thread-handoff.md](./next-thread-handoff.md)

## Recovery Scope

This document covers:

- repository restore
- local build verification
- GitHub Actions deploy path
- Debian file layout
- Caddy restore
- Cloudflare restore checkpoints
- `basic_auth` rotation
- CrowdSec recovery checks

It does not cover:

- reauthoring topic content from scratch
- changing the app architecture
- replacing Caddy or Cloudflare with another stack

## Known Good Current Shape

Repository:

- local working copy: `C:\GitHub\CoderLAP`
- stable branch: `main`
- active working branch: `dev`

Build:

- build entrypoint: `python scripts/build_site.py`
- test suite: `python -m unittest discover -s tests -v`
- generated output: `dist/`

GitHub Actions:

- workflow file: `.github/workflows/coderlap-static-cicd.yml`
- CI runner: `ubuntu-latest`
- deploy runner labels: `self-hosted`, `Linux`, `X64`, `coderlap`
- artifact name: `coderlap-dist`

Debian host:

- deploy root: `/srv/www/coderlap`
- live static output: `/srv/www/coderlap/dist`
- previous release backup: `/srv/www/coderlap/dist.backup`
- runner path: `/home/goaud/actions-runner-coderlap`

Caddy:

- config file: `/etc/caddy/Caddyfile`
- service: `caddy.service`
- origin certificate: `/etc/ssl/certs/cf-origin-coderlap.pem`
- origin key: `/etc/ssl/private/cf-origin-coderlap.key`

CrowdSec:

- access log: `/var/log/caddy/access.log`
- acquisition file: `/etc/crowdsec/acquis.d/setup.caddy.yaml`

## Step 1. Restore The Repository

On a new local machine:

```powershell
git clone https://github.com/goAuD/CoderLAP.git
cd CoderLAP
git checkout dev
pip install -r requirements.txt
```

Verify the expected structure exists:

- `README.md`
- `AGENTS.md`
- `.github/workflows/coderlap-static-cicd.yml`
- `scripts/build_site.py`
- `site/`
- `docs/project/`

## Step 2. Verify Local Build

Run in this order on Windows:

```powershell
python -m unittest discover -s tests -v
python scripts/build_site.py
```

Expected:

- all tests pass
- `dist/` is regenerated
- output includes:
  - `dist/index.html`
  - `dist/hu/index.html`
  - `dist/data/topic-index.json`
  - `dist/.well-known/security.txt`
  - `dist/robots.txt`

Optional local preview:

```powershell
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

If `8000` is busy or returns an empty response, retry with another free port
such as `8001`.

## Step 3. Verify GitHub Actions Path

The deploy chain is:

```text
dev review
-> merge to main
-> GitHub Actions build
-> self-hosted deploy
-> Caddy serves /srv/www/coderlap/dist
```

Workflow behavior:

- CI runs on `push` to `dev` and `main`
- deploy runs only on `push` to `main` or manual `workflow_dispatch`

The deploy job must:

- download artifact `coderlap-dist`
- stage into `/srv/www/coderlap/dist.incoming`
- rotate the current release into `/srv/www/coderlap/dist.backup`
- promote `dist.incoming` into `/srv/www/coderlap/dist`

If restore requires a manual deploy check:

1. confirm the self-hosted runner is online in GitHub
2. trigger the workflow manually from `main`
3. confirm the deployment summary points to `/srv/www/coderlap/dist`

## Step 4. Restore Debian File Layout

Expected server shape:

```text
/srv/www/coderlap/
  dist/
  dist.backup/
```

If the directories are missing:

```bash
sudo mkdir -p /srv/www/coderlap
sudo chown -R goaud:goaud /srv/www/coderlap
```

If the deploy runner exists but is stopped, check:

```bash
cd /home/goaud/actions-runner-coderlap
./svc.sh status
```

If the runner is missing entirely, it must be re-registered in GitHub with the
existing `coderlap` label set before deploy can work again.

## Step 5. Restore Caddy

The current live site depends on:

- `/etc/caddy/Caddyfile`
- `/etc/ssl/certs/cf-origin-coderlap.pem`
- `/etc/ssl/private/cf-origin-coderlap.key`

Minimum restore checkpoints:

1. `coderlap.com, www.coderlap.com` site block exists
2. `basic_auth` exists
3. origin cert and key paths exist
4. root points to `/srv/www/coderlap/dist`
5. access log writes to `/var/log/caddy/access.log`
6. security headers are present

After restoring or editing Caddy:

```bash
sudo caddy fmt --overwrite /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
sudo systemctl status caddy --no-pager -l
```

## Step 6. Restore Cloudflare Direction

The current model assumes:

- Cloudflare proxy enabled for `coderlap.com`
- Cloudflare proxy enabled for `www.coderlap.com`
- SSL/TLS mode `Full (strict)`

Important rule:

- do not switch the site back to direct public origin mode while the Cloudflare
  Origin Certificate is active

Recovery checkpoints in Cloudflare:

- `coderlap.com` record exists and is proxied
- `www` record exists and is proxied
- zone SSL/TLS is still `Full (strict)`
- basic caching or security features did not accidentally bypass auth behavior

## Step 7. Restore `basic_auth`

The shared password is intentionally not stored in the repository.

Current Caddy requirement:

- use `bcrypt`
- do not use `argon2id` with the current Caddy setup

Generate a replacement hash on Debian:

```bash
caddy hash-password --algorithm bcrypt
```

Replace the hash in the `coderlap` block, then:

```bash
sudo caddy fmt --overwrite /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
```

Verification:

```bash
curl -I https://coderlap.com
curl -I -u admin:'YOUR_PASSWORD' https://coderlap.com
```

Expected:

- without credentials: `401`
- with credentials: successful content response

## Step 8. Restore CrowdSec Visibility

Current expected files:

- access log: `/var/log/caddy/access.log`
- acquisition config: `/etc/crowdsec/acquis.d/setup.caddy.yaml`

Current expected acquisition content:

```yaml
filenames:
  - /var/log/caddy/access.log
labels:
  type: caddy
  format: json
```

If the access log is missing:

```bash
sudo touch /var/log/caddy/access.log
sudo chown caddy:caddy /var/log/caddy/access.log
sudo chmod 640 /var/log/caddy/access.log
sudo systemctl reload caddy
```

If CrowdSec was restored or acquisition changed:

```bash
sudo systemctl restart crowdsec
sudo cscli metrics
```

Healthy state indicators:

- `file:/var/log/caddy/access.log` appears under `Acquisition Metrics`
- lines are read and parsed
- `crowdsecurity/caddy-logs` appears under `Parser Metrics`
- local HTTP scenarios can pour lines to buckets

Important log nuance:

- `remote_ip` will often be a Cloudflare edge IP
- `client_ip` should represent the original visitor IP

## Step 9. End-To-End Recovery Verification

After repo, deploy, Caddy, Cloudflare, and CrowdSec restore, verify all of:

1. `main` deploys successfully through GitHub Actions
2. `https://coderlap.com` returns `401` without credentials
3. `https://coderlap.com` returns the app with valid credentials
4. homepage loads
5. one topic page loads
6. language switch still works
7. `/var/log/caddy/access.log` receives entries
8. `sudo cscli metrics` shows the Caddy access log acquisition

## Minimum Backup Inventory

These items should exist in at least one recoverable place:

- GitHub repository
- Cloudflare zone configuration
- origin certificate PEM
- origin key file
- current shared password or a planned rotation procedure
- `/etc/caddy/Caddyfile`
- Debian runner registration knowledge

The repository alone is not enough to restore the live system.

## Suggested Dry-Run Frequency

Minimum recommendation:

- after major infra changes
- before broader rollout beyond the current trusted group
- before removing `basic_auth`

## Failure Triage Rule

If recovery fails, narrow it down in this order:

1. local build
2. GitHub Actions artifact
3. deploy target directory
4. Caddy validity and service status
5. Cloudflare proxy and TLS mode
6. `basic_auth`
7. CrowdSec visibility

Do not change multiple layers at once during restore. Re-establish one layer,
verify it, then continue.
