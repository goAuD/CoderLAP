# CoderLAP Static Frontend Design

Date: `2026-04-09`  
Status: `approved for planning`  
Branch target: `dev`

## Context

`CoderLAP` already has a complete Hungarian Markdown corpus for the Austrian `LAP` exam in `Applikationsentwicklung - Coding`.

Current source of truth:

- numbered German folder tree
- `README.md` topic files
- `LAP_CONTENT_REGISTRY.json`
- `LAP_CONTENT_REGISTRY.csv`

The next phase is a stable, professional, static frontend that presents the existing corpus without changing the canonical content structure.

## Primary Decision

Build a generated static **multipage** site with:

- Python-based site generation
- vanilla `HTML/CSS/JS` in the browser
- dark, professional, mobile-first UI
- English frontend UI in `V1`
- Hungarian topic content in `V1`
- hidden i18n architecture for later `de/hu`
- printable light-mode detail pages

React is explicitly **not** part of `V1`.

## Goals

- Make the full corpus easy to browse, search, filter, read, and print.
- Keep the runtime simple, fast, and low-risk.
- Preserve Markdown as the source of truth.
- Support later German translation without redesigning the site.
- Keep deployment static-first for later Caddy hosting with Basic Auth.
- Produce a frontend that feels professional, not like a quick documentation dump.

## Non-Goals

- No backend.
- No database.
- No user accounts.
- No visible language switcher in `V1`.
- No deployment automation in this phase.
- No content migration away from the existing numbered folder tree.
- No full translation workflow yet.

## Architecture Overview

The site will have two layers:

1. Source layer
- existing Markdown files
- registry metadata
- site configuration files

2. Generated output layer
- static HTML pages
- static CSS and JS assets
- generated JSON index files for search/navigation
- local font assets

Recommended output directory:

- `dist/`

Recommended source directories to add:

- `site/` for templates, assets, UI text, and generator helpers
- `docs/superpowers/specs/` for design and planning documents

## Why Multipage

Multipage is the best fit because it gives:

- direct links to every topic
- better reading experience for long-form educational content
- better print handling
- simpler progressive enhancement
- lower runtime complexity than a large single-page app
- cleaner future language routing

## Route Model

`V1` route model:

- `/` home and catalog entry point
- `/topics/<slug>/` topic detail pages
- `/imprint/`
- `/privacy/`

Future-ready route model:

- `/de/`
- `/de/topics/<slug>/`
- `/hu/`
- `/hu/topics/<slug>/`

`V1` should internally prepare for the future route model, but only the active language path set needs to be published first.

## Homepage Specification

The homepage is both a landing page and the main discovery surface.

Required homepage sections:

- hero with short project positioning
- search field with immediate keyboard focus support
- quick project stats
- main-topic filter controls for the `18` modules
- searchable result list
- entry point to sidebar navigation

Homepage behavior:

- fast client-side filtering from generated JSON
- clear empty-state when no results match
- compact mobile layout
- wider desktop layout with more breathing room

## Sidebar and Navigation

The primary navigation is a left-side sliding sidebar.

Required behavior:

- opens from the left
- overlays content on mobile
- remains more persistent on desktop
- lists the full main-topic and subtopic hierarchy
- supports quick jump into any topic page

Detail-page navigation:

- breadcrumb
- previous topic
- next topic
- back-to-catalog action
- print action

## Search and Filter Model

Search and filter must be deterministic and static.

Search index data should include at least:

- topic title
- slug
- main topic number
- main topic label
- subtopic label
- canonical path
- source count
- review status
- translation status

`V1` search scope:

- title
- slug
- main topic name
- subtopic directory name

`V1` filters:

- main topic

Prepared but optional filters:

- review status
- translation status
- source availability

No server-side search is required.

## Topic Detail Page Specification

Each topic page is a dedicated reading page generated from one canonical Markdown file.

Required page parts:

- page title
- topic metadata
- rendered Markdown content
- previous and next topic links
- back-to-home/catalog action
- print action

Markdown rendering must support the current corpus well, including:

- headings
- paragraphs
- flat lists
- tables
- inline code
- fenced code blocks when present
- source lists

## Print Specification

Print mode is a separate light presentation, not dark mode.

Required print behavior:

- white background
- dark text
- remove dotted grid pattern
- remove sidebar and most navigation chrome
- keep title and core metadata
- keep tables readable
- keep sources readable
- optimize margins for paper and PDF export

Print is focused on individual topic detail pages.

## Visual System

The visual direction is restrained, modern, and professional.

Design characteristics:

- dark default interface
- grey-based text instead of bright white
- subtle dotted grid pattern in the background
- inset panel shadows for surfaces
- slightly raised button treatment for contrast
- minimalistic spacing and clean composition
- clear reading hierarchy for long-form text

Accent direction:

- muted teal or desaturated cyan

Avoid:

- purple-heavy default AI aesthetics
- glossy neon effects
- oversized decorative motion
- high-contrast pure white text blocks

## Typography

Fonts must be local, not CDN-hosted.

Recommended font pairing:

- headings: `Manrope`
- body and UI: `Source Sans 3`

Requirements:

- download and store font files locally as `woff2`
- define fallback sans-serif stacks
- optimize for readability on phone, tablet, and desktop
- keep body text soft grey on dark surfaces

## CSS Strategy

Use a global token-based CSS approach.

Required CSS design:

- global custom properties for colors, shadows, spacing, radii, type scale, and motion
- mobile-first layout rules
- responsive breakpoints kept consistent across the site
- dedicated print rules
- component-level structure for shared UI pieces

The CSS should be organized so future contributors can extend it without untangling a monolithic stylesheet.

## Responsiveness

The site must be mobile-first and study-friendly on smaller screens.

Required responsive principles:

- no horizontal scroll in normal usage
- comfortable touch targets
- readable body text without zoom
- sidebar as off-canvas on mobile
- dense but readable topic lists on phone
- wider reading column on desktop with controlled line length

## Build Pipeline

Use Python for site generation.

The build pipeline should:

- read the registry
- read the canonical Markdown files
- render topic detail HTML pages
- generate the homepage catalog data
- generate sidebar hierarchy data
- calculate previous and next topic links
- copy static assets
- emit a complete deployable static directory

Suggested high-level generator outputs:

- `dist/index.html`
- `dist/topics/<slug>/index.html`
- `dist/imprint/index.html`
- `dist/privacy/index.html`
- `dist/assets/...`
- `dist/data/topic-index.json`
- `dist/data/navigation.json`

## i18n Strategy

`V1` must prepare for multilingual expansion without exposing a fake language switcher.

Rules:

- the visible UI stays English in `V1`
- the visible content stays Hungarian in `V1`
- the language switcher remains hidden until German topic content exists
- routing and data structures should assume future `de/hu` ordering
- content identity should be anchored to stable registry IDs

Recommended i18n structure:

- UI strings in separate language files
- content resolution keyed by registry ID and language
- future language availability flags derived from generated metadata

Future expectation:

- when German content starts landing, `de` becomes the primary public language and `hu` becomes the secondary option

## Legal Pages

The site must include:

- `Imprint`
- `Privacy`

`V1` requirement:

- create the page structure and routing now
- keep the footer minimal and compliant-oriented
- use official Austrian and EU legal sources when finalizing the text

Footer content should remain minimal:

- project name
- imprint link
- privacy link
- optional GitHub link

## Security and Hosting Assumptions

The frontend should default to a low attack surface.

Assumptions:

- static-only site
- no backend runtime
- no database
- later Basic Auth in Caddy
- later deployment behind an existing Debian+Caddy setup

This phase must not depend on SSH access, Caddy changes, or live deployment.

## Testing Strategy

`V1` must be verified before translation and deployment work starts.

Required validation areas:

- generator produces the full site successfully
- all `233` topic pages render
- homepage search and main-topic filters work
- sidebar navigation works on mobile and desktop
- topic pages link correctly through previous and next navigation
- print output is light and readable
- local fonts load correctly
- no broken internal links in generated output
- layout works at phone, tablet, laptop, and desktop widths

Recommended testing approach:

- generator smoke test
- link validation over `dist/`
- manual browser QA
- targeted responsive checks

## Delivery Sequence

Implementation should follow this order:

1. create the generator and output shape
2. create the base templates and asset pipeline
3. implement homepage and detail pages
4. implement search, filter, and sidebar navigation
5. implement print styles
6. implement legal pages and footer
7. test and polish
8. start translation support work after frontend stability

## Final Decision Summary

The approved `V1` is:

- Python-generated static multipage site
- vanilla `HTML/CSS/JS`
- English UI
- Hungarian content
- hidden future-ready `de/hu` i18n architecture
- dark default theme
- light print theme
- local fonts
- mobile-first responsive layout
- minimal legal footer and dedicated legal pages

This design prioritizes:

- clarity
- long-term maintainability
- low runtime complexity
- low attack surface
- strong reading and study usability
