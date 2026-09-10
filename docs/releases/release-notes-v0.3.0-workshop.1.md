# CoderLAP `v0.3.0-workshop.1`

Release date: `2026-09-10`

## Release Intent

The Workshop (Műhely) design brings a shared visual style to the existing
bilingual LAP study site. German remains at `/`, Hungarian at `/hu/`, with
235 topics and the existing locally stored learning progress.

## Changes

- Shared blue brand icon and favicon, consistent colors, spacing and progress
  pill, and clearer homepage and topic layouts.
- Mobile navigation alignment and an iPhone sticky-header scrolling fix.
- Subtle, one-time section reveals that respect reduced-motion preferences.
- Quick-view skeletons during real loading, with localized errors and retry.
- CoderQuiz and CoderCoaster introductions with development status, available
  from the homepage and individual footer links. App destinations follow later.
- Footer groups for tools and legal links, plus GitHub. Development status
  stays below each project name, and the floating button has reserved space.
- Central safe-area spacing for iPhone layouts and a calmer homepage title:
  “Schritt für Schritt zur LAP.”

Implemented in PRs #11–#16. The earlier design prototypes #9–#10 are separate
from this release.

## Validation

- 80 Python tests, 8 JavaScript interaction tests, and the bilingual static build
  passed during release preparation.
- Browser geometry checked at 320px, 390px, 844px landscape and 1440px, including
  simulated nonzero safe-area insets. No horizontal document overflow or footer
  link overlap with the floating button was found in these checks.
- Project links, privacy navigation and sticky-header anchor clearance checked.
- The iPhone scrolling fix was confirmed on a physical device in preview.
- The final footer status alignment was rebuilt and checked in landscape.

Simulated safe-area checks do not replace a physical iPhone portrait/landscape
check of the final release. Screenshot capture was unavailable during the
automated browser checks; those results describe geometry and interaction.

## Access And Delivery

The site remains behind Caddy Basic Auth and Cloudflare. This release adds no
tracking, production dependencies, authentication changes or indexing changes.
It does not make the upcoming apps available or open the site to public access.

Delivery uses the existing `main` push workflow and Debian runner. The previous
live files are retained as `/srv/www/coderlap/dist.backup` until the next deploy.
The release tag identifies the deployed `main` commit. The GitHub Release links
the production deployment and post-deploy monitor runs.

## Recovery And Follow-Up

- For recovery, use the [backup and restore playbook](../project/backup-restore-playbook.md).
  The production commit before this rollout is
  `260be4315cd2fee3145d080603ed758ae1e4f600`; the existing deploy workflow can be
  run manually at a temporary recovery branch referencing that commit if needed.
- Check the final footer and safe areas on a physical iPhone in both orientations.
- Replace the upcoming-app introduction links only when each app and its access
  protection are ready.
