# Final Austrian Legal Review

Last updated: `2026-04-16`

## Scope

This document is the release-gate review for the current CoderLAP publication
model.

It is not a substitute for legal counsel. It is the maintainer checklist that
must be passed before wider public release.

## Current Publication Model Reviewed

Current live shape:

- static site
- Cloudflare proxy in front of origin
- Caddy on Debian as origin
- restricted access with `basic_auth`
- no user accounts
- no open public contact form on the site
- browser-side progress storage in `localStorage`
- server-side technical logs at Cloudflare, Caddy, and CrowdSec layers

## Review Result

### Current private rollout

For the current restricted-access rollout, the existing imprint and privacy
pages are a defensible working baseline.

### Before wider public release

The following points should be treated as release blockers until explicitly
re-checked against the final publication model:

1. A direct electronic contact path should appear explicitly in the imprint,
   not only the GitHub profile link.
2. The final privacy text should state the effective retention logic for access
   logs more concretely than “only as long as required”.
3. If the repository becomes public and the site starts linking to public issue
   intake, that feedback path should be reflected consistently in imprint and
   privacy wording.
4. If `basic_auth` is removed and the site becomes openly indexable, the final
   media-law classification and disclosure threshold should be checked again in
   the actual public shape.

## Release Checklist

### 1. Imprint / provider information

Check before wider release:

- named provider / media owner present
- direct contact email present and monitored
- project type and publication format still match the real service
- if the site is fully public, re-check the final wording against:
  - `§ 5 ECG`
  - `§ 24 MedienG`
  - `§ 25 MedienG`

### 2. Privacy notice

Check before wider release:

- Cloudflare remains named as part of the delivery/security path if still used
- origin/server logging remains described accurately
- local browser storage (`coderlap_progress`) remains described accurately
- rights and Austrian complaint path still point to the current DSB pages
- retention wording matches the actual log rotation / retention practice in
  force

### 3. Access model

Check before wider release:

- if `basic_auth` remains, the wording should still describe a restricted
  access model
- if `basic_auth` is removed, legal pages must be updated before the change
- if a public feedback channel is introduced, the site text should no longer
  describe maintainer-mediated private intake as the active path

### 4. Search/indexing state

Check before wider release:

- if `robots.txt` changes from blocked to indexable, that change should happen
  only after the legal pages are in their public-release wording
- if the site remains private, `robots.txt` may stay restrictive

### 5. Contact and accountability

Check before wider release:

- direct contact mailbox exists and is tested
- mailbox owner is defined
- response responsibility is clear for teacher/student legal or privacy
  questions

## Current Actionable Decision

Current decision:

- no urgent legal rewrite is required for the present restricted-access test
  rollout
- do not call the legal layer “final” once the site is opened wider without
  first re-checking the blockers above

## Primary Sources

- USP.gv.at, „Impressumspflicht gemäß § 24 Mediengesetz“
  https://www.usp.gv.at/themen/brancheninformationen/information-und-kommunikation/impressumspflicht-gemaess-para-24-mediengesetz.html
  Used for the Austrian imprint framework and the relation to the
  E-Commerce-Gesetz.
- USP.gv.at, „Offenlegungspflicht gemäß § 25 Mediengesetz“
  https://www.usp.gv.at/themen/brancheninformationen/information-und-kommunikation/offenlegungspflicht-gemaess-para-25-mediengesetz.html
  Used for the disclosure threshold and the distinction between imprint and
  media-law disclosure.
- RIS, E-Commerce-Gesetz, § 5
  https://www.ris.bka.gv.at/eli/bgbl/i/2001/152/P5/NOR40025801
  Used as the primary Austrian legal provision for provider information.
- Österreichische Datenschutzbehörde, „Ihre Rechte als betroffene Person“
  https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person
  Used for the current Austrian rights framing.
- Österreichische Datenschutzbehörde, „Beschwerde“
  https://dsb.gv.at/eingabe-an-die-dsb/beschwerde
  Used for the current Austrian complaint channel.
- EUR-Lex, Regulation (EU) 2016/679 (GDPR)
  https://eur-lex.europa.eu/eli/reg/2016/679/oj
  Used for legal bases, information duties, and data subject rights.
- RIS, Telekommunikationsgesetz 2021, § 165
  https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40238623/NOR40238623.pdf
  Used for the Austrian rule set around storing or reading information on end
  devices.

Opened: `2026-04-16`
