# CoderLAP Static Frontend Implementation Plan

> **For Claude:** Use `${SUPERPOWERS_SKILLS_ROOT}/skills/collaboration/executing-plans/SKILL.md` to implement this plan task-by-task.

**Goal:** Build a Python-generated static multipage frontend for the existing CoderLAP Markdown corpus with English UI, Hungarian topic content, fast search/filter, dark responsive design, light print view, and hidden future-ready `de/hu` i18n architecture.

**Architecture:** Keep the current Markdown corpus and registry as the source of truth. Add a Python generator that reads `LAP_CONTENT_REGISTRY.json` plus the canonical `README.md` files, renders static HTML through Jinja templates, emits JSON indexes for search/navigation, and copies local assets into `dist/`. Keep runtime behavior in vanilla `HTML/CSS/JS`, with no backend and no database.

**Tech Stack:** Python 3, `Jinja2`, `Markdown`, vanilla `HTML/CSS/JS`, local `woff2` fonts, standard-library `unittest`

---

## Required Reading Before Implementation

- [AGENTS.md](d:\GitHub\CoderLAP\AGENTS.md)
- [2026-04-09-coderlap-static-frontend-design.md](d:\GitHub\CoderLAP\docs\superpowers\specs\2026-04-09-coderlap-static-frontend-design.md)
- [generate_content_registry.py](d:\GitHub\CoderLAP\scripts\generate_content_registry.py)
- [LAP_CONTENT_REGISTRY.json](d:\GitHub\CoderLAP\LAP_CONTENT_REGISTRY.json)

## Conventions For The Engineer

- Keep the current numbered German folder tree untouched.
- Do not modify canonical topic content while building the site layer.
- Favor standard library unless a dependency clearly saves complexity.
- Keep the runtime static and low-complexity.
- Follow @skills/frontend-design and @skills/frontend-responsive-design-standards when implementing UI assets.
- Maintain keyboard accessibility for search, sidebar, and print affordances.

### Task 1: Bootstrap the site generator workspace

**Files:**
- Create: `d:\GitHub\CoderLAP\requirements.txt`
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\__init__.py`
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\settings.py`
- Create: `d:\GitHub\CoderLAP\scripts\build_site.py`
- Create: `d:\GitHub\CoderLAP\tests\__init__.py`
- Create: `d:\GitHub\CoderLAP\tests\test_site_builder_settings.py`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_builder_settings.py`:

```python
from pathlib import Path
import unittest

from scripts.site_builder.settings import BuildSettings


class BuildSettingsTest(unittest.TestCase):
    def test_from_repo_root_builds_expected_paths(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        settings = BuildSettings.from_repo_root(repo_root)

        self.assertEqual(settings.repo_root.name, "CoderLAP")
        self.assertEqual(settings.registry_path, repo_root / "LAP_CONTENT_REGISTRY.json")
        self.assertEqual(settings.template_dir, repo_root / "site" / "templates")
        self.assertEqual(settings.asset_dir, repo_root / "site" / "assets")
        self.assertEqual(settings.output_dir, repo_root / "dist")


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_builder_settings -v`

Expected output:

```text
ERROR: test_site_builder_settings (unittest.loader._FailedTest.test_site_builder_settings)
ModuleNotFoundError: No module named 'scripts.site_builder'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\requirements.txt`:

```text
Jinja2==3.1.6
Markdown==3.8
```

In `d:\GitHub\CoderLAP\scripts\site_builder\settings.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BuildSettings:
    repo_root: Path
    registry_path: Path
    template_dir: Path
    asset_dir: Path
    output_dir: Path
    i18n_dir: Path
    legal_content_dir: Path

    @classmethod
    def from_repo_root(cls, repo_root: Path) -> "BuildSettings":
        return cls(
            repo_root=repo_root,
            registry_path=repo_root / "LAP_CONTENT_REGISTRY.json",
            template_dir=repo_root / "site" / "templates",
            asset_dir=repo_root / "site" / "assets",
            output_dir=repo_root / "dist",
            i18n_dir=repo_root / "site" / "i18n",
            legal_content_dir=repo_root / "site" / "content" / "legal" / "en",
        )
```

In `d:\GitHub\CoderLAP\scripts\build_site.py`:

```python
from pathlib import Path

from scripts.site_builder.settings import BuildSettings


def main() -> None:
    settings = BuildSettings.from_repo_root(Path(__file__).resolve().parent.parent)
    print(f"Site build workspace ready: {settings.output_dir}")


if __name__ == "__main__":
    main()
```

**Step 4: Install dependencies and rerun the test**

Run: `python -m pip install -r requirements.txt`

Expected output:

```text
Successfully installed Jinja2-3.1.6 Markdown-3.8
```

Run: `python -m unittest tests.test_site_builder_settings -v`

Expected output:

```text
test_from_repo_root_builds_expected_paths ... ok
```

**Step 5: Commit**

```bash
git add requirements.txt scripts/site_builder/__init__.py scripts/site_builder/settings.py scripts/build_site.py tests/__init__.py tests/test_site_builder_settings.py
git commit -m "chore: bootstrap static site generator workspace"
```

### Task 2: Load registry items and canonical Markdown content

**Files:**
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\models.py`
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\loaders.py`
- Create: `d:\GitHub\CoderLAP\tests\test_site_builder_loaders.py`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_builder_loaders.py`:

```python
from pathlib import Path
import tempfile
import unittest

from scripts.site_builder.loaders import load_registry_items, load_topic_markdown


class LoaderTest(unittest.TestCase):
    def test_load_registry_items_returns_sorted_topics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry = root / "registry.json"
            registry.write_text(
                """
                {
                  "items": [
                    {"id": "LAP-02-02", "lang": "hu", "title": "B", "path": "02_Module/02_Sub/README.md", "main_topic_number": "02", "main_topic_dir": "02_Module", "subtopic_number": "02", "subtopic_dir": "02_Sub", "slug": "02-02-b", "review_status": "draft", "translation_status": "not_started", "source_count": 1, "opened_at": "2026-04-08", "canonical": true},
                    {"id": "LAP-01-01", "lang": "hu", "title": "A", "path": "01_Module/01_Sub/README.md", "main_topic_number": "01", "main_topic_dir": "01_Module", "subtopic_number": "01", "subtopic_dir": "01_Sub", "slug": "01-01-a", "review_status": "draft", "translation_status": "not_started", "source_count": 2, "opened_at": "2026-04-08", "canonical": true}
                  ]
                }
                """.strip(),
                encoding="utf-8",
            )

            items = load_registry_items(registry)

            self.assertEqual([item.id for item in items], ["LAP-01-01", "LAP-02-02"])

    def test_load_topic_markdown_reads_utf8_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            readme = root / "README.md"
            readme.write_text("# Cím\n\nMagyar tartalom.", encoding="utf-8")

            markdown = load_topic_markdown(readme)

            self.assertIn("Magyar tartalom.", markdown)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_builder_loaders -v`

Expected output:

```text
ImportError: cannot import name 'load_registry_items' from 'scripts.site_builder.loaders'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\scripts\site_builder\models.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TopicRecord:
    id: str
    lang: str
    title: str
    path: str
    main_topic_number: str
    main_topic_dir: str
    subtopic_number: str
    subtopic_dir: str
    slug: str
    review_status: str
    translation_status: str
    source_count: int
    opened_at: str | None
    canonical: bool

    def absolute_markdown_path(self, repo_root: Path) -> Path:
        return repo_root / self.path
```

In `d:\GitHub\CoderLAP\scripts\site_builder\loaders.py`:

```python
from __future__ import annotations

import json
from pathlib import Path

from scripts.site_builder.models import TopicRecord


def load_registry_items(registry_path: Path) -> list[TopicRecord]:
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    items = [TopicRecord(**item) for item in payload["items"] if item["canonical"]]
    return sorted(items, key=lambda item: (item.main_topic_number, item.subtopic_number))


def load_topic_markdown(markdown_path: Path) -> str:
    return markdown_path.read_text(encoding="utf-8")
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_builder_loaders -v`

Expected output:

```text
test_load_registry_items_returns_sorted_topics ... ok
test_load_topic_markdown_reads_utf8_content ... ok
```

**Step 5: Commit**

```bash
git add scripts/site_builder/models.py scripts/site_builder/loaders.py tests/test_site_builder_loaders.py
git commit -m "feat: add registry and markdown loaders for site build"
```

### Task 3: Build navigation groups and previous/next topic links

**Files:**
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\navigation.py`
- Create: `d:\GitHub\CoderLAP\tests\test_site_builder_navigation.py`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_builder_navigation.py`:

```python
import unittest

from scripts.site_builder.models import TopicRecord
from scripts.site_builder.navigation import build_navigation


class NavigationTest(unittest.TestCase):
    def test_build_navigation_creates_prev_next_links(self) -> None:
        topics = [
            TopicRecord("LAP-01-01", "hu", "ASCII", "01/A/README.md", "01", "01_Grundlagen", "01", "01_ASCII", "01-01-ascii", "draft", "not_started", 1, None, True),
            TopicRecord("LAP-01-02", "hu", "Bit", "01/B/README.md", "01", "01_Grundlagen", "02", "02_Bit", "01-02-bit", "draft", "not_started", 1, None, True),
            TopicRecord("LAP-02-01", "hu", "OS", "02/A/README.md", "02", "02_Betriebssysteme", "01", "01_OS", "02-01-os", "draft", "not_started", 1, None, True),
        ]

        navigation = build_navigation(topics)

        self.assertEqual(navigation["topics"]["LAP-01-02"]["previous_id"], "LAP-01-01")
        self.assertEqual(navigation["topics"]["LAP-01-02"]["next_id"], "LAP-02-01")
        self.assertEqual(len(navigation["main_topics"]), 2)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_builder_navigation -v`

Expected output:

```text
ModuleNotFoundError: No module named 'scripts.site_builder.navigation'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\scripts\site_builder\navigation.py`:

```python
from __future__ import annotations

from collections import OrderedDict

from scripts.site_builder.models import TopicRecord


def build_navigation(topics: list[TopicRecord]) -> dict:
    main_topics: OrderedDict[str, dict] = OrderedDict()
    topic_map: dict[str, dict] = {}

    for index, topic in enumerate(topics):
        main_entry = main_topics.setdefault(
            topic.main_topic_number,
            {
                "number": topic.main_topic_number,
                "label": topic.main_topic_dir,
                "topics": [],
            },
        )
        main_entry["topics"].append(
            {
                "id": topic.id,
                "title": topic.title,
                "slug": topic.slug,
                "subtopic_number": topic.subtopic_number,
                "subtopic_dir": topic.subtopic_dir,
            }
        )

        previous_id = topics[index - 1].id if index > 0 else None
        next_id = topics[index + 1].id if index + 1 < len(topics) else None
        topic_map[topic.id] = {
            "id": topic.id,
            "slug": topic.slug,
            "previous_id": previous_id,
            "next_id": next_id,
        }

    return {
        "main_topics": list(main_topics.values()),
        "topics": topic_map,
    }
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_builder_navigation -v`

Expected output:

```text
test_build_navigation_creates_prev_next_links ... ok
```

**Step 5: Commit**

```bash
git add scripts/site_builder/navigation.py tests/test_site_builder_navigation.py
git commit -m "feat: add navigation model for static site"
```

### Task 4: Render Markdown through Jinja templates

**Files:**
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\render.py`
- Create: `d:\GitHub\CoderLAP\tests\test_site_builder_render.py`
- Create: `d:\GitHub\CoderLAP\site\templates\base.html`
- Create: `d:\GitHub\CoderLAP\site\templates\home.html`
- Create: `d:\GitHub\CoderLAP\site\templates\topic.html`
- Create: `d:\GitHub\CoderLAP\site\templates\legal.html`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_builder_render.py`:

```python
from pathlib import Path
import tempfile
import unittest

from scripts.site_builder.render import build_template_environment, render_markdown


class RenderTest(unittest.TestCase):
    def test_render_markdown_supports_tables_and_code(self) -> None:
        html = render_markdown(
            "# Title\n\n| A | B |\n| - | - |\n| 1 | 2 |\n\n`code`",
        )
        self.assertIn("<table>", html)
        self.assertIn("<code>code</code>", html)

    def test_build_template_environment_loads_base_templates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            templates = root / "templates"
            templates.mkdir()
            (templates / "base.html").write_text("<html>{% block body %}{% endblock %}</html>", encoding="utf-8")

            env = build_template_environment(templates)

            self.assertIsNotNone(env.get_template("base.html"))


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_builder_render -v`

Expected output:

```text
ModuleNotFoundError: No module named 'scripts.site_builder.render'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\scripts\site_builder\render.py`:

```python
from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown import markdown


def render_markdown(markdown_text: str) -> str:
    return markdown(
        markdown_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def build_template_environment(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
```

In `d:\GitHub\CoderLAP\site\templates\base.html`:

```html
<!DOCTYPE html>
<html lang="{{ ui_lang }}">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }}</title>
    <link rel="stylesheet" href="{{ asset_prefix }}/css/base.css">
    <link rel="stylesheet" href="{{ asset_prefix }}/css/layout.css">
    <link rel="stylesheet" href="{{ asset_prefix }}/css/components.css">
    <link rel="stylesheet" href="{{ asset_prefix }}/css/print.css" media="print">
  </head>
  <body class="{{ body_class }}">
    {% block body %}{% endblock %}
    <script src="{{ asset_prefix }}/js/site.js" defer></script>
  </body>
</html>
```

In `d:\GitHub\CoderLAP\site\templates\home.html`:

```html
{% extends "base.html" %}
{% block body %}
<main class="page-shell">
  <section class="hero-panel">
    <p class="eyebrow">{{ ui.project_tagline }}</p>
    <h1>{{ ui.home_title }}</h1>
    <p class="hero-copy">{{ ui.home_intro }}</p>
  </section>
</main>
{% endblock %}
```

In `d:\GitHub\CoderLAP\site\templates\topic.html`:

```html
{% extends "base.html" %}
{% block body %}
<main class="page-shell">
  <article class="topic-article">{{ content_html | safe }}</article>
</main>
{% endblock %}
```

In `d:\GitHub\CoderLAP\site\templates\legal.html`:

```html
{% extends "base.html" %}
{% block body %}
<main class="page-shell">
  <article class="legal-article">{{ content_html | safe }}</article>
</main>
{% endblock %}
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_builder_render -v`

Expected output:

```text
test_build_template_environment_loads_base_templates ... ok
test_render_markdown_supports_tables_and_code ... ok
```

**Step 5: Commit**

```bash
git add scripts/site_builder/render.py tests/test_site_builder_render.py site/templates/base.html site/templates/home.html site/templates/topic.html site/templates/legal.html
git commit -m "feat: add markdown renderer and Jinja templates"
```

### Task 5: Generate topic pages, homepage, and navigation JSON

**Files:**
- Create: `d:\GitHub\CoderLAP\scripts\site_builder\build.py`
- Create: `d:\GitHub\CoderLAP\tests\test_site_builder_build.py`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_builder_build.py`:

```python
from pathlib import Path
import json
import tempfile
import unittest

from scripts.site_builder.build import write_json


class BuildHelpersTest(unittest.TestCase):
    def test_write_json_creates_parent_directories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "data" / "topic-index.json"

            write_json(output_path, {"count": 1})

            self.assertTrue(output_path.exists())
            self.assertEqual(json.loads(output_path.read_text(encoding="utf-8"))["count"], 1)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_builder_build -v`

Expected output:

```text
ModuleNotFoundError: No module named 'scripts.site_builder.build'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\scripts\site_builder\build.py`:

```python
from __future__ import annotations

import json
import shutil
from pathlib import Path

from scripts.site_builder.loaders import load_registry_items, load_topic_markdown
from scripts.site_builder.navigation import build_navigation
from scripts.site_builder.render import build_template_environment, render_markdown
from scripts.site_builder.settings import BuildSettings


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_site(settings: BuildSettings, ui_strings: dict, legal_pages: dict) -> None:
    topics = load_registry_items(settings.registry_path)
    navigation = build_navigation(topics)
    env = build_template_environment(settings.template_dir)

    if settings.output_dir.exists():
        shutil.rmtree(settings.output_dir)
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(settings.asset_dir, settings.output_dir / "assets", dirs_exist_ok=True)

    topic_index = []

    for topic in topics:
        markdown_text = load_topic_markdown(topic.absolute_markdown_path(settings.repo_root))
        content_html = render_markdown(markdown_text)
        output_dir = settings.output_dir / "topics" / topic.slug
        output_dir.mkdir(parents=True, exist_ok=True)

        previous_id = navigation["topics"][topic.id]["previous_id"]
        next_id = navigation["topics"][topic.id]["next_id"]

        html = env.get_template("topic.html").render(
            page_title=f"{topic.title} | CoderLAP",
            ui_lang="en",
            body_class="topic-page",
            asset_prefix="/assets",
            ui=ui_strings,
            topic=topic,
            previous_id=previous_id,
            next_id=next_id,
            content_html=content_html,
        )
        (output_dir / "index.html").write_text(html, encoding="utf-8")

        topic_index.append(
            {
                "id": topic.id,
                "title": topic.title,
                "slug": topic.slug,
                "main_topic_number": topic.main_topic_number,
                "main_topic_label": topic.main_topic_dir,
                "subtopic_label": topic.subtopic_dir,
                "source_count": topic.source_count,
                "review_status": topic.review_status,
                "translation_status": topic.translation_status,
            }
        )

    home_html = env.get_template("home.html").render(
        page_title="CoderLAP",
        ui_lang="en",
        body_class="home-page",
        asset_prefix="/assets",
        ui=ui_strings,
        topics=topic_index,
        navigation=navigation["main_topics"],
    )
    (settings.output_dir / "index.html").write_text(home_html, encoding="utf-8")

    for slug, markdown_text in legal_pages.items():
        html = env.get_template("legal.html").render(
            page_title=f"{slug.title()} | CoderLAP",
            ui_lang="en",
            body_class="legal-page",
            asset_prefix="/assets",
            ui=ui_strings,
            content_html=render_markdown(markdown_text),
        )
        legal_dir = settings.output_dir / slug
        legal_dir.mkdir(parents=True, exist_ok=True)
        (legal_dir / "index.html").write_text(html, encoding="utf-8")

    write_json(settings.output_dir / "data" / "topic-index.json", {"topics": topic_index})
    write_json(settings.output_dir / "data" / "navigation.json", navigation)
```

**Step 4: Extend the entrypoint**

In `d:\GitHub\CoderLAP\scripts\build_site.py`, replace the placeholder `main()` with:

```python
import json
from pathlib import Path

from scripts.site_builder.build import build_site
from scripts.site_builder.settings import BuildSettings


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    settings = BuildSettings.from_repo_root(repo_root)
    ui_strings = json.loads((settings.i18n_dir / "en.json").read_text(encoding="utf-8"))
    legal_pages = {
        "imprint": (settings.legal_content_dir / "imprint.md").read_text(encoding="utf-8"),
        "privacy": (settings.legal_content_dir / "privacy.md").read_text(encoding="utf-8"),
    }
    build_site(settings, ui_strings, legal_pages)
    print(f"Built site into {settings.output_dir}")


if __name__ == "__main__":
    main()
```

**Step 5: Run test to verify it passes**

Run: `python -m unittest tests.test_site_builder_build -v`

Expected output:

```text
test_write_json_creates_parent_directories ... ok
```

**Step 6: Commit**

```bash
git add scripts/site_builder/build.py scripts/build_site.py tests/test_site_builder_build.py
git commit -m "feat: add static site build pipeline"
```

### Task 6: Add English UI strings and legal content sources

**Files:**
- Create: `d:\GitHub\CoderLAP\site\i18n\en.json`
- Create: `d:\GitHub\CoderLAP\site\content\legal\en\imprint.md`
- Create: `d:\GitHub\CoderLAP\site\content\legal\en\privacy.md`
- Create: `d:\GitHub\CoderLAP\tests\test_site_content_assets.py`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_content_assets.py`:

```python
from pathlib import Path
import json
import unittest


class SiteContentAssetsTest(unittest.TestCase):
    def test_english_ui_strings_define_core_labels(self) -> None:
        payload = json.loads(Path("site/i18n/en.json").read_text(encoding="utf-8"))

        self.assertEqual(payload["home_title"], "A focused study hub for the Austrian LAP exam")
        self.assertIn("Search topics", payload["search_placeholder"])
        self.assertEqual(payload["print_label"], "Print topic")

    def test_legal_markdown_files_exist(self) -> None:
        self.assertTrue(Path("site/content/legal/en/imprint.md").exists())
        self.assertTrue(Path("site/content/legal/en/privacy.md").exists())


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_content_assets -v`

Expected output:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'site/i18n/en.json'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\site\i18n\en.json`:

```json
{
  "project_tagline": "Austrian LAP exam knowledge base",
  "home_title": "A focused study hub for the Austrian LAP exam",
  "home_intro": "Browse 233 Hungarian study topics through a calm, fast, mobile-first interface built for revision.",
  "search_placeholder": "Search topics, slugs, or module names",
  "search_label": "Search topics",
  "filter_label": "Filter by module",
  "sidebar_label": "Open topic navigation",
  "back_to_catalog": "Back to catalog",
  "print_label": "Print topic",
  "previous_label": "Previous topic",
  "next_label": "Next topic",
  "imprint_label": "Imprint",
  "privacy_label": "Privacy"
}
```

In `d:\GitHub\CoderLAP\site\content\legal\en\imprint.md`:

```markdown
# Imprint

This site is a private educational project for LAP exam preparation.

## Project owner

- Name: `Viktor Halupka`
- Project: `CoderLAP`

## Status

- Static educational website
- Non-commercial draft until deployment review is complete

## Finalization note

- Complete Austrian imprint details before public deployment.
- Validate the final text against official Austrian sources and the actual publishing setup.
```

In `d:\GitHub\CoderLAP\site\content\legal\en\privacy.md`:

```markdown
# Privacy

This static site is designed to minimize data processing.

## Current assumptions

- No user accounts
- No database
- No form submissions
- No third-party runtime CDN dependencies

## Finalization note

- Complete the final privacy text before public deployment.
- Validate the final text against official Austrian and EU privacy requirements.
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_content_assets -v`

Expected output:

```text
test_english_ui_strings_define_core_labels ... ok
test_legal_markdown_files_exist ... ok
```

**Step 5: Commit**

```bash
git add site/i18n/en.json site/content/legal/en/imprint.md site/content/legal/en/privacy.md tests/test_site_content_assets.py
git commit -m "feat: add ui strings and legal content sources"
```

### Task 7: Add local font acquisition and asset copy support

**Files:**
- Create: `d:\GitHub\CoderLAP\scripts\fetch_site_fonts.py`
- Create: `d:\GitHub\CoderLAP\tests\test_fetch_site_fonts.py`
- Create: `d:\GitHub\CoderLAP\site\assets\fonts\.gitkeep`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_fetch_site_fonts.py`:

```python
from pathlib import Path
import tempfile
import unittest

from scripts.fetch_site_fonts import build_output_path


class FetchSiteFontsTest(unittest.TestCase):
    def test_build_output_path_keeps_woff2_extension(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_path = build_output_path(
                root,
                family_slug="manrope",
                source_url="https://fonts.gstatic.com/s/manrope/v15/font.woff2",
            )

            self.assertEqual(output_path.name, "manrope-font.woff2")
            self.assertEqual(output_path.parent, root)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_fetch_site_fonts -v`

Expected output:

```text
ModuleNotFoundError: No module named 'scripts.fetch_site_fonts'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\scripts\fetch_site_fonts.py`:

```python
from __future__ import annotations

import re
import urllib.request
from pathlib import Path


GOOGLE_CSS_URLS = {
    "manrope": "https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap",
    "source-sans-3": "https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&display=swap",
}


def build_output_path(output_dir: Path, family_slug: str, source_url: str) -> Path:
    suffix = Path(source_url.rstrip("/").split("/")[-1]).suffix or ".woff2"
    return output_dir / f"{family_slug}-font{suffix}"


def main() -> None:
    output_dir = Path(__file__).resolve().parent.parent / "site" / "assets" / "fonts"
    output_dir.mkdir(parents=True, exist_ok=True)

    for family_slug, css_url in GOOGLE_CSS_URLS.items():
        request = urllib.request.Request(css_url, headers={"User-Agent": "Mozilla/5.0"})
        css_text = urllib.request.urlopen(request).read().decode("utf-8")
        urls = re.findall(r"url\((https://fonts\.gstatic\.com[^\)]+\.woff2)\)", css_text)
        if not urls:
            raise RuntimeError(f"No font URL found for {family_slug}")

        target_path = build_output_path(output_dir, family_slug, urls[0])
        urllib.request.urlretrieve(urls[0], target_path)
        print(f"Downloaded {target_path.name}")


if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_fetch_site_fonts -v`

Expected output:

```text
test_build_output_path_keeps_woff2_extension ... ok
```

**Step 5: Download the font files**

Run: `python ./scripts/fetch_site_fonts.py`

Expected output:

```text
Downloaded manrope-font.woff2
Downloaded source-sans-3-font.woff2
```

**Step 6: Commit**

```bash
git add scripts/fetch_site_fonts.py tests/test_fetch_site_fonts.py site/assets/fonts/.gitkeep site/assets/fonts
git commit -m "feat: add local font acquisition workflow"
```

### Task 8: Implement the global visual system and print styles

**Files:**
- Create: `d:\GitHub\CoderLAP\site\assets\css\base.css`
- Create: `d:\GitHub\CoderLAP\site\assets\css\layout.css`
- Create: `d:\GitHub\CoderLAP\site\assets\css\components.css`
- Create: `d:\GitHub\CoderLAP\site\assets\css\print.css`
- Create: `d:\GitHub\CoderLAP\tests\test_site_css_assets.py`
- Modify: `d:\GitHub\CoderLAP\site\templates\base.html`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_site_css_assets.py`:

```python
from pathlib import Path
import unittest


class CssAssetsTest(unittest.TestCase):
    def test_base_css_defines_core_tokens(self) -> None:
        css = Path("site/assets/css/base.css").read_text(encoding="utf-8")
        self.assertIn("--color-bg: #15181c;", css)
        self.assertIn("--color-text: #c9d1d9;", css)
        self.assertIn("--color-accent: #5fa7a2;", css)
        self.assertIn("--divider-line:", css)

    def test_print_css_switches_to_light_theme(self) -> None:
        css = Path("site/assets/css/print.css").read_text(encoding="utf-8")
        self.assertIn("@media print", css)
        self.assertIn("background: #ffffff", css)
        self.assertIn("color: #111111", css)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_css_assets -v`

Expected output:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'site/assets/css/base.css'
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\site\assets\css\base.css`:

```css
:root {
  --font-heading: "Manrope", "Segoe UI", sans-serif;
  --font-body: "Source Sans 3", "Segoe UI", sans-serif;
  --color-bg: #15181c;
  --color-panel: #1c2127;
  --color-panel-elevated: #222831;
  --color-text: #c9d1d9;
  --color-text-muted: #9aa6b2;
  --color-accent: #5fa7a2;
  --color-accent-soft: rgba(95, 167, 162, 0.18);
  --shadow-inset: inset 0 1px 0 rgba(255, 255, 255, 0.03), inset 0 -1px 0 rgba(0, 0, 0, 0.3);
  --shadow-raised: 0 0.75rem 1.5rem rgba(0, 0, 0, 0.22);
  --divider-line: linear-gradient(90deg, rgba(95, 167, 162, 0), rgba(95, 167, 162, 0.85), rgba(95, 167, 162, 0));
  --radius-md: 1rem;
  --radius-lg: 1.5rem;
  --content-width: 72rem;
}

@font-face {
  font-family: "Manrope";
  src: url("../fonts/manrope-font.woff2") format("woff2");
  font-weight: 500 800;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Source Sans 3";
  src: url("../fonts/source-sans-3-font.woff2") format("woff2");
  font-weight: 400 700;
  font-style: normal;
  font-display: swap;
}

html {
  color-scheme: dark;
}

body {
  margin: 0;
  font-family: var(--font-body);
  background: var(--color-bg);
  color: var(--color-text);
}
```

In `d:\GitHub\CoderLAP\site\assets\css\layout.css`:

```css
body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background-image:
    radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.08) 1px, transparent 0);
  background-size: 22px 22px;
  opacity: 0.22;
}

.page-shell {
  width: min(100% - 2rem, var(--content-width));
  margin: 0 auto;
  padding: 1.5rem 0 4rem;
}
```

In `d:\GitHub\CoderLAP\site\assets\css\components.css`:

```css
.hero-panel,
.topic-article,
.legal-article,
.sidebar-panel {
  background: rgba(28, 33, 39, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-inset);
  backdrop-filter: blur(16px);
}

.section-divider::after,
.topic-article h2::after,
.topic-article h3::after {
  content: "";
  display: block;
  width: min(7rem, 30%);
  height: 1px;
  margin-top: 0.75rem;
  background: var(--divider-line);
}

.button-raised {
  border-radius: 999px;
  box-shadow: var(--shadow-raised);
}
```

In `d:\GitHub\CoderLAP\site\assets\css\print.css`:

```css
@media print {
  html {
    color-scheme: light;
  }

  body {
    background: #ffffff !important;
    color: #111111 !important;
  }

  body::before,
  .sidebar-panel,
  .topbar,
  .filters-panel,
  .print-button {
    display: none !important;
  }

  .topic-article,
  .legal-article {
    box-shadow: none !important;
    border: 0 !important;
    background: #ffffff !important;
  }
}
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_css_assets -v`

Expected output:

```text
test_base_css_defines_core_tokens ... ok
test_print_css_switches_to_light_theme ... ok
```

**Step 5: Update the base template**

In `d:\GitHub\CoderLAP\site\templates\base.html`, add a top bar shell and footer:

```html
<body class="{{ body_class }}">
  <header class="topbar">
    <button class="button-raised" type="button" data-sidebar-toggle>{{ ui.sidebar_label }}</button>
  </header>
  {% block body %}{% endblock %}
  <footer class="site-footer">
    <span>CoderLAP</span>
    <a href="/imprint/">{{ ui.imprint_label }}</a>
    <a href="/privacy/">{{ ui.privacy_label }}</a>
  </footer>
  <script src="{{ asset_prefix }}/js/site.js" defer></script>
</body>
```

**Step 6: Commit**

```bash
git add site/assets/css/base.css site/assets/css/layout.css site/assets/css/components.css site/assets/css/print.css site/templates/base.html tests/test_site_css_assets.py
git commit -m "feat: add global dark theme and light print styles"
```

### Task 9: Implement homepage search, module filter, and sidebar behavior

**Files:**
- Create: `d:\GitHub\CoderLAP\site\assets\js\site.js`
- Modify: `d:\GitHub\CoderLAP\site\templates\home.html`
- Modify: `d:\GitHub\CoderLAP\site\templates\topic.html`
- Create: `d:\GitHub\CoderLAP\tests\test_template_hooks.py`

**Step 1: Write the failing test**

In `d:\GitHub\CoderLAP\tests\test_template_hooks.py`:

```python
from pathlib import Path
import unittest


class TemplateHooksTest(unittest.TestCase):
    def test_home_template_exposes_search_and_filter_hooks(self) -> None:
        html = Path("site/templates/home.html").read_text(encoding="utf-8")
        self.assertIn('data-search-input', html)
        self.assertIn('data-module-filter', html)
        self.assertIn('data-topic-results', html)

    def test_topic_template_exposes_print_hook(self) -> None:
        html = Path("site/templates/topic.html").read_text(encoding="utf-8")
        self.assertIn('data-print-trigger', html)


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_template_hooks -v`

Expected output:

```text
AssertionError: 'data-search-input' not found in ...
```

**Step 3: Write minimal implementation**

In `d:\GitHub\CoderLAP\site\templates\home.html`, expand the template:

```html
{% extends "base.html" %}
{% block body %}
<main class="page-shell">
  <section class="hero-panel section-divider">
    <p class="eyebrow">{{ ui.project_tagline }}</p>
    <h1>{{ ui.home_title }}</h1>
    <p class="hero-copy">{{ ui.home_intro }}</p>
    <label class="sr-only" for="topic-search">{{ ui.search_label }}</label>
    <input id="topic-search" type="search" placeholder="{{ ui.search_placeholder }}" data-search-input>
    <select data-module-filter aria-label="{{ ui.filter_label }}">
      <option value="">All modules</option>
      {% for main_topic in navigation %}
      <option value="{{ main_topic.number }}">{{ main_topic.number }} - {{ main_topic.label }}</option>
      {% endfor %}
    </select>
  </section>

  <aside class="sidebar-panel" data-sidebar hidden></aside>
  <section class="results-panel" data-topic-results></section>
  <script type="application/json" id="topic-index-json">{{ {"topics": topics} | tojson }}</script>
  <script type="application/json" id="navigation-json">{{ {"main_topics": navigation} | tojson }}</script>
</main>
{% endblock %}
```

In `d:\GitHub\CoderLAP\site\templates\topic.html`, add:

```html
{% extends "base.html" %}
{% block body %}
<main class="page-shell">
  <nav class="topic-actions">
    <a href="/">{{ ui.back_to_catalog }}</a>
    <button class="button-raised print-button" type="button" data-print-trigger>{{ ui.print_label }}</button>
  </nav>
  <article class="topic-article">{{ content_html | safe }}</article>
</main>
{% endblock %}
```

In `d:\GitHub\CoderLAP\site\assets\js\site.js`:

```javascript
function parseJsonScript(id) {
  const element = document.getElementById(id);
  if (!element) return null;
  return JSON.parse(element.textContent);
}

function renderTopicResults(topics, container) {
  container.innerHTML = topics
    .map(
      (topic) => `
        <a class="topic-card" href="/topics/${topic.slug}/">
          <span class="topic-card__meta">${topic.main_topic_number}</span>
          <strong>${topic.title}</strong>
          <span>${topic.subtopic_label}</span>
        </a>
      `,
    )
    .join("");
}

function setupHomePage() {
  const searchInput = document.querySelector("[data-search-input]");
  const moduleFilter = document.querySelector("[data-module-filter]");
  const results = document.querySelector("[data-topic-results]");
  const sidebar = document.querySelector("[data-sidebar]");
  const topicPayload = parseJsonScript("topic-index-json");
  const navigation = parseJsonScript("navigation-json");
  const topics = topicPayload ? topicPayload.topics : [];

  if (!searchInput || !moduleFilter || !results) return;

  function applyFilters() {
    const query = searchInput.value.trim().toLowerCase();
    const moduleValue = moduleFilter.value;
    const filtered = topics.filter((topic) => {
      const haystack = [
        topic.title,
        topic.slug,
        topic.main_topic_label,
        topic.subtopic_label,
      ].join(" ").toLowerCase();
      const moduleMatch = !moduleValue || topic.main_topic_number === moduleValue;
      return moduleMatch && haystack.includes(query);
    });
    renderTopicResults(filtered, results);
  }

  searchInput.addEventListener("input", applyFilters);
  moduleFilter.addEventListener("change", applyFilters);
  renderTopicResults(topics, results);

  if (sidebar && navigation) {
    sidebar.hidden = false;
    sidebar.innerHTML = navigation.main_topics
      .map(
        (mainTopic) => `
          <section>
            <h2>${mainTopic.number} - ${mainTopic.label}</h2>
            ${mainTopic.topics.map((topic) => `<a href="/topics/${topic.slug}/">${topic.title}</a>`).join("")}
          </section>
        `,
      )
      .join("");
  }
}

function setupPrintButtons() {
  document.querySelectorAll("[data-print-trigger]").forEach((button) => {
    button.addEventListener("click", () => window.print());
  });
}

document.addEventListener("DOMContentLoaded", () => {
  setupHomePage();
  setupPrintButtons();
});
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_template_hooks -v`

Expected output:

```text
test_home_template_exposes_search_and_filter_hooks ... ok
test_topic_template_exposes_print_hook ... ok
```

**Step 5: Commit**

```bash
git add site/assets/js/site.js site/templates/home.html site/templates/topic.html tests/test_template_hooks.py
git commit -m "feat: add search, filter, sidebar, and print hooks"
```

### Task 10: Add a full build smoke test, output validation, and usage docs

**Files:**
- Create: `d:\GitHub\CoderLAP\tests\test_build_site_smoke.py`
- Modify: `d:\GitHub\CoderLAP\README.md`
- Modify: `d:\GitHub\CoderLAP\docs\superpowers\specs\2026-04-09-coderlap-static-frontend-design.md`

**Step 1: Write the failing smoke test**

In `d:\GitHub\CoderLAP\tests\test_build_site_smoke.py`:

```python
from pathlib import Path
import subprocess
import unittest


class BuildSiteSmokeTest(unittest.TestCase):
    def test_build_site_generates_expected_outputs(self) -> None:
        result = subprocess.run(
            ["python", "scripts/build_site.py"],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertIn("Built site into", result.stdout)
        self.assertTrue(Path("dist/index.html").exists())
        self.assertTrue(Path("dist/data/topic-index.json").exists())
        self.assertTrue(Path("dist/topics/01-01-zeichensatz_ascii/index.html").exists())
        self.assertTrue(Path("dist/imprint/index.html").exists())
        self.assertTrue(Path("dist/privacy/index.html").exists())


if __name__ == "__main__":
    unittest.main()
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_build_site_smoke -v`

Expected output:

```text
FAIL: dist/topics/01-01-zeichensatz_ascii/index.html does not exist
```

**Step 3: Make the build complete enough to pass**

Run: `python ./scripts/build_site.py`

Expected output:

```text
Built site into D:\GitHub\CoderLAP\dist
```

If the build fails, fix the build code first before rerunning the smoke test. The smoke test is the final gate for `V1` scaffolding.

**Step 4: Run the smoke test**

Run: `python -m unittest tests.test_build_site_smoke -v`

Expected output:

```text
test_build_site_generates_expected_outputs ... ok
```

**Step 5: Update the repo documentation**

In `d:\GitHub\CoderLAP\README.md`, add a new section near the roadmap:

```markdown
## Static frontend build

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Build the site:

```bash
python ./scripts/build_site.py
```

The output is written to `dist/`.
```

In `d:\GitHub\CoderLAP\docs\superpowers\specs\2026-04-09-coderlap-static-frontend-design.md`, add a short note at the bottom:

```markdown
## Planning follow-through

- Implementation plan: `docs/plans/2026-04-09-coderlap-static-frontend.md`
```

**Step 6: Commit**

```bash
git add tests/test_build_site_smoke.py README.md docs/superpowers/specs/2026-04-09-coderlap-static-frontend-design.md
git commit -m "docs: add build usage and smoke-test the static site"
```

## Final Verification Checklist

- Run: `python -m pip install -r requirements.txt`
- Run: `python ./scripts/fetch_site_fonts.py`
- Run: `python ./scripts/build_site.py`
- Run: `python -m unittest discover -s tests -v`
- Manually inspect:
  - home page at `dist/index.html`
  - at least three topic pages under `dist/topics/`
  - `dist/imprint/index.html`
  - `dist/privacy/index.html`
  - print preview of one topic page
  - mobile viewport around `375px`
  - tablet viewport around `768px`
  - desktop viewport around `1440px`

## Scope Guardrails

- Do not add React, Vite, or a client-side framework.
- Do not add a backend or database.
- Do not expose the language switcher in `V1`.
- Do not rewrite topic Markdown content as part of the frontend build.
- Keep the background single-color dark graphite so the dotted grid remains clean.
- Keep accent colors calming and desaturated.
- Use decorative separator lines consistently, not everywhere.
