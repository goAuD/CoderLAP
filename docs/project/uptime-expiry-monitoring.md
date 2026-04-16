# CoderLAP Uptime And Expiry Monitoring

Last updated: `2026-04-16`

## Purpose

This monitoring layer is intentionally small.

The goal is not full observability. The goal is to catch the failures that
would silently break the private rollout:

- DNS drift
- Cloudflare edge reachability problems
- broken `basic_auth`
- a dead app behind successful TLS
- edge certificate expiry getting too close

## Current Monitoring Shape

Repository assets:

- workflow: `.github/workflows/coderlap-site-monitor.yml`
- script: `scripts/check_site_health.py`

The workflow runs:

- manually via `workflow_dispatch`
- daily on schedule

The script checks:

1. `coderlap.com` DNS resolves
2. `www.coderlap.com` DNS resolves
3. edge TLS answers and the presented certificate is not near expiry
4. unauthenticated request returns `401`
5. `WWW-Authenticate` still advertises Basic auth
6. authenticated request returns `200`
7. authenticated body still contains the expected `CoderLAP` token

## Required GitHub Secrets

The workflow expects these repository secrets:

- `CODERLAP_BASIC_AUTH_USER`
- `CODERLAP_BASIC_AUTH_PASSWORD`

These should match the currently active Caddy `basic_auth` credentials.

## Manual Run

Local/manual invocation:

```powershell
$env:CODERLAP_BASIC_AUTH_USER="admin"
$env:CODERLAP_BASIC_AUTH_PASSWORD="your-current-password"
python .\scripts\check_site_health.py `
  --base-url https://coderlap.com `
  --www-url https://www.coderlap.com `
  --min-cert-days 21
```

The script exits non-zero on any failed check.

## Operational Notes

- The TLS expiry check sees the certificate that the public client sees.
  Because `coderlap.com` is proxied through Cloudflare, this means the
  Cloudflare edge certificate, not the private origin certificate on Debian.
- The authenticated check is intentionally simple. It is there to distinguish
  “TLS works” from “the actual app shell still loads behind auth”.
- If `basic_auth` is removed later for public launch, the script should be
  updated instead of disabled.

## Thresholds

Current defaults:

- timeout: `10` seconds
- minimum certificate lifetime: `21` days
- expected authenticated token: `CoderLAP`

These defaults are conservative enough for the current setup without creating
false urgency.

## Failure Handling

When the monitor fails:

1. confirm whether the failure is DNS, TLS, auth, or app response
2. check the latest Cloudflare DNS/proxy state
3. check Caddy on Debian
4. if auth failed, verify the current Caddy hash and the secret values in
   GitHub
5. rerun the workflow manually after the fix

## Completion Status

This checklist item is considered done because:

- the monitor exists in the repository
- it is runnable manually
- it is schedulable through GitHub Actions
- it checks the current restricted-access production shape rather than an old
  pre-launch assumption
