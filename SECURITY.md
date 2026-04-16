# Security Policy

## Supported scope

`CoderLAP` is currently a Markdown-first content repository with a live static
site delivered behind Cloudflare + Caddy.

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

- do not commit secrets
- do not paste credentials, hashes, or server-only details into issues,
  screenshots, or docs
- keep GitHub secrets and deploy credentials current for automation
- keep Dependabot, dependency visibility, and repository security features on
  when the repo is public
- treat repository visibility and site access control as separate decisions
- prefer one clean deployment path
- review Caddy and Cloudflare configuration before wider exposure
