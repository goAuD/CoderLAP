# CoderLAP Private Rollout Access Model

Last updated: `2026-04-12`

## Current Goal

CoderLAP is intentionally not open to the general public yet.

The project is already live on `coderlap.com`, but access is deliberately
limited to a small trusted group during the current review phase.

## Current Access Model

- Cloudflare proxy enabled
- SSL/TLS mode `Full (strict)`
- origin protected by a Cloudflare Origin Certificate in Caddy
- access gate implemented with Caddy `basic_auth`
- indexing blocked with `robots.txt`

This is acceptable for a small private rollout because it keeps the stack static
and avoids introducing a backend user system.

## Operational Rules

- Keep the shared password out of the repository.
- Distribute the password only out of band.
- Rotate the password when the trusted access group changes.
- Rotate the password immediately if it is forwarded beyond the intended group.
- Keep `basic_auth` enabled until legal text, content QA, and launch readiness
  are explicitly approved.

## Current Security Tradeoff

Strengths:

- low attack surface
- no application accounts
- no password database
- no session store
- fast to rotate

Limitations:

- one shared password is not individually revocable
- access cannot be attributed to individual users
- once the password spreads, containment requires full rotation

## Recommended Next Step If Access Needs Grow

If the user group becomes larger than a small trusted circle, prefer one of
these before building any app backend:

1. Cloudflare Access with identity-based access control
2. a new rotated shared password for a distinct cohort
3. Caddy-side per-user credentials only if absolutely necessary and still
   manageable

Do not build a custom auth backend unless the project scope changes materially.

## Conditions For Public Opening

Before removing `basic_auth`, complete all of the following:

- final Austrian legal/imprint review
- privacy text aligned with the actual live stack
- search/indexing decision made explicitly
- `robots.txt` updated accordingly
- public launch checklist signed off
