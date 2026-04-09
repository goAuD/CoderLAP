# Security Policy

## Supported scope

`CoderLAP` is currently a Markdown-first content repository with a future static-site delivery path.

At this stage, the most relevant security areas are:

- repository access control
- secret handling
- deployment configuration
- static-site hosting configuration

## Reporting

If you discover a security issue:

- do not publish credentials, tokens, or server details in a public issue
- contact the maintainer privately first

Repository owner and code owner:

- `@goAuD`
- Viktor Halupka

## Expected practices

- keep the repository private until publication is intentionally decided
- do not commit secrets
- use GitHub secrets or deploy keys for automation later
- prefer one clean deployment path
- review Caddy configuration before exposure
