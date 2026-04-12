# CoderLAP GitHub Metadata and Release Hygiene

Last updated: `2026-04-12`

## Purpose

This document keeps the GitHub repository presentation and release discipline aligned with the actual project state.

It is intentionally separate from deployment and content architecture notes.

## Current Repository Positioning

CoderLAP is currently:

- a private repository
- a live but access-restricted study platform on `coderlap.com`
- a bilingual static site with German as the public default and Hungarian as the canonical authoring source

This means the GitHub metadata should describe the project as already built and deployed, not as a future frontend idea.

## Repository Metadata Baseline

Recommended repository description:

> Bilingual Austrian LAP study base for Applikationsentwicklung - Coding: German-first static site, Hungarian canonical Markdown source, explicit primary sources.

Recommended homepage:

- `https://coderlap.com`

Recommended topic set:

- `austrian-lap`
- `applikationsentwicklung`
- `coding`
- `software-development`
- `exam-prep`
- `study-material`
- `bilingual`
- `german`
- `hungarian`
- `markdown`
- `static-site`
- `jinja2`
- `i18n`

The topic set should stay concise and descriptive. Avoid topic churn unless the project direction changes materially.

## Release Intent

The release list should communicate project maturity, not marketing hype.

Use releases for milestone checkpoints, not for every content typo or UI polish commit.

## Recommended Versioning Track

Use private rollout milestones first:

- `v0.1.0-private-beta.1`
  first stable private bilingual rollout behind `basic_auth`
- `v0.2.0-reviewed-content`
  content, translation, and legal review materially improved
- `v1.0.0-public`
  unrestricted public release candidate or public launch

The exact patch numbers can move, but the semantics should stay obvious.

## What Belongs In Release Notes

Include:

- language-routing state
- deploy state
- legal/privacy state if relevant
- notable frontend or search improvements
- known follow-up items that still block broader rollout

Avoid:

- giant changelog dumps
- cosmetic-only bullet spam
- pretending a private beta is a public launch

## Branch Discipline

- `dev` remains the working branch
- `main` remains the release branch
- release tags should point at `main`, not `dev`

Even if the repo owner bypasses branch protection in a private repo, the release story should still treat `main` as the stable milestone line.

## Immediate Hygiene Rule

Whenever the live delivery model changes materially, check all three:

1. GitHub description/homepage/topics
2. deploy/legal docs in `docs/project/`
3. the next release milestone notes
