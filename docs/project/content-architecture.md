# CoderLAP Content and Build Architecture

Last updated: `2026-04-16`

## Purpose

This document describes the **current** content architecture of `CoderLAP`.

It reflects the repository after:

- the Hungarian source corpus was completed
- all `235` registered topic documents were translated to German as
  `README.de.md`
- the static frontend and i18n layer were implemented

## Canonical Sources

The project has four distinct source layers:

1. **PDF hierarchy source**
   - `themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`
   - Defines the canonical topic tree.

2. **Canonical learning content**
   - `README.md` inside each numbered subtopic folder
   - Hungarian remains the canonical source language.

3. **Translation sidecars**
   - `README.de.md` next to the Hungarian `README.md`
   - German is the translated delivery language, not the canonical authoring
     source.

4. **Machine-readable metadata**
   - `LAP_CONTENT_REGISTRY.json`
   - `LAP_CONTENT_REGISTRY.csv`
   - Used for indexing, navigation, build input, and stable IDs.

## Current Repository Model

Relevant layout:

```text
CoderLAP/
  01_.../
    01_.../
      README.md
      README.de.md
  ...
  18_.../
  LAP_CONTENT_REGISTRY.json
  LAP_CONTENT_REGISTRY.csv
  scripts/
    build_site.py
    generate_content_registry.py
    review_content.py
    site_builder/
      build.py
      loaders.py
      navigation.py
      render.py
      settings.py
  site/
    assets/
    content/legal/
      de/
      en/
      hu/
    i18n/
      de.json
      en.json
      hu.json
    templates/
  docs/
    project/
    process/
    plans/
    superpowers/
```

## Language Model

### Content authoring

- `README.md` = Hungarian canonical content
- `README.de.md` = German translation sidecar

### Site output

- German is the default published language at `/`
- Hungarian is published at `/hu/`

### UI layer

- `site/i18n/de.json`
- `site/i18n/hu.json`

English files can exist as editorial fallback material, but the active published
site is currently `de + hu`.

## Static Build Model

Build entrypoint:

```powershell
python .\scripts\build_site.py
```

Build characteristics:

- Jinja2 templates + Markdown rendering
- static output only
- no database
- no runtime backend
- local font assets bundled in the repo
- output written to `dist/`

Generated output shape:

```text
dist/
  index.html        # German default
  topics/...
  module-packs/...
  imprint/
  privacy/
  robots.txt
  .well-known/
    security.txt
  hu/
    index.html      # Hungarian
    topics/...
    module-packs/...
    imprint/
    privacy/
  assets/
  data/
```

The site builder prefers a language-specific Markdown file when it exists:

- German build prefers `README.de.md`
- Hungarian build falls back to `README.md`

### Műhely frontend

The selected visual direction is the light Műhely design. It uses the existing
static templates and local Manrope / Source Sans 3 fonts, with no new runtime
dependencies. The normal build applies it to both languages, every topic,
module print packs and legal pages.

- `site/assets/css/base.css`: shared palette, typography, spacing and reading
  width. Adjust these variables before adding page-specific overrides.
- `layout.css`: responsive page structure and navigation placement.
- `components.css`: catalogue groups, controls and the static loop illustration.
- `print.css`: printable content without navigation or decoration.
- `site/i18n/*.json`: interface wording, including Regex's caption.
- `site/templates/workshop-visual.html`: the homepage loop illustration.

The catalogue initially groups topics by module. Search and module filtering
continue to use the existing bilingual terms and aliases, displaying matching
topics directly. JavaScript-disabled browsers retain the static topic links.
At widths of 48rem and above, catalogue accordions pack independently into
fixed odd/even columns. A ResizeObserver measures each block and sets CSS grid
row spans using the actual track height (including browser zoom rounding).
The DOM and keyboard order remain 01–18; mobile retains the same single-column
order. Searching or filtering disconnects the old observations and restores
the regular result-card grid. Without ResizeObserver the ordinary grid remains
usable. Print does not use the independently measured row spans.
Catalogue summaries suppress the native WebKit tap overlay, which can flash as
a filled rectangle on iOS. The shared `:focus-visible` outline remains
available for keyboard navigation.

Regression check: open and close module 02, then 06, and verify that modules
03/05/07 in the left column retain their document positions. Repeat on the left,
check a long open module, resize to mobile and back, and clear a search/filter.
Topic pages derive their chapter navigation from the rendered H2 headings;
the navigation is collapsible on mobile. Quick view supports its close button,
Escape and a keyboard focus loop that excludes collapsed topic links.

The existing `coderlap_progress` data format and completion behavior are
preserved. This change introduces no new progression system, authentication,
analytics or Quiz/Coaster deployment. Language roots and the quick-view close
label are passed once by the shared base template. Translated topic pages
declare the translation language; missing translations retain the source
language declaration.

Review locally before promotion: homepage search/filter, topic completion and
undo, language switching, quick view with keyboard, a long topic title, module
printing and legal pages. Browser emulation supplements the Python tests;
physical mobile and printer checks remain separate release validation.

The header and favicon share `site/assets/favicon.svg`; its standalone colors
match `--color-accent` and `--color-accent-contrast` in `base.css`. Update that
single SVG when changing the brand. The progress pill uses the shared accent,
spacing and radius tokens; progress storage and counting stay unchanged.
CSS, JavaScript and the icon URLs carry the existing build version so refreshed
HTML requests the current assets. This does not invalidate cached HTML or
override a CDN cache rule that ignores query strings.
On narrow screens the navigation fills its grid row, aligning its first button
with the brand icon instead of inheriting desktop right alignment.
The language switcher and the GitHub button above it share the right edge;
the GitHub button retains a full touch target around its smaller icon.
CoderQuiz and CoderCoaster are introduced below the homepage hero in the shared
`coder-tools.html` template. Every page links to each app's stable `#coderquiz` or
`#codercoaster` anchor from its localized footer. Native details show their
development status and a short explanation on
tap, including without JavaScript; there are no placeholder app URLs or extra
header rows. Copy lives in the existing language dictionaries. Add real app
destinations only when those releases and their access protection are ready.
The shared header height token is measured with ResizeObserver, so anchor links
and quick-view panels clear wrapped mobile navigation. CSS provides fallback
heights when JavaScript or ResizeObserver is unavailable.
The footer separates tools and legal links, with a GitHub link alongside the
brand. Links stack vertically within each group and have full touch targets.
Each tool's development status stays on its own line below the project name.
Its right gutter reserves the floating back-to-top button's width plus spacing,
so even during scrolling the button cannot cover a footer link.

`viewport-fit=cover` is paired with central `--safe-*` tokens from CSS
`env(safe-area-inset-*)`. Shared page gutters, header top padding, footer bottom
padding, quick view and the floating button respect those insets. Keep this
pairing when changing full-screen layout; verify portrait and landscape on a
physical iPhone as well as simulated nonzero insets. The calmer homepage title
is maintained in the existing HU/DE/EN dictionaries.
Keep document and site-shell ancestors of the sticky header free of clipping
layers. Nested `overflow-x: clip` was removed after iPhone scroll jitter was
reported; physical Safari validation is required for this rendering issue.
Wide tables and code blocks scroll inside their own containers, rather than
relying on clipping the whole page to hide overflow.
The no-JavaScript catalogue uses the same card classes and long-word wrapping
as the interactive catalogue, so narrow screens do not overflow.

Motion is controlled by the `--motion-*` tokens in `base.css`. The hero, topic
article and initial catalogue groups get one subtle 360 ms reveal when entering
the viewport. Content is never hidden while awaiting JavaScript or an observer.
No reveal or skeleton animation runs in print or with reduced motion enabled.
Search results do not repeatedly animate as the learner types.

On topic and legal pages, quick view shows skeleton rows only while its navigation
request is pending, without a minimum display delay. The close button works during
loading; a late response cannot reopen the overlay or steal focus. A failed request
(including the existing five-second timeout) removes the skeleton, shows a localized
message and links to the catalogue. Close and reopen quick view to retry. The
homepage already embeds its navigation and does not need a loading placeholder.

Run `node --test tests/site-interactions.test.cjs` with Node.js 18+ alongside the
Python suite. These dependency-free tests exercise pending/closed/ready/error/retry
states and reduced-motion/observer fallbacks with a small DOM test double. They do
not replace browser layout, keyboard or animation checks. The existing CI workflow
currently runs the Python suite; run this Node command explicitly during review.

For a temporary phone preview on the same trusted LAN, build the site and bind
the static server to the development computer's LAN address (replace the example
address with its actual IPv4 address):

```powershell
python scripts/build_site.py
python -m http.server 8767 --bind 192.168.0.50 --directory dist
```

Open `http://192.168.0.50:8767/` (German) or `/hu/` (Hungarian) on the phone.
`127.0.0.1` on a phone refers to the phone itself. Stop the foreground server
with Ctrl+C after review. This preview serves only `dist/`, has no Basic Auth,
and must not be exposed to the internet. If the computer responds but a phone
cannot connect, check Wi-Fi client isolation and a narrowly scoped private-LAN
firewall allowance; do not disable the firewall.

Before promotion, verify lesson → Startseite navigation at normal zoom and with
user zoom enabled, warm-cache refresh of the CSS/icon, and the existing completion
state. Retain production Basic Auth and the documented previous-build rollback.
DevTools page/pinch zoom can crop an otherwise responsive page: compare
`visualViewport.scale` with 1 before diagnosing missing CSS; keep user zoom enabled.

## Registry Model

Registry generator:

```powershell
python .\scripts\generate_content_registry.py
```

Current ID format:

```text
LAP-<MAIN>-<SUB>
```

Examples:

- `LAP-01-01`
- `LAP-11-43`
- `LAP-18-05`

Important rule:

- regenerate the registry if canonical topic files are added, removed, renamed,
  or structurally moved

The registry is intentionally external. The project still does **not** depend on
front matter embedded into all topic files.

Current metadata semantics worth remembering:

- `review_status` is still a coarse editorial field and currently remains
  `draft`
- `translation_status` is generated from the file system
- `de_complete` means the German sidecar exists
- `de_missing` means the German sidecar is missing

## What Is Intentionally Preserved

- the numbered German folder tree
- the PDF-aligned hierarchy
- Hungarian canonical source content
- Markdown-first authoring
- static-site delivery

## What Is Intentionally Deferred

- migration into `content/hu` / `content/de`
- full front matter across all topic files
- database-backed authoring or publishing
- CMS/editor backend
- any runtime app architecture beyond static delivery

## Current Technical Direction

The architecture is now stable enough for:

1. content/UI QA and maintenance
2. restricted live delivery at `coderlap.com`
3. Debian + Caddy delivery behind Cloudflare
4. low-attack-surface hosting with a single deploy path
5. public-safe repository visibility without changing the static-first model

This document should be updated whenever the on-disk structure, language
routing, or build pipeline changes.
