# CoderLAP Access Hygiene Playbook

Last updated: `2026-04-16`

This playbook defines how to operate the current restricted-access model
without drifting into ad hoc password sharing.

The current goal is not “perfect identity management.” The goal is to keep the
existing Caddy `basic_auth` setup safe enough for a small trusted circle until
the project is ready for wider release.

## Current Access Model

The current live model is:

- Cloudflare proxy enabled
- SSL/TLS mode `Full (strict)`
- Cloudflare Origin Certificate in Caddy
- Caddy `basic_auth` in front of the site
- indexing blocked with `robots.txt`

This is intentionally simple and static.

## Access Hygiene Goal

Maintain a private rollout where:

- the password is not casually re-used forever
- access can be reset quickly if it spreads
- the operator knows who currently has access
- rotation does not depend on memory

## What To Track

Keep a small access register outside the public repository.

Minimum fields:

- who received access
- date access was granted
- cohort or reason for access
- whether the person still needs access
- whether the password was shared directly or via a teacher/intermediary

Good enough formats:

- a private local note
- a private password manager note
- an offline spreadsheet

Do not put the live password into the repository.

## Current Operational Rule

The shared password is acceptable only while all of the following remain true:

- access stays within a small trusted group
- the group changes infrequently
- there is a clear rotation procedure
- the site is still in private review mode

If these conditions stop being true, the current model becomes weak fast.

## Rotation Triggers

Rotate the password immediately if:

- the password is forwarded beyond the intended group
- someone leaves the trusted rollout group
- the password appears in screenshots, chat logs, or shared notes
- a teacher or student reports wider unintended access
- you are no longer confident who has it

Rotate the password proactively if:

- the rollout group changes materially
- the current password has been in use too long
- you are preparing a new cohort or test phase

## Rotation Procedure

Generate a new hash on the Debian host:

```bash
caddy hash-password --algorithm bcrypt
```

Replace the old hash in `/etc/caddy/Caddyfile`, then:

```bash
sudo caddy fmt --overwrite /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
```

Verify:

```bash
curl -I https://coderlap.com
curl -I -u admin:'NEW_PASSWORD' https://coderlap.com
```

Expected:

- without credentials: `401`
- with the new password: the site responds successfully

Only after successful verification should the new password be distributed.

## Distribution Rules

- share the password only out of band
- do not post it into general classroom chat if avoidable
- do not store it in public issue comments, repo text, or screenshots
- prefer direct sharing to the small intended group
- do not send it together with “feel free to forward”

If the project is used through a teacher, prefer giving the teacher clear
instructions rather than letting the password propagate informally.

## Minimal Rotation Checklist

Use this checklist every time:

1. update the access register first
2. generate a new `bcrypt` hash
3. update Caddy
4. validate and reload
5. verify `401` without auth
6. verify successful response with the new password
7. only then distribute the new password
8. mark the old password as retired

## What To Do If Access Spreads

If the password leaks or spreads too broadly:

1. assume the old password is compromised
2. rotate immediately
3. narrow the next sharing set
4. update the access register with the incident date
5. do not try to “wait and see” if the spread is already obvious

The shared-password model has no individual revocation. Delay only increases
the blast radius.

## Recommended Access Register Template

This template should stay outside the repository:

```text
Date granted | Person or cohort | Reason | Shared by | Still needed? | Notes
```

Example:

```text
2026-04-16 | Teacher A | review | direct | yes | private beta
2026-04-16 | Student group B | classroom test | via Teacher A | yes | short-term
```

If names are sensitive, initials or short labels are enough. The point is
operational clarity, not bureaucracy.

## Review Cadence

Minimum recommendation:

- review the access register whenever the rollout group changes
- review before each password rotation
- review before any broader release decision

## Threshold For Moving Beyond Shared Password

Do not add a backend auth system by default.

But if access needs exceed a small trusted circle, the next step should be one
of these:

1. Cloudflare Access
2. a separate rotated password for a distinct cohort
3. per-user Caddy credentials only if still operationally manageable

If password distribution becomes the main operational burden, the current model
has reached its limit.

## Relationship To Other Documents

Use this together with:

- [private-rollout-access.md](./private-rollout-access.md)
- [backup-restore-playbook.md](./backup-restore-playbook.md)
- [pre-public-checklist.md](./pre-public-checklist.md)

## Done Criteria

This improvement is complete only when:

- the rotation procedure is documented
- the operator has a private access register outside the repo
- password sharing is no longer ad hoc
- recovery and access reset can be done without improvisation
