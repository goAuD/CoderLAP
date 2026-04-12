from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.site_builder.build import build_site, write_json
from scripts.site_builder.settings import BuildSettings


def _write_registry(registry_path: Path) -> None:
    registry_path.write_text(
        json.dumps(
            {
                "items": [
                    {
                        "id": "LAP-01-01",
                        "lang": "hu",
                        "title": "ASCII",
                        "path": "01_Grundlagen/01_ASCII/README.md",
                        "main_topic_number": "01",
                        "main_topic_dir": "01_Grundlagen",
                        "subtopic_number": "01",
                        "subtopic_dir": "01_ASCII",
                        "slug": "01-01-ascii",
                        "review_status": "draft",
                        "translation_status": "not_started",
                        "source_count": 2,
                        "opened_at": "2026-04-09",
                        "canonical": True,
                    }
                ]
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def _write_templates(template_dir: Path) -> None:
    (template_dir / "base.html").write_text(
        "<!DOCTYPE html><html lang=\"{{ page_lang | default(ui_lang, true) }}\"><body>{% block body %}{% endblock %}</body></html>",
        encoding="utf-8",
    )
    (template_dir / "home.html").write_text(
        "{% extends \"base.html\" %}{% block body %}<h1>{{ ui.home_title }}</h1><p>{{ ui.home_intro }}</p>{% endblock %}",
        encoding="utf-8",
    )
    (template_dir / "topic.html").write_text(
        "{% extends \"base.html\" %}{% block body %}<article data-topic-id=\"{{ topic.id }}\">{{ content_html | safe }}</article>{% endblock %}",
        encoding="utf-8",
    )
    (template_dir / "legal.html").write_text(
        "{% extends \"base.html\" %}{% block body %}<section class=\"legal\">{{ content_html | safe }}</section>{% endblock %}",
        encoding="utf-8",
    )


class BuildHelpersTests(unittest.TestCase):
    def test_write_json_creates_parent_directories_and_writes_utf8_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path = Path(tmpdir) / "nested" / "data" / "index.json"

            write_json(json_path, {"title": "Árvíztűrő tükörfúrógép"})

            self.assertTrue(json_path.exists())
            raw = json_path.read_text(encoding="utf-8")
            self.assertIn('  "title": "Árvíztűrő tükörfúrógép"', raw)
            self.assertEqual(json.loads(raw), {"title": "Árvíztűrő tükörfúrógép"})


class BuildSiteTests(unittest.TestCase):
    def test_build_site_renders_topic_home_legal_pages_and_navigation_data(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            registry_path = repo_root / "registry.json"
            template_dir = repo_root / "templates"
            asset_dir = repo_root / "assets-src"
            static_content_dir = repo_root / "static-src"
            output_dir = repo_root / "dist"
            markdown_path = repo_root / "01_Grundlagen" / "01_ASCII" / "README.md"

            template_dir.mkdir()
            asset_dir.mkdir()
            (static_content_dir / ".well-known").mkdir(parents=True)
            markdown_path.parent.mkdir(parents=True)
            output_dir.mkdir()

            _write_registry(registry_path)
            _write_templates(template_dir)
            markdown_path.write_text(
                "# ASCII\n\n## Lényeg 30 másodpercben\n\nAz ASCII egy karakterkodolas.",
                encoding="utf-8",
            )
            (asset_dir / "site.css").write_text("body { color: black; }", encoding="utf-8")
            (static_content_dir / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
            (static_content_dir / ".well-known" / "security.txt").write_text(
                "Contact: https://example.test/issues\n",
                encoding="utf-8",
            )
            (output_dir / "stale.txt").write_text("remove me", encoding="utf-8")

            settings = BuildSettings(
                repo_root=repo_root,
                registry_path=registry_path,
                template_dir=template_dir,
                asset_dir=asset_dir,
                static_content_dir=static_content_dir,
                output_dir=output_dir,
                i18n_dir=repo_root / "i18n",
                legal_content_dir=repo_root / "legal",
            )

            ui_strings = {
                "lang": "en",
                "project_tagline": "Study faster",
                "home_title": "CoderLAP",
                "home_intro": "A focused LAP study site.",
            }
            legal_pages = {
                "imprint": "# Imprint\n\nOwner",
                "privacy": "# Privacy\n\nRules",
            }

            result = build_site(settings, ui_strings, legal_pages)

            self.assertEqual(result, output_dir)
            self.assertFalse((output_dir / "stale.txt").exists())
            self.assertTrue((output_dir / "assets" / "site.css").exists())
            self.assertTrue((output_dir / "robots.txt").exists())
            self.assertTrue((output_dir / ".well-known" / "security.txt").exists())
            self.assertTrue((output_dir / "index.html").exists())
            self.assertTrue((output_dir / "topics" / "01-01-ascii" / "index.html").exists())
            self.assertTrue((output_dir / "imprint" / "index.html").exists())
            self.assertTrue((output_dir / "privacy" / "index.html").exists())

            topic_html = (output_dir / "topics" / "01-01-ascii" / "index.html").read_text(encoding="utf-8")
            home_html = (output_dir / "index.html").read_text(encoding="utf-8")
            imprint_html = (output_dir / "imprint" / "index.html").read_text(encoding="utf-8")
            privacy_html = (output_dir / "privacy" / "index.html").read_text(encoding="utf-8")

            self.assertIn('data-topic-id="LAP-01-01"', topic_html)
            self.assertIn('<html lang="hu">', topic_html)
            self.assertIn("<h1>ASCII</h1>", topic_html)
            self.assertNotIn("Lényeg 30 másodpercben", topic_html)
            self.assertIn('<html lang="en">', home_html)
            self.assertIn("CoderLAP", home_html)
            self.assertIn("<h1>Imprint</h1>", imprint_html)
            self.assertIn("<h1>Privacy</h1>", privacy_html)

            topic_index = json.loads((output_dir / "data" / "topic-index.json").read_text(encoding="utf-8"))
            navigation = json.loads((output_dir / "data" / "navigation.json").read_text(encoding="utf-8"))

            self.assertEqual(
                topic_index,
                [
                    {
                        "id": "LAP-01-01",
                        "title": "ASCII",
                        "slug": "01-01-ascii",
                        "main_topic_number": "01",
                        "main_topic_label": "01_Grundlagen",
                        "subtopic_label": "01_ASCII",
                        "source_count": 2,
                        "review_status": "draft",
                        "translation_status": "not_started",
                    }
                ],
            )
            self.assertEqual(navigation["main_topics"][0]["number"], "01")
            self.assertEqual(navigation["topics"]["LAP-01-01"]["slug"], "01-01-ascii")


if __name__ == "__main__":
    unittest.main()
