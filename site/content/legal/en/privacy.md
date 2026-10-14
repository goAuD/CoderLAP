# Privacy Policy

## Responsible context

- Scope: CoderLAP (`https://coderlap.com`) and CoderQuiz
  (`https://quiz.coderlap.com`)
- Controller for both services: Viktor Halupka, see the imprint
- Service type: static learning material and a practice quiz running in the
  browser for the Austrian LAP exam in software development and coding
- Current publication status: restricted access with temporary HTTP Basic Auth
- Responsible contact basis: see the imprint page and the public project profile

## What data processing can realistically happen right now

- Requests to the site can trigger technical connection data at Cloudflare and
  on the origin server, including IP address, timestamp, requested URL, user
  agent, and similar request metadata
- The browser sends HTTP Basic Auth credentials in HTTPS requests for access
  checks at web-server level. This does not create application user accounts.
  The browser may request a separate login for each web address; a shared
  sign-in system is not yet in place
- For CoderLAP, the browser can store a local progress entry under the key
  `coderlap_progress`
- That CoderLAP entry contains local topic progress state and a
  timestamp

## Local storage in CoderQuiz

CoderQuiz uses the browser's `localStorage` to remember the chosen language
and allow a practice session to be resumed:

- `cq-lang`: the selected interface language
- `cq-<bankId>-topics`: the topics selected for the particular question pack
- `cq-<bankId>-progress`: question IDs, revisions and order, the current
  question and screen, shuffled answer order, submitted answers, their
  evaluation, score and selected topics

`<bankId>` is the question pack's identifier. Each pack therefore has its own
local saved session. The application does not send these language preferences
or practice data to the server or external services. This is separate from the
technical request data listed above, generated when loading the site and its
question packs.

`coderlap.com` and `quiz.coderlap.com` are separate browser origins. Their
local storage is separate; there is no automatic progress synchronisation
between them or with other devices. Clearing the site data for
`quiz.coderlap.com` in the browser settings removes the saved language, topic
selection and practice session together. CoderLAP progress belongs to the
separate site data for `coderlap.com`.

## Features not currently provided

- no application user accounts
- no server-side database for learning results
- no public sign-up or contact forms on the published site
- no analytics or marketing tracking in the current default setup
- no comment or community feature inside the site itself

## Purposes and legal bases

- delivery, security, and abuse prevention of the website based on legitimate
  interests under Article 6(1)(f) GDPR
- access restriction for the private project phase also based on legitimate
  interests under Article 6(1)(f) GDPR
- browser-side storage for the chosen language, topic selection and resuming
  the requested learning or practice function

## Storage locations and recipients

- Cloudflare as the upstream proxy and security layer
- self-operated origin infrastructure with Caddy on Debian
- local browser storage on the visitor's device

## Storage period

- browser-side preferences and progress data have no set expiry; they can be
  removed by clearing the site's browser data
- restarting the quiz replaces the previous practice session; the application
  discards a saved session that is no longer compatible with updated questions
- technical proxy and server logs should only be kept as long as operationally
  required for delivery, abuse detection, or troubleshooting

## Your rights

- right to be informed
- right of access
- right to rectification
- right to erasure where applicable
- right to restriction of processing where applicable
- right to object where processing relies on legitimate interests
- right to lodge a complaint with the Austrian Data Protection Authority

## Complaint authority

- Austrian Data Protection Authority
- Barichgasse 40-42, 1030 Vienna, Austria
- `https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person`
- `https://dsb.gv.at/eingabe-an-die-dsb/beschwerde`

## Note on the current project phase

- This privacy policy is written for the current restricted-access rollout
  behind access control
- Before any unrestricted public launch, the contact path, retention details,
  and final legal classification should be reviewed again

## Sources

- MDN, "Window: localStorage property"
  https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
  For persistent local storage separated by browser origin.
- Caddy, "basic_auth"
  https://caddyserver.com/docs/caddyfile/directives/basic_auth
  For the operation of HTTP Basic Auth checks at web-server level.
- Austrian Data Protection Authority, "Ihre Rechte als betroffene Person"
  https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person Used for
  the Austrian framing of information duties and data-subject rights.
- Austrian Data Protection Authority, "Beschwerde"
  https://dsb.gv.at/eingabe-an-die-dsb/beschwerde Used for the current Austrian
  complaint path and complaint authority details.
- EUR-Lex, Regulation (EU) 2016/679 (GDPR)
  https://eur-lex.europa.eu/eli/reg/2016/679/oj Used for legal bases,
  information duties, and data-subject rights.
- RIS, Telecommunications Act 2021, Section 165
  https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40238623/NOR40238623.pdf
  Used for the Austrian legal baseline around storing or accessing information
  on end-user devices.
