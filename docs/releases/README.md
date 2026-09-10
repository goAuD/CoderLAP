# CoderLAP Releases

Last updated: `2026-09-10`

This folder stores release-note source files that describe milestone states of
the repository and the live site.

The release docs are intentionally separate from `docs/project/` because they
are historical milestone records, not evergreen architecture or process notes.

## Current Files

- [release-notes-v0.3.0-workshop.1.md](./release-notes-v0.3.0-workshop.1.md)
- [release-notes-v0.1.0-private-beta.1.md](./release-notes-v0.1.0-private-beta.1.md)
- [release-notes-v0.2.0-public-repo.1.md](./release-notes-v0.2.0-public-repo.1.md)
- [release-notes-v0.2.1-maintenance.1.md](./release-notes-v0.2.1-maintenance.1.md)

## Naming Rule

Use release files when a milestone materially changes one or more of:

- repository visibility or collaboration model
- delivery/deploy state
- legal/access posture
- frontend/search/print capability at milestone level

Do not create a release doc for every minor polish commit.

## Release Sequence

1. Write the milestone notes here on a dedicated branch and merge through `dev`.
2. Promote `dev` to `main` through a release PR after CI passes.
3. Verify deployment and the protected production site.
4. Tag the deployed `main` commit and publish a GitHub Release using the same
   note file. Never move an existing release tag to a different commit.

The GitHub Release and its linked Actions runs record the final deployment
commit and verification results; the note file describes the versioned scope.
