# CoderLAP Pre-Public Checklist

Last updated: `2026-04-16`

Use this checklist before removing `basic_auth` or allowing unrestricted access
to `coderlap.com`.

## Legal

- [ ] Imprint reviewed against the actual publication model and Austrian
      disclosure obligations
- [ ] Privacy notice reviewed against the actual live stack, including
      Cloudflare, origin logs, and browser-side storage
- [ ] Direct electronic contact path decided and published if public access is
      planned
- [ ] Final decision made whether the current site qualifies for the reduced
      disclosure model or needs fuller media-law disclosure

## Access And Security

- [ ] `basic_auth` password rotated before wider rollout if the old password was
      shared broadly
- [ ] Cloudflare proxy still enabled
- [ ] SSL/TLS remains `Full (strict)`
- [ ] Origin certificate files and permissions checked
- [ ] Optional Cloudflare Authenticated Origin Pulls tested end to end before
      activation
- [ ] `security.txt` still points to the intended reporting channel

## Search And Indexing

- [ ] `robots.txt` reviewed for the intended visibility level
- [ ] `X-Robots-Tag` and any equivalent proxy/header rules checked
- [ ] Only switch to indexable mode after access policy and legal text are final

## Content And Translation

- [ ] Hungarian canonical content spot-checked in representative modules
- [ ] German live translations spot-checked against the Hungarian source
- [ ] Registry regenerated if metadata or structure changed
- [ ] Search and filter still behave correctly after the latest content changes

## Frontend And Print

- [ ] Mobile review completed on representative long-title topic pages
- [ ] Desktop review completed on homepage plus representative topic pages
- [ ] Print preview checked on at least 10 to 15 representative topics
- [ ] No obvious overflow, clipping, or broken pagination in the release
      candidate

## Repo And Release Hygiene

- [ ] Repository visibility and collaboration settings reviewed against
      [public-repo-flip-checklist.md](./public-repo-flip-checklist.md)
- [ ] Root README reflects the current live language model and deploy shape
- [ ] Deploy docs reflect the current Cloudflare + Caddy model
- [ ] GitHub repository description, topics, and first release tags are set when
      public-facing metadata matters
- [ ] `dev` and `main` are in the intended release state

## Go / No-Go Rule

If legal, access, or print review is still materially incomplete, keep the site
behind `basic_auth` and leave indexing disabled.
