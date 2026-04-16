# CoderLAP GitHub Security Settings Checklist

Last updated: `2026-04-16`

Use this checklist when the repository becomes public or whenever the GitHub
security posture is reviewed.

This checklist is about GitHub-side controls. It does not replace the site
deploy/security docs for Cloudflare, Caddy, or Debian.

## Baseline Goal

The recommended baseline is:

- public repository
- restricted live site behind `basic_auth`
- GitHub issues enabled
- minimal secrets footprint
- least-privilege Actions settings
- dependency and secret visibility enabled

## GitHub Security Tab

Recommended settings to enable:

- Dependency graph: `On`
- Dependabot alerts: `On`
- Dependabot security updates: `On`
- Secret scanning alerts: `On`, if available for the repo plan
- Push protection for secrets: `On`, if available for the repo plan
- Private vulnerability reporting: `On`

Reasoning:

- dependency visibility matters immediately in a public repo
- secret scanning is high-value and low-maintenance
- private vulnerability reporting fits the current `SECURITY.md` model

## Dependabot Baseline

Dependabot config now exists here:

- [../../.github/dependabot.yml](../../.github/dependabot.yml)

Current update scope:

- Python dependencies from `requirements.txt`
- GitHub Actions workflow dependencies

Recommended behavior:

- keep weekly updates enabled
- merge low-risk dependency bumps deliberately, not blindly
- review Actions bumps for permission or runner-behavior changes

## Actions Settings

Recommended baseline:

- Actions enabled
- allow GitHub-authored and verified actions
- keep default workflow permissions at `read repository contents`
- require approval for first-time external contributors if that setting is
  available in your plan

Reasoning:

- the repo already uses official Actions
- there is no reason to grant broader default token rights
- first-time approval reduces abuse risk in a public repo

## Self-Hosted Runner Rule

This repository already has a self-hosted deploy runner in the delivery chain.

That means:

- do not treat public workflow changes casually
- do not merge unreviewed workflow edits into `main`
- keep deploy logic restricted to trusted events only
- keep secrets out of PR-triggered jobs

Current good signs already present:

- CI runs on GitHub-hosted Ubuntu
- deploy uses the self-hosted runner only on trusted events
- workflow permissions are already `contents: read`

Still recommended:

- keep the runner attached only where it is needed
- avoid adding broad custom labels unless necessary
- review any future `workflow_dispatch`, `pull_request_target`, or secret-using
  job carefully

## Branch Protection

Recommended minimum once the repo is public:

- protect `main`
- require the main CI workflow to pass before merge
- block force-pushes
- block deletion of the protected branch

Nice-to-have later:

- require pull requests for all changes to `main`
- require at least one review when collaborators become active
- dismiss stale approvals on new commits

It is acceptable to keep owner bypass temporarily if you are still operating as
the sole maintainer, but that should be a conscious choice.

## Secrets Discipline

Keep only the secrets you actually need.

Current expected secrets include:

- `CODERLAP_BASIC_AUTH_USER`
- `CODERLAP_BASIC_AUTH_PASSWORD`

Rules:

- rotate when the site password rotates
- do not duplicate secrets across unnecessary scopes
- do not keep historical or unused values around

## Discussions And Community Surface

Safe default:

- Issues: `On`
- Discussions: `Off`

Turn Discussions on only if you want open-ended public conversation. For
CoderLAP, that is optional and not required for the current school-focused use
case.

## Current Review Trigger

Re-check this checklist when any of the following changes:

- repo visibility
- branch protection model
- self-hosted runner usage
- secret set
- Actions permission model
- site access policy

## Related Docs

- [public-repo-flip-checklist.md](./public-repo-flip-checklist.md)
- [github-release-hygiene.md](./github-release-hygiene.md)
- [deploy-strategy.md](./deploy-strategy.md)
- [SECURITY.md](../../SECURITY.md)
