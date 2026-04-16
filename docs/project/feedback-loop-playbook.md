# CoderLAP Feedback Loop Playbook

Last updated: `2026-04-16`

This playbook defines how feedback should be collected and triaged during the
current restricted rollout and how that process should evolve once direct
GitHub issue intake is intentionally opened.

The goal is to keep feedback lightweight and useful. The goal is not to build a
backend system or add operational overhead that the project does not need.

## Current Reality

Right now:

- the site is live but access-restricted behind `basic_auth`
- the repository can be made public without changing the site access model
- GitHub issue templates already exist
- a public issue link from the site is not appropriate until open issue intake
  is intentionally enabled

This means the feedback loop should currently be maintainer-mediated, not
fully self-service.

## Current Feedback Model

During the private rollout, acceptable inbound channels are:

- direct messages from teachers or students
- classroom feedback passed through a teacher
- local notes gathered during testing sessions
- private maintainer triage into GitHub issues afterward

This is enough for the current stage.

## Why This Is Good Enough For Now

- the user group is still small
- the access model is intentionally restricted
- the site still does not need open issue intake
- the main risk is losing useful corrections, not scaling a support team

The point is to capture real feedback reliably without forcing a premature
public workflow.

## Existing GitHub Issue Templates

The repository already contains these templates:

- `.github/ISSUE_TEMPLATE/content-improvement.md`
- `.github/ISSUE_TEMPLATE/frontend-or-deploy.md`

These are the right backbone for the later public loop.

Recommended category mapping:

- content error -> `content-improvement.md`
- translation issue -> `content-improvement.md`
- typo / wording -> `content-improvement.md`
- print problem -> `frontend-or-deploy.md`
- frontend / navigation issue -> `frontend-or-deploy.md`
- deploy or infra regression -> `frontend-or-deploy.md`

## Current Operating Procedure

When a teacher or student reports something:

1. capture the feedback in a private channel
2. reduce it to one concrete issue
3. classify it as:
   - content
   - translation
   - typo / wording
   - print
   - frontend / navigation
   - deploy / infra
4. transcribe it into the appropriate GitHub issue template
5. link the affected topic, module, or page path

This keeps the issue tracker useful even if the repository visibility changes
before the site feedback model does.

## Minimal Triage Standard

Each feedback item should answer:

- what is wrong
- where it appears
- who reported it, if that context matters
- whether it blocks studying or is only a polish issue

Priority shortcut:

- `high`: content error, broken navigation, broken print, wrong translation in
  an exam-relevant concept
- `medium`: wording issue, layout bug, source-quality improvement
- `low`: cosmetic polish, non-blocking UI cleanup

## Repository Preparation For Public Opening

Before exposing GitHub issues directly from the site, make sure all of the
following are true:

- issue templates are in place
- blank issues are disabled unless intentionally allowed
- labels are clean and understandable
- the repo description and topics are ready for public visibility
- legal text no longer implies a private-only feedback model

The repository should be public because you want it public, not only because a
feedback link would be convenient.

## Site Integration Rule

Do not add a visible “report issue” or “feedback” link to the site until open
issue intake is intentionally enabled.

Once open issue intake is intentionally enabled, the preferred first
implementation is simple:

- one GitHub “report issue” link
- optionally pointing to the issue chooser
- no custom backend form

Do not build a dedicated feedback backend for this project unless the scope
changes materially.

## Open Issue Intake Model

Once direct GitHub issue intake is enabled, the target model becomes:

- public GitHub issues for structured feedback
- pull requests for direct fixes from advanced contributors
- optional direct contact path later if legal/public-operational needs require
  it

At that point, the site can safely expose a public feedback/report link.

## Legal And Communication Nuance

While the site rollout is still restricted and feedback remains
maintainer-mediated:

- the site should not claim that public issues or pull requests are already the
  active feedback channel
- the legal/imprint text should reflect the current restricted-access reality

Once direct GitHub issue intake is enabled:

- the imprint/privacy wording can be updated to mention the public repository
  workflow more directly

## Done Criteria

This improvement is complete when:

- the private rollout uses a consistent maintainer-mediated feedback flow
- the repo is ready for later direct GitHub issue intake
- the legal text no longer overstates the current feedback openness
- the next step to expose a public feedback link is obvious and low-risk

Related checklist:

- [public-repo-flip-checklist.md](./public-repo-flip-checklist.md)
