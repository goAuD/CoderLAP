# LAP Deploy Strategy

## Goal

Move the project into a GitHub-ready local location now and keep the deployment path simple later.

The intended long-term direction is:

```txt
Local source repo
  -> private GitHub repository
  -> server checkout or deploy
  -> static site served by Caddy
```

## Current Local Source Location

Canonical working source right now:

```txt
C:\GitHub\CoderLAP
```

Legacy/original source snapshot:

```txt
C:\DEV_SCHOOL\LAP_THEMEN
```

## Recommended Repository Model

Recommended repo shape:

- private repository
- `main` = stable content
- `dev` = active work

This is enough for the project at the current stage.

## What Should Be Deployed Later

Do **not** deploy the raw working repo directly as the final public web root unless intentionally doing so.

Preferred later deployment target:

- a generated static site output
- or a controlled static content directory

The Markdown corpus stays the source.
The web build is only the presentation layer.

## Recommended First Hosting Direction

For the first real hosted version:

- own server
- `Caddy`
- static site
- `Basic Auth`
- no SQL database
- no backend auth system

## Recommended Caddy Shape

Example direction:

```caddy
example.com {
    root * /var/www/coderlap-site
    encode zstd gzip

    basic_auth {
        <USERNAME> <HASHED_PASSWORD>
    }

    file_server
}
```

This is intentionally simple and low-maintenance.

## Recommended Deployment Options

Choose exactly **one** of these later:

### Option A: GitHub Actions -> SSH deploy

Good if:

- you want automatic deployment
- you already have SSH access
- you want push-based deployment

### Option B: server-side `git pull`

Good if:

- you want the simplest server control model
- you prefer pulling from the server after review
- you want fewer moving parts

## Recommended First Real Path

Based on the current project stage, the lowest-risk path is:

1. keep the project in `C:\GitHub\CoderLAP`
2. initialize or connect it to a private GitHub repo
3. keep editing there
4. later, on the server, choose one deployment path only
5. serve the built/static result through Caddy

## Security Minimum

Minimum baseline:

- private GitHub repo
- SSH-based access where needed
- no deploy secrets committed to the repo
- `Basic Auth` on the first hosted version
- HTTPS via Caddy

## Practical Note For This Project

Because the content corpus is already complete:

- the next engineering phase is not more content creation
- it is structure, translation support, indexing, and site delivery

That is why:

- stable registry
- private repo
- predictable deployment path

are now higher-value than large structural rewrites.
