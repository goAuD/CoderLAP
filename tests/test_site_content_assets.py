from __future__ import annotations

import json
from pathlib import Path
import unittest


class SiteContentAssetsTests(unittest.TestCase):
    def test_english_ui_strings_and_legal_content_sources_exist(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]

        ui_path = repo_root / "site" / "i18n" / "en.json"
        imprint_path = repo_root / "site" / "content" / "legal" / "en" / "imprint.md"
        privacy_path = repo_root / "site" / "content" / "legal" / "en" / "privacy.md"
        robots_path = repo_root / "site" / "content" / "static" / "root" / "robots.txt"
        security_txt_path = repo_root / "site" / "content" / "static" / "root" / ".well-known" / "security.txt"

        ui_strings = json.loads(ui_path.read_text(encoding="utf-8"))
        self.assertEqual(ui_strings["project_tagline"], "LAP \u00b7 Software Development \u00b7 Coding")
        self.assertEqual(ui_strings["home_title"], "Austrian LAP study base \u00b7 Software Development, Coding")
        self.assertIn("Search topics", ui_strings["search_placeholder"])
        self.assertEqual(ui_strings["search_label"], "Search")
        self.assertEqual(ui_strings["filter_label"], "Filter")
        self.assertEqual(ui_strings["empty_state_label"], "No topics found.")
        self.assertEqual(ui_strings["sidebar_label"], "Quick view")
        self.assertEqual(ui_strings["primary_navigation_label"], "Primary navigation")
        self.assertEqual(ui_strings["back_to_catalog"], "Back to catalog")
        self.assertEqual(ui_strings["print_label"], "Print topic")
        self.assertEqual(ui_strings["previous_label"], "Previous")
        self.assertEqual(ui_strings["next_label"], "Next")
        self.assertEqual(ui_strings["topic_pagination_label"], "Topic pagination")
        self.assertEqual(ui_strings["imprint_label"], "Imprint")
        self.assertEqual(ui_strings["privacy_label"], "Privacy")

        imprint_text = imprint_path.read_text(encoding="utf-8")
        self.assertIn("# Imprint", imprint_text)
        self.assertIn("## Sources", imprint_text)
        self.assertIn("## Contact", imprint_text)
        self.assertIn("Section 5 ECG", imprint_text)
        self.assertIn("Section 25 MedienG", imprint_text)

        privacy_text = privacy_path.read_text(encoding="utf-8")
        self.assertIn("# Privacy Policy", privacy_text)
        self.assertIn("## Sources", privacy_text)
        self.assertIn("## What data processing can realistically happen right now", privacy_text)
        self.assertIn("coderlap_progress", privacy_text)
        self.assertIn("Cloudflare", privacy_text)
        self.assertIn("Austrian Data Protection Authority", privacy_text)

        robots_text = robots_path.read_text(encoding="utf-8")
        self.assertIn("User-agent: *", robots_text)
        self.assertIn("Disallow: /", robots_text)

        security_txt = security_txt_path.read_text(encoding="utf-8")
        self.assertIn("Contact: https://github.com/goAuD/CoderLAP/issues", security_txt)
        self.assertIn("Canonical: https://coderlap.com/.well-known/security.txt", security_txt)
        self.assertIn("Preferred-Languages: de, hu, en", security_txt)


if __name__ == "__main__":
    unittest.main()
