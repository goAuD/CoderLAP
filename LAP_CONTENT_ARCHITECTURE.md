---
title: LAP Content Architecture and Delivery Guide
filename_suggestion: LAP_CONTENT_ARCHITECTURE.md
status: draft
owner: Viktor
project: LAP Learning Platform
language: en
last_updated: 2026-04-08
purpose: >
  Canonical content and delivery guide for the LAP learning platform.
  Defines markdown content schema, ID system, review workflow, i18n direction,
  search/filter requirements, and recommended hosting/deployment model.
---

# LAP Content Architecture and Delivery Guide

## 1. Purpose

This document defines the **content architecture** and the **recommended delivery model**
for the LAP learning platform.

The goal is to build a platform that is:

- self-written
- source-based
- searchable
- filterable
- later translatable
- mobile-friendly
- easy to host
- simple to maintain

The platform starts as **Markdown-first** and later gets an **HTML/CSS/JS presentation layer**.

---

## 2. Core Decisions

### 2.1 Source of truth

The canonical source of truth is always the **Markdown content**.

Not the frontend.  
Not the i18n JSON files.  
Not a database.

**Canonical source:**

```txt
content/hu/**/*.md
```

### 2.2 First language

The initial working language is **Hungarian**.

German comes later as a second content layer:

- either as separate `content/de/**/*.md`
- or through a translation pipeline after review

### 2.3 First-version philosophy

The first version is **not a classic web application**.

It is a:

- protected static knowledge site
- low-complexity content system
- low-cost deployment
- low-attack-surface setup

That means:

- no required SQL database
- no required Supabase
- no required custom auth backend
- no required admin dashboard

---

## 3. Content Principle

Each subtopic file is a standalone learning unit.

Each file must:

- have a unique stable ID
- contain a 30-second answer
- contain a longer explanation
- contain keywords
- contain sources
- contain status metadata
- be translatable later under the same ID

---

## 4. Recommended Folder Structure

```txt
content/
  hu/
    datentechnik-und-systemmanagement/
      AEDC-DS-001-halozati-alapfogalmak.md
      AEDC-DS-002-os-modellek.md
      AEDC-DS-003-ip-dns-dhcp.md

    angewandte-mathematik/
      AEDC-AM-001-logika-alapok.md
      AEDC-AM-002-binari-hexadecimalis.md

    applikationsentwicklung/
      AEDC-AP-001-oop-alapok.md
      AEDC-AP-002-adatszerkezetek.md

  de/
    # later only
    # same IDs as HU content
    # created only from reviewed/approved HU content

i18n/
  hu.json
  de.json

docs/
  content-rules/
  source-policy/
  review-guidelines/

scripts/
  validate-content.*
  build-site.*
  export-search-index.*

site/
  # static frontend / generated output / public files
```

---

## 5. Stable ID System

### 5.1 Why fixed IDs are required

A fixed ID is required for:

- search
- filtering
- internal linking
- language mapping
- stable URLs
- content indexing
- validation
- review workflow
- future export/build scripts

### 5.2 ID format

Recommended format:

```txt
AEDC-<DOMAIN>-<NNN>
```

Examples:

```txt
AEDC-DS-001
AEDC-DS-002
AEDC-AM-001
AEDC-AP-001
```

### 5.3 Domain abbreviations

Recommended values:

- `DS` = Datentechnik und Systemmanagement
- `AM` = Angewandte Mathematik
- `AP` = Applikationsentwicklung

### 5.4 ID rules

- The ID **never changes** if the title changes.
- The ID is **not generated from the filename**.
- The ID is **not generated from the slug**.
- The ID is the primary content identifier.
- One ID belongs to one conceptual unit only.

---

## 6. Filename Convention

Recommended format:

```txt
<ID>-<slug>.md
```

Examples:

```txt
AEDC-DS-001-halozati-alapfogalmak.md
AEDC-AP-014-oop-oroklodes-polimorfizmus.md
```

Rules:

- slug should be lowercase
- avoid accents in slug
- use hyphens instead of spaces
- filename should stay human-readable
- stability comes from the ID, not the slug

---

## 7. Required Front Matter

Every content file should begin with structured metadata.

### 7.1 Recommended front matter template

```md
---
id: AEDC-DS-001
lang: hu
title: Hálózati alapfogalmak
slug: halozati-alapfogalmak
domain: DS
domain_label: Datentechnik und Systemmanagement
topic: halozatok
subtopic: alapok
exam_relevance: core
answer_length: 30s
difficulty: basic
review_status: draft
translation_status: not_started
source_quality: official_plus_secondary
tags:
  - halozat
  - tcp-ip
  - lan
keywords:
  - protokoll
  - kliens
  - szerver
  - topologia
related_ids:
  - AEDC-DS-002
  - AEDC-DS-003
source_count: 3
updated_at: 2026-04-08
canonical: true
---
```

### 7.2 Required fields

Minimum required:

- `id`
- `lang`
- `title`
- `slug`
- `domain`
- `domain_label`
- `topic`
- `subtopic`
- `exam_relevance`
- `answer_length`
- `difficulty`
- `review_status`
- `translation_status`
- `tags`
- `keywords`
- `related_ids`
- `source_count`
- `updated_at`
- `canonical`

---

## 8. Required Content Blocks Inside Each Markdown File

Recommended structure:

```md
# Title

## Rövid válasz (30 mp)

## Magyarázat

## Mire figyelj vizsgán

## Kulcsszavak

## Kapcsolódó altémák

## Források
```

### 8.1 Minimum content rule

Each subtopic must contain:

- one short 30-second answer
- one longer explanation
- 3–8 keywords
- at least 1–3 sources
- related subtopics
- visible content status in front matter

---

## 9. Complete Example File

```md
---
id: AEDC-DS-001
lang: hu
title: Hálózati alapfogalmak
slug: halozati-alapfogalmak
domain: DS
domain_label: Datentechnik und Systemmanagement
topic: halozatok
subtopic: alapok
exam_relevance: core
answer_length: 30s
difficulty: basic
review_status: draft
translation_status: not_started
source_quality: official_plus_secondary
tags:
  - halozat
  - tcp-ip
  - lan
keywords:
  - protokoll
  - kliens
  - szerver
  - topologia
related_ids:
  - AEDC-DS-002
  - AEDC-DS-003
source_count: 3
updated_at: 2026-04-08
canonical: true
---

# Hálózati alapfogalmak

## Rövid válasz (30 mp)

A hálózat olyan összekapcsolt eszközök rendszere, amelyek adatot tudnak egymással cserélni.
A kommunikáció szabályait protokollok írják le, például ilyen a TCP/IP.
A hálózat célja az erőforrás-megosztás, az adatátvitel és a kommunikáció biztosítása.

## Magyarázat

Számítógépes hálózatban több eszköz kapcsolódik egymáshoz, például számítógépek,
szerverek, routerek vagy nyomtatók. Ezek vezetékes vagy vezeték nélküli kapcsolaton
keresztül kommunikálnak.

A hálózati kommunikációhoz közös szabályrendszer kell. Ezeket hívjuk protokolloknak.
A legismertebb protokollcsalád a TCP/IP. A hálózatok lehetnek kis helyi hálózatok
(LAN) vagy nagyobb, földrajzilag kiterjedt rendszerek is.

Vizsgán fontos, hogy a hálózat fogalmát ne csak technikai listaként mondd vissza,
hanem tudd elmagyarázni a célját is: kommunikáció, adatmegosztás, erőforrás-megosztás.

## Mire figyelj vizsgán

- tudd röviden megfogalmazni, mi a hálózat
- tudd megkülönböztetni az eszközt és a protokollt
- említs példát: kliens, szerver, router, TCP/IP
- ne csak definíciót mondj, hanem funkciót is

## Kulcsszavak

- hálózat
- protokoll
- TCP/IP
- kliens
- szerver
- router
- LAN
- kommunikáció

## Kapcsolódó altémák

- AEDC-DS-002
- AEDC-DS-003

## Források

1. Hivatalos szakmai vagy oktatási forrás
2. Dokumentáció vagy szabvány
3. Kiegészítő szakmai magyarázó forrás
```

---

## 10. Source Handling Rules

### 10.1 Source priority

Recommended priority:

1. official source
2. standard / documentation
3. educational institution source
4. high-quality professional explainer source

### 10.2 Core rule

We do **not** copy the source.

We:

- read it
- understand it
- summarize it in our own words
- link back to it properly

### 10.3 Source block format

Recommended format:

```md
## Források

1. Szerző / szervezet – Cím – URL
2. Szerző / szervezet – Cím – URL
3. Szerző / szervezet – Cím – URL
```

### 10.4 Avoid

Do not include:

- book copies
- large pasted text blocks
- copied exam examples
- screenshot collections
- unclear-origin summaries

---

## 11. Search and Filter Requirements

The future frontend/search layer should be able to use these fields:

- `id`
- `lang`
- `title`
- `slug`
- `domain`
- `domain_label`
- `topic`
- `subtopic`
- `exam_relevance`
- `difficulty`
- `review_status`
- `translation_status`
- `tags`
- `keywords`
- `related_ids`
- `updated_at`

### 11.1 Minimum filters

Recommended first filters:

- by main domain
- by topic
- by subtopic
- by difficulty
- by review status
- by language
- by keyword/tag

### 11.2 Minimum search targets

Search should match:

- title
- tags
- keywords
- short answer
- explanation
- ID

---

## 12. Review and Translation Status Model

### 12.1 Review status

Recommended values:

- `draft`
- `reviewed`
- `approved`
- `published`

### 12.2 Translation status

Recommended values:

- `not_started`
- `machine_draft`
- `human_reviewed`
- `approved`

### 12.3 Why this matters

With 233+ files, it must remain visible:

- what is still raw
- what has been reviewed by you
- what is ready for translation
- what is safe to publish

---

## 13. Related Content Strategy

Use `related_ids` consistently.

Why this helps:

- creates a light knowledge graph
- improves navigation
- supports exam-oriented study paths
- enables future “read this next” sections

Example:

```yaml
related_ids:
  - AEDC-DS-002
  - AEDC-DS-005
  - AEDC-AP-011
```

---

## 14. i18n Strategy

### 14.1 Core rule

Translation must **not** come before reviewed Hungarian source content.

### 14.2 Recommended sequence

1. HU markdown is created
2. HU review happens
3. HU becomes approved
4. DE draft is created using the same ID
5. DE review happens
6. DE becomes approved
7. content is published

### 14.3 Practical rule

At the beginning, i18n files should translate only the **UI layer**:

- menu labels
- button labels
- filter labels
- status labels
- navigation text
- helper messages

Content translation should remain a separate content process.

---

## 15. Build Strategy

### 15.1 Recommended model

The frontend is only a presentation layer.

Flow:

```txt
Markdown content -> validation -> index/export -> static site
```

### 15.2 Acceptable first implementation

The first version can be:

- plain HTML/CSS/JS
- simple markdown parsing/export
- JSON search index
- static site generation or static export

### 15.3 Not recommended at the start

Do not introduce too early:

- SQL database
- complex CMS
- custom auth system
- browser-based editor panel
- overengineered backend

---

## 16. Recommended Validation Rules

Later a validation script should check at least:

- does every file have an `id`
- is every `id` unique
- does every file have a `title`
- does every file have a `domain`
- does every file have a `review_status`
- does every file have at least one source
- does every file contain a short answer
- do all `related_ids` exist
- are there slug collisions
- are any required sections missing

---

## 17. Recommended Repository Model

### 17.1 Repository type

Recommended starting point:

- GitHub personal account
- private repository
- optional collaborators if needed later

### 17.2 Branch model

Simple starting model:

- `main` = stable branch
- `dev` = active working branch
- optional feature branches later if needed

### 17.3 Content workflow

Recommended content flow:

- Codex works on `dev`
- you review changes
- only checked content moves to `main`
- deployment happens from `main`

---

## 18. Recommended Hosting Model

### 18.1 First version hosting goal

The recommended first version is:

- own server
- Caddy
- static site
- Basic Auth
- private repo
- built or exported site directory

### 18.2 Why this is recommended

Because it is:

- cheap
- simple
- stable
- low maintenance
- low complexity
- low attack surface
- enough for the first real version

### 18.3 What is intentionally not needed now

Not needed in the first version:

- SQL
- Supabase
- user database
- password reset system
- admin dashboard
- full backend auth
- complex access management

---

## 19. Recommended Caddy Direction

### 19.1 Why Caddy fits

Caddy is a strong fit here because the platform needs:

- simple static hosting
- easy configuration
- HTTPS-friendly operation
- lightweight access protection
- minimal operational complexity

### 19.2 Basic Auth recommendation

Recommended starter protection:

- protect the whole site or a specific route
- use hashed password
- keep it behind HTTPS
- do not build a separate auth backend yet

### 19.3 Recommended target Caddy shape

```caddy
chseets.com {
    root * /var/www/chseets
    encode zstd gzip

    basic_auth {
        <USERNAME> <HASHED_PASSWORD>
    }

    file_server
}
```

### 19.4 Practical recommendation

For this project, Basic Auth is not the final enterprise identity layer.

It is:

- cheap
- fast
- understandable
- good enough for the first protected version

---

## 20. Recommended Deployment Strategy

### 20.1 Deployment goal

The first deployment goal should be:

**after push, the static site updates in a predictable and simple way**

### 20.2 Two acceptable deployment options

#### Option A — GitHub Actions -> server deploy

Good if:

- you want automated deploy
- you already have SSH access to the server
- you want a clean CI/CD path

#### Option B — server-side `git pull` with deploy key

Good if:

- you want a pull-based model
- you prefer simpler server control
- you want minimal moving parts

### 20.3 One-rule deployment principle

At the beginning, choose **one single deployment path**.

Do not mix:

- Actions deploy
- manual SCP copy
- server-side pull
- multiple parallel scripts

One clean path is better than three half-working paths.

### 20.4 Recommended starting direction

Recommended starting combination:

- private repo
- `main` branch deployment
- static export/build
- Caddy serving the output
- Basic Auth protecting access
- deployment by either:
  - GitHub Actions over SSH
  - or server-side pull with deploy key

---

## 21. Security Minimum

Minimum recommended baseline:

- private repository
- Basic Auth
- hashed password
- HTTPS
- minimal exposed surface
- only required open ports
- deployment secrets not stored in the repo
- use GitHub Secrets or deploy key if automation is added later

---

## 22. Final Decision Summary

### Content

- Markdown-first
- HU-first
- reviewed-first
- fixed ID system
- unified front matter
- source-based content
- related content via `related_ids`

### Translation

- UI i18n first
- content translation later
- only from reviewed/approved HU content

### Technical direction

- static site
- own server
- Caddy
- Basic Auth
- no database at the start
- no separate auth backend at the start

### Repo and deployment

- private GitHub repo
- `main` + `dev`
- one clean deployment path
- later automation possible

---

## 23. Suggested Root-Level Files

Recommended additional root docs:

```txt
LAP_CONTENT_ARCHITECTURE.md
LAP_MARKDOWN_SCHEMA.md
LAP_REVIEW_WORKFLOW.md
LAP_DEPLOY_STRATEGY.md
LAP_SOURCE_POLICY.md
```

---

## 24. Final Recommendation

Recommended starting direction:

- keep the 233+ subtopics in `.md` files
- assign a stable fixed ID to every file
- keep markdown as the source of truth
- keep the frontend as a presentation layer only
- keep the repository private
- host it on your own Caddy server
- use Basic Auth for the first protected version
- do not introduce a database now
- keep deployment simple and singular

---

## 25. Project Mantra

**First stable content system.  
Then translation.  
Then presentation layer.  
Then refinement.  
Not the other way around.**
