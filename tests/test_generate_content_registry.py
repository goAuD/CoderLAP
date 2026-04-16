from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import scripts.generate_content_registry as registry_module
from scripts.generate_content_registry import RegistryItem, _read_markdown, get_translation_status, write_json


class GenerateContentRegistryTests(unittest.TestCase):
    def test_get_translation_status_returns_de_missing_without_german_sidecar(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            subtopic_dir = Path(tmpdir)
            (subtopic_dir / "README.md").write_text("# Topic\n", encoding="utf-8")

            self.assertEqual(get_translation_status(subtopic_dir), "de_missing")

    def test_get_translation_status_returns_de_complete_when_german_sidecar_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            subtopic_dir = Path(tmpdir)
            (subtopic_dir / "README.md").write_text("# Topic\n", encoding="utf-8")
            (subtopic_dir / "README.de.md").write_text("# Thema\n", encoding="utf-8")

            self.assertEqual(get_translation_status(subtopic_dir), "de_complete")

    def test_write_json_uses_portable_source_root_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "registry.json"
            items = [
                RegistryItem(
                    id="LAP-01-01",
                    lang="hu",
                    title="ASCII",
                    path="01_Topic/01_Subtopic/README.md",
                    main_topic_number="01",
                    main_topic_dir="01_Topic",
                    subtopic_number="01",
                    subtopic_dir="01_Subtopic",
                    slug="01-01-ascii",
                    review_status="draft",
                    translation_status="de_complete",
                    source_count=1,
                    opened_at="2026-04-12",
                    canonical=True,
                )
            ]

            with patch.object(registry_module, "OUTPUT_JSON", output_path):
                write_json(items)

            payload = output_path.read_text(encoding="utf-8")
            self.assertIn('"source_root": "."', payload)
            self.assertIn('"translation_status": "de_complete"', payload)


    def test_read_markdown_raises_value_error_for_invalid_utf8(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            bad_path = Path(tmpdir) / "README.md"
            bad_path.write_bytes(b"\x80\x81\x82 invalid bytes")

            with self.assertRaises(ValueError) as cm:
                _read_markdown(bad_path)
            self.assertIn("Invalid UTF-8", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
