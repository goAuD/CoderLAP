# AGENTS.md

## Project Identity

This project is now actively maintained at `C:\GitHub\CoderLAP`.

Project name:

- `CoderLAP`

Preferred working location going forward:

- `C:\GitHub\CoderLAP`

Purpose:

- Build a complete study knowledge base for the Austrian `LAP` exam in
  `Applikationsentwicklung - Coding`.
- Base the structure on
  `themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`.
- Develop the content first in **Hungarian**.
- Keep folder names and file names in **German**.
- German translations exist as `README.de.md` alongside Hungarian `README.md`.
- German is the **default language** (served at `/`).
- Hungarian is the **secondary language** (served at `/hu/`).
- Planned production domain: `coderlap.com`.
- Present the whole project in a simple **HTML/CSS/JS web frontend**.

This is a long-running project. Any future thread should treat this file as the
continuity source.

## Source Of Truth

Primary structural source:

- `themenkatalog-applikationsentwicklung-coding-v2-2024.pdf` in the repository
  root

Canonical content source:

- the existing `README.md` files inside the numbered subtopic folders

Canonical metadata layer:

- `LAP_CONTENT_REGISTRY.json`
- `LAP_CONTENT_REGISTRY.csv`

Interpretation rules:

- The PDF defines the canonical topic hierarchy unless the user explicitly
  changes it.
- The existing directory structure in the repository root is already aligned to
  the PDF.
- Each main module has its own numbered folder.
- Each subtopic has its own numbered subfolder.
- The current numbered folder tree is intentionally preserved and should not be
  migrated unless the user explicitly requests it.

## Directory Conventions

Keep these conventions stable across all threads.

- Main folders remain in German, numbered, ASCII-safe.
- Subtopic folders remain in German, numbered, ASCII-safe.
- Content files inside subtopic folders should default to `README.md`.
- Do not rename existing topic folders unless the user explicitly requests it.
- Do not move the PDF.
- Do not create alternate naming schemes in parallel.

Example:

- `01_Grundlagen_in_der_Informationstechnik/01_Zeichensatz_ASCII/README.md`

## Current Status

Completed already:

- Full folder structure created from the PDF.
- `18` main folders created.
- `233` subtopic folders created.
- Main topic `01_Grundlagen_in_der_Informationstechnik` completed.
- `7 / 7` subtopic documents exist for main topic `01`.
- Main topic `02_Betriebssysteme_und_Software` completed.
- `10 / 10` subtopic documents exist for main topic `02`.
- Main topic `03_Betreuung_von_mobiler_Hardware` completed.
- `6 / 6` subtopic documents exist for main topic `03`.
- Main topic `04_Technische_Dokumentation_Projektarbeit_Schulungen` completed.
- `6 / 6` subtopic documents exist for main topic `04`.
- Main topic `05_Gesetzliche_Bestimmungen` completed.
- `16 / 16` subtopic documents exist for main topic `05`.
- Main topic `06_Netzwerkdienste` completed.
- `13 / 13` subtopic documents exist for main topic `06`.
- Main topic `07_IT_Security_und_Betriebssicherheit` completed.
- `8 / 8` subtopic documents exist for main topic `07`.
- Main topic `08_Informatik_und_Gesellschaft` completed.
- `11 / 11` subtopic documents exist for main topic `08`.
- Main topic `09_Ergonomischer_Arbeitsplatz` completed.
- `6 / 6` subtopic documents exist for main topic `09`.
- Main topic `10_Fachberatung_und_Planung` completed.
- `5 / 5` subtopic documents exist for main topic `10`.
- Main topic `11_Informatik` completed.
- `43 / 43` subtopic documents exist for main topic `11`.
- Topic `11` was completed in two phases: `01-21` and `22-43`.
- Main topic `12_Projektmanagement` completed.
- `20 / 20` subtopic documents exist for main topic `12`.
- Main topic `13_Projektmethoden_und_Tools` completed.
- `18 / 18` subtopic documents exist for main topic `13`.
- Main topic `14_Qualitaetssicherung` completed.
- `7 / 7` subtopic documents exist for main topic `14`.
- Main topic `15_Grundkenntnisse_des_Programmierens` completed.
- `20 / 20` subtopic documents exist for main topic `15`.
- Main topic `16_Datenbanken_Datenmodelle_Datenstrukturen` completed.
- `19 / 19` subtopic documents exist for main topic `16`.
- Main topic `17_Systementwicklung_und_Testkonzepte` completed.
- `13 / 13` subtopic documents exist for main topic `17`.
- Main topic `18_Uebungsbeispiel` completed.
- `5 / 5` subtopic documents exist for main topic `18`.
- A practical reference implementation was also added under
  `18_Uebungsbeispiel\Musterloesung_Minimal`.
- Total completed subtopic documents so far: `233`.
- Stable registry files were generated for all `233` canonical subtopic
  documents.
- Internal architecture/deployment docs now live under `docs/project/`.
- i18n infrastructure fully built: German default (`/`), Hungarian secondary
  (`/hu/`).
- All `233` subtopics translated to German as `README.de.md` files.
- Static site generator (Jinja2) outputs bilingual site to `dist/`.
- Planned production domain: `coderlap.com`.

When continuing work in a new thread:

- Check existing progress before creating new files.
- Extend the existing structure instead of inventing a new one.
- Use `C:\GitHub\CoderLAP` as the only active working copy.

## Content Language Rules

Default language for content:

- **Hungarian**

Naming language:

- **German** for directories and file names

Allowed exceptions:

- Sources may be in English, German, or other reliable languages.
- Internal planning notes for Codex may be in English.

## Content Level And Tone

Target level:

- `LAP (szakmunkás)` level
- practical
- exam-oriented
- clear and teachable

Avoid:

- overly academic depth unless the user asks for it
- vague definitions without examples
- bloated theory that is not useful in an oral or practical exam setting
- unsupported claims

Prefer:

- crisp definitions
- practical examples
- common exam pitfalls
- short memory aids
- direct exam-ready wording

Special note for main topic `11_Informatik`:

- the user considers this topic especially important
- go slightly deeper than in earlier modules
- still keep the content exam-oriented and scannable
- complete it in two halves because of the large number of subtopics

Special note for main topic `15_Grundkenntnisse_des_Programmierens`:

- the user asked for this topic to be developed slightly more deeply than topic
  `11_Informatik`
- keep the content practical and exam-oriented, but add more concept
  clarification
- prefer stronger compare/contrast sections for commonly confused programming
  basics
- include more precise distinctions for fundamentals such as algorithm vs
  program, variable vs constant, scope vs lifetime, compiler vs interpreter, and
  loop variants

Special note for main topic `18_Uebungsbeispiel`:

- this topic is practical, not theory-only
- keep the PDF as the exact functional source of truth
- besides the normal `README.md` writeups in the subfolders, create a minimal
  working reference solution
- prefer the simplest exam-realistic implementation over feature-rich
  architecture
- avoid adding backend, persistence, or extra UX features unless the PDF
  explicitly requires them

## Required Output Format For Topic Documents

Every new subtopic `README.md` should follow a consistent, visual-first
structure.

Recommended structure:

1. `# <German topic title>`
2. `## Lényeg 30 másodpercben`
3. `## Gyors vizuális kép`
4. `## Mi az ...?` or equivalent core explanation
5. `## Miért fontos?`
6. `## ...: ne keverd össze` or a comparison table when relevant
7. `## Mit nem tud / mire kell figyelni?` when relevant
8. `## Vizsgán jól használható megfogalmazás`
9. `## Gyakori vizsgahibák`
10. `## Gyors önellenőrzés`
11. `## Rövid válaszok az önellenőrzéshez`
12. `## Források`

Notes:

- Not every topic needs every section, but the structure should stay close to
  this pattern.
- The document should be easy to scan visually.
- Use tables where they improve understanding.
- Use short paragraphs.
- Use bullet lists for distinct points.
- Keep it Markdown-first so the content can later be reused for a website.

## Markdown Style Rules

Use:

- clear headings
- flat bullet lists
- compact tables
- inline code for technical terms, commands, literals, encodings, protocol
  names, keywords

Avoid:

- deeply nested bullets
- giant text walls
- decorative fluff
- inconsistent heading styles

Design intent:

- visual first
- structured
- fast to revise from
- suitable for later HTML rendering

## Source And Research Rules

The user explicitly wants modern, trustworthy sources.

Always prefer:

- official documentation
- standards bodies
- official legal texts or official government pages
- major technical references with current maintenance

Strong preferred sources by topic:

- Web and encoding: `W3C`, `WHATWG`, `MDN`, `Unicode`, `IETF RFCs`, `IANA`
- Security: `OWASP`, `NIST`, vendor official docs, RFCs
- Databases and web tech: official product/vendor documentation, standards, MDN,
  W3C
- Legal/EU/Austria topics: `EUR-Lex`, `RIS`, `oesterreich.gv.at`, official
  ministry or EU sources

Avoid:

- random blogs
- SEO spam sites
- low-quality tutorials
- outdated forum posts as primary sources
- unverifiable summaries

When a topic may have changed over time:

- verify with current sources
- include exact source URLs
- prefer primary sources over secondary explanations

## Source Citation Rules Inside Documents

Every topic document must end with a `## Források` section.

Minimum expectation:

- direct URL for each source
- short note on why that source was used
- access/open date when helpful

Preferred citation style:

1. Source title URL Usage note

Do not leave sources implied. Make them explicit.

## Workflow For Future Threads

When continuing this project:

1. Read this `AGENTS.md`.
2. Check whether the active working copy is `C:\GitHub\CoderLAP`.
3. Read the project architecture notes: `docs/project/content-architecture.md`,
   `docs/project/architecture-adoption.md`, `docs/project/deploy-strategy.md`
4. Check the registry files before large structural work:
   `LAP_CONTENT_REGISTRY.json`, `LAP_CONTENT_REGISTRY.csv`
5. Continue in the existing numbered structure.
6. For a requested topic, verify whether a `README.md` already exists.
7. If not, create it in the subtopic folder.
8. If it exists, improve it without breaking the established format unless the
   user asks for a redesign.
9. Use current, reliable sources when needed.
10. Keep Hungarian content and German file/folder names.
11. Preserve consistency across all topics.

## Fresh Thread Bootstrap

For a completely new Codex thread on another machine, use this startup order:

1. Open the repository root `C:\GitHub\CoderLAP`.
2. Read `AGENTS.md` first.
3. Read `README.md` for the high-level state.
4. Read `docs/project/deploy-strategy.md` if the task involves Git, GitHub,
   Caddy, DNS, Debian, or deployment.
5. Read `docs/project/next-thread-handoff.md` for the shortest practical
   continuation context.
6. Only read `LAP_CONTENT_REGISTRY.json` when indexing, i18n mapping, or
   site-building logic is relevant.

Deployment-oriented assumptions for a new thread:

- the GitHub repository already exists as `goAuD/CoderLAP`
- `main` and `dev` branches already exist
- the normal working branch should usually be `dev`
- the Debian server is reachable from the other PC via SSH
- the intended hosting direction is still static output behind Caddy

## Roadmap

Planned phases:

1. Keep the Hungarian canonical corpus stable and review-ready.
2. Keep the German translation sidecars aligned with the Hungarian source.
3. Maintain and polish the bilingual static frontend.
4. Deploy the generated static site to `coderlap.com`.
5. Keep deployment simple: Debian + Caddy + static output.

## Current i18n Guidance

The current priority is Hungarian source content.

Write documents with future translation in mind:

- use clear section boundaries
- avoid ambiguous phrasing
- avoid culture-specific shorthand unless explained
- keep terminology consistent across topics
- prefer reusable wording for definitions

Current direction:

- keep one canonical source document per subtopic
- use the registry IDs as stable language-mapping anchors
- keep German translations as `README.de.md` sidecars
- keep German default at `/` and Hungarian at `/hu/`

## Architecture Adoption Notes

What is already adopted from the architecture plan:

- Markdown-first source of truth
- stable external metadata registry instead of immediate front matter migration
- GitHub-ready repo hygiene via `.gitignore`
- explicit deployment planning for later Caddy delivery
- sidecar translation files (`README.de.md`)
- bilingual static-site build pipeline

What is intentionally deferred for now:

- full front matter in all `233` topic files
- migration into a new `content/hu` tree
- full `related_ids` graph inside each document
- database/CMS-backed publishing

## Registry Notes

Registry generator:

- `scripts\generate_content_registry.py`

Generated outputs:

- `LAP_CONTENT_REGISTRY.json`
- `LAP_CONTENT_REGISTRY.csv`

Current ID format:

- `LAP-<MAIN>-<SUB>`

Examples:

- `LAP-01-01`
- `LAP-11-43`
- `LAP-18-05`

Current default metadata values in the registry:

- `lang = hu`
- `review_status = draft`
- `translation_status = de_complete` when `README.de.md` exists, otherwise
  `de_missing`
- `canonical = true`

If content files are added, removed, or renamed, regenerate the registry. The
generator script is repository-root relative.

## Repo And Deployment Notes

Current repo preparation state:

- `.gitignore` exists
- architecture adoption is documented under `docs/project/`
- deployment direction is documented under `docs/project/`
- project is already Git/GitHub-ready under `C:\GitHub\CoderLAP`
- the bilingual static frontend build is already implemented

Recommended next technical phase after content completion:

1. continue from the GitHub copy
2. keep `main` and `dev`
3. perform final QA on `dev`
4. deploy the generated/static output through Caddy
5. cut over `coderlap.com`

## Current Web Frontend Guidance

The project already renders through a static web interface.

Therefore:

- keep content portable and Markdown-friendly
- avoid format choices that are hard to transform into HTML
- use clean headings and tables
- keep sections semantically meaningful
- do not bury important facts in huge paragraphs

Potential future deliverables:

- further UI polish
- deployment-specific hardening
- search/filter refinements
- print improvements
- content QA adjustments

Do not replace the current frontend architecture unless the user explicitly
requests a redesign.

## Editing Policy

When modifying this project:

- preserve prior work unless the user asks for a rewrite
- prefer incremental improvement over unnecessary restructuring
- keep naming stable
- do not duplicate the same topic in multiple places
- if a topic overlaps another topic, mention the distinction clearly inside the
  content rather than restructuring folders

## Session Memory Notes

What the user wants from Codex:

- collaborate over many threads
- preserve continuity
- keep a stable format
- produce visually clear study material
- use reliable modern sources
- stay practical and exam-oriented

What has already been validated by the user:

- the folder structure is good
- the first topic format is good
- the content style should remain similar going forward
- for `11_Informatik`, slightly deeper coverage is desired
- for `11_Informatik`, work in two halves: `01-21` and later `22-43`

## Default Assumptions

Unless the user says otherwise:

- create or edit files under the current repository root
- treat `C:\GitHub\CoderLAP` as the canonical local working copy
- use `README.md` inside each topic folder
- write in Hungarian
- keep directory/file names in German
- include sources in every topic document
- optimize for clarity, consistency, and future reuse
