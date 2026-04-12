# Privacy Policy

## Responsible context

- Project name: CoderLAP
- Service type: static educational website for the Austrian LAP exam in software development and coding
- Current publication status: restricted access behind `basic_auth`
- Responsible contact basis: see the imprint page and the public project profile

## What data processing can realistically happen right now

- Requests to the site can trigger technical connection data at Cloudflare and on the origin server, including IP address, timestamp, requested URL, user agent, and similar request metadata
- The current `basic_auth` gate processes submitted credentials only for comparison at web-server level; it does not create in-site user accounts
- The browser can store a local progress entry under the key `coderlap_progress`
- That browser-side storage contains only local topic progress state and a timestamp

## What is not currently planned

- no application user accounts
- no public sign-up or contact forms on the published site
- no analytics or marketing tracking in the current default setup
- no comment or community feature inside the site itself

## Purposes and legal bases

- delivery, security, and abuse prevention of the website based on legitimate interests under Article 6(1)(f) GDPR
- access restriction for the private project phase also based on legitimate interests under Article 6(1)(f) GDPR
- browser-side progress storage only for the requested study-progress function of the site

## Storage locations and recipients

- Cloudflare as the upstream proxy and security layer
- self-operated origin infrastructure with Caddy on Debian
- local browser storage on the visitor's device

## Storage period

- browser-side progress data stays on the device until the user clears it or removes site data in the browser
- technical proxy and server logs should only be kept as long as operationally required for delivery, abuse detection, or troubleshooting

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

- This privacy policy is written for the current restricted-access rollout behind access control
- Before any unrestricted public launch, the contact path, retention details, and final legal classification should be reviewed again

## Sources

- Austrian Data Protection Authority, "Ihre Rechte als betroffene Person"
  https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person
  Used for the Austrian framing of information duties and data-subject rights.
- Austrian Data Protection Authority, "Beschwerde"
  https://dsb.gv.at/eingabe-an-die-dsb/beschwerde
  Used for the current Austrian complaint path and complaint authority details.
- EUR-Lex, Regulation (EU) 2016/679 (GDPR)
  https://eur-lex.europa.eu/eli/reg/2016/679/oj
  Used for legal bases, information duties, and data-subject rights.
- RIS, Telecommunications Act 2021, Section 165
  https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40238623/NOR40238623.pdf
  Used for the Austrian legal baseline around storing or accessing information on end-user devices.
