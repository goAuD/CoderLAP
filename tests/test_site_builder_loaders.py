from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.site_builder.loaders import load_registry_items, load_topic_markdown
from scripts.site_builder.models import TopicRecord


class TopicRecordTests(unittest.TestCase):
    def test_absolute_markdown_path_joins_repo_root_and_relative_path(self) -> None:
        record = TopicRecord(
            id="LAP-11-02",
            lang="hu",
            title="Példa",
            path="11_Informatik/02_Pelda/README.md",
            main_topic_number="11",
            main_topic_dir="11_Informatik",
            subtopic_number="02",
            subtopic_dir="02_Pelda",
            slug="11-02-pelda",
            review_status="draft",
            translation_status="not_started",
            source_count=3,
            opened_at="2026-04-09",
            canonical=True,
        )

        self.assertEqual(
            record.absolute_markdown_path(Path("C:/GitHub/CoderLAP")),
            Path("C:/GitHub/CoderLAP/11_Informatik/02_Pelda/README.md"),
        )

    def test_absolute_markdown_path_rejects_absolute_or_escaped_paths(self) -> None:
        repo_root = Path("C:/GitHub/CoderLAP")
        absolute_record = TopicRecord(
            id="LAP-11-02",
            lang="hu",
            title="Példa",
            path="C:/GitHub/Other/README.md",
            main_topic_number="11",
            main_topic_dir="11_Informatik",
            subtopic_number="02",
            subtopic_dir="02_Pelda",
            slug="11-02-pelda",
            review_status="draft",
            translation_status="not_started",
            source_count=3,
            opened_at="2026-04-09",
            canonical=True,
        )
        escaped_record = TopicRecord(
            id="LAP-11-03",
            lang="hu",
            title="Másik",
            path="../outside/README.md",
            main_topic_number="11",
            main_topic_dir="11_Informatik",
            subtopic_number="03",
            subtopic_dir="03_Masik",
            slug="11-03-masik",
            review_status="draft",
            translation_status="not_started",
            source_count=1,
            opened_at="2026-04-09",
            canonical=True,
        )

        with self.assertRaises(ValueError):
            absolute_record.absolute_markdown_path(repo_root)

        with self.assertRaises(ValueError):
            escaped_record.absolute_markdown_path(repo_root)


class LoaderTests(unittest.TestCase):
    def test_load_registry_items_returns_only_canonical_items_sorted(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            registry_path = Path(tmpdir) / "registry.json"
            registry_path.write_text(
                json.dumps(
                    {
                        "items": [
                            {
                                "id": "LAP-02-10",
                                "lang": "hu",
                                "title": "Later",
                                "path": "02_B/10/README.md",
                                "main_topic_number": "02",
                                "main_topic_dir": "02_B",
                                "subtopic_number": "10",
                                "subtopic_dir": "10",
                                "slug": "02-10-later",
                                "review_status": "draft",
                                "translation_status": "not_started",
                                "source_count": 1,
                                "opened_at": None,
                                "canonical": True,
                            },
                            {
                                "id": "LAP-01-02",
                                "lang": "hu",
                                "title": "Skip",
                                "path": "01_A/02/README.md",
                                "main_topic_number": "01",
                                "main_topic_dir": "01_A",
                                "subtopic_number": "02",
                                "subtopic_dir": "02",
                                "slug": "01-02-skip",
                                "review_status": "draft",
                                "translation_status": "not_started",
                                "source_count": 1,
                                "opened_at": None,
                                "canonical": False,
                            },
                            {
                                "id": "LAP-01-01",
                                "lang": "hu",
                                "title": "First",
                                "path": "01_A/01/README.md",
                                "main_topic_number": "01",
                                "main_topic_dir": "01_A",
                                "subtopic_number": "01",
                                "subtopic_dir": "01",
                                "slug": "01-01-first",
                                "review_status": "draft",
                                "translation_status": "not_started",
                                "source_count": 2,
                                "opened_at": "2026-04-09",
                                "canonical": True,
                            },
                        ]
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )

            records = load_registry_items(registry_path)

        self.assertEqual([record.id for record in records], ["LAP-01-01", "LAP-02-10"])
        self.assertTrue(all(isinstance(record, TopicRecord) for record in records))
        self.assertTrue(all(record.canonical for record in records))

    def test_load_registry_items_skips_malformed_noncanonical_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            registry_path = Path(tmpdir) / "registry.json"
            registry_path.write_text(
                json.dumps(
                    {
                        "items": [
                            {
                                "id": "LAP-01-99",
                                "canonical": False,
                            },
                            {
                                "id": "LAP-01-01",
                                "lang": "hu",
                                "title": "First",
                                "path": "01_A/01/README.md",
                                "main_topic_number": "01",
                                "main_topic_dir": "01_A",
                                "subtopic_number": "01",
                                "subtopic_dir": "01",
                                "slug": "01-01-first",
                                "review_status": "draft",
                                "translation_status": "not_started",
                                "source_count": 2,
                                "opened_at": "2026-04-09",
                                "canonical": True,
                            },
                        ]
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )

            records = load_registry_items(registry_path)

        self.assertEqual([record.id for record in records], ["LAP-01-01"])

    def test_load_registry_items_rejects_malformed_registry_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            registry_path = Path(tmpdir) / "registry.json"
            registry_path.write_text(
                json.dumps(
                    {
                        "items": [
                            {
                                "id": "LAP-01-01",
                                "canonical": True,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "missing required fields"):
                load_registry_items(registry_path)

        with tempfile.TemporaryDirectory() as tmpdir:
            registry_path = Path(tmpdir) / "registry.json"
            registry_path.write_text(json.dumps({"version": 1}), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "items"):
                load_registry_items(registry_path)

    def test_load_topic_markdown_reads_utf8_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            markdown_path = Path(tmpdir) / "README.md"
            markdown_path.write_text("# Cím\n\nÁrvíztűrő tükörfúrógép", encoding="utf-8")

            self.assertEqual(load_topic_markdown(markdown_path), "# Cím\n\nÁrvíztűrő tükörfúrógép")
