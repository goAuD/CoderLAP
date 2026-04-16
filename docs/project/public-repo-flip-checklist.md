# CoderLAP Public Repo Flip Checklist

Last updated: `2026-04-16`

Use this checklist when the GitHub repository is about to be switched from
private to public visibility.

This checklist is about the repository. It is **not** the same as the wider
site-launch checklist for `coderlap.com`.

## Target State

The recommended first public state is:

- GitHub repository: public
- live site: still access-restricted behind `basic_auth`
- indexing: still blocked
- issue templates: enabled
- direct site-side feedback link: still optional, not automatic

This keeps the code and docs visible without forcing an immediate public site
launch.

## Root Repo Files

Before flipping visibility, confirm these root files are present and current:

- [README.md](../../README.md)
- [LICENSE](../../LICENSE)
- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [SECURITY.md](../../SECURITY.md)
- [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md)
- [AGENTS.md](../../AGENTS.md)

Also confirm:

- `.github/CODEOWNERS` exists
- `.github/PULL_REQUEST_TEMPLATE.md` exists
- `.github/ISSUE_TEMPLATE/` contains the intended issue types

## GitHub Settings

Recommended first-pass settings:

- visibility: public
- default branch: `main`
- issues: enabled
- discussions: optional, leave disabled unless you want community conversation
- wiki: optional, usually unnecessary here
- projects: optional
- pages: not needed because deployment is already external

Reasoning:

- issues are useful immediately for structured corrections
- discussions are only useful if you want open-ended community conversation
- this repo does not need GitHub Pages because delivery already happens through
  Cloudflare + Caddy

## Metadata

Confirm these are set before visibility changes:

- repository description
- homepage URL
- concise topic list

Current intended metadata baseline is documented in:

- [github-release-hygiene.md](./github-release-hygiene.md)

## Release And Tag

Before or immediately after the visibility flip:

- create or publish the intended milestone release
- make sure the release note matches the real state
- keep `main` as the tag target

Recommended milestone for the repo-public step:

- `v0.2.0-public-repo.1`

Meaning:

- repository is public
- site may still remain behind `basic_auth`
- this is not yet the unrestricted public site launch

Release note drafts live under:

- [../releases/README.md](../releases/README.md)

## Feedback Intake Decision

Decide explicitly whether public visibility also means public issue intake from
the site.

Safe default:

- make the repo public
- keep issue templates ready
- do **not** expose a visible site-side “report issue” link until you want that
  workflow

This avoids forcing the classroom/site workflow to change on the same day as
the repo visibility flip.

Related doc:

- [feedback-loop-playbook.md](./feedback-loop-playbook.md)

## Site Separation Rule

Do not confuse these two events:

1. repository becomes public
2. site becomes broadly public

They can happen at different times.

The repository can be public while the site still uses:

- `basic_auth`
- restrictive `robots.txt`
- maintainer-mediated feedback intake

## Done Criteria

This checklist is complete when:

- the repository can be viewed publicly without stale or misleading docs
- basic governance files are present
- release/tag naming is decided
- issue/discussion policy is deliberate
- the repo flip does not accidentally imply a public site launch
