from __future__ import annotations

import unittest
from pathlib import Path


class SiteCssAssetsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(__file__).resolve().parents[1]
        self.base_css = (self.repo_root / "site" / "assets" / "css" / "base.css").read_text(encoding="utf-8")
        self.print_css = (self.repo_root / "site" / "assets" / "css" / "print.css").read_text(encoding="utf-8")

    def test_base_css_defines_required_dark_theme_tokens(self) -> None:
        self.assertIn("--color-bg: #15181c;", self.base_css)
        self.assertIn("--color-text: #c9d1d9;", self.base_css)
        self.assertIn("--color-accent: #5fa7a2;", self.base_css)
        self.assertIn("--divider-line:", self.base_css)

    def test_base_css_uses_local_font_faces(self) -> None:
        self.assertIn('font-family: "Manrope";', self.base_css)
        self.assertIn('font-family: "Source Sans 3";', self.base_css)
        self.assertIn("../fonts/manrope-", self.base_css)
        self.assertIn("../fonts/source-sans-3-", self.base_css)

    def test_print_css_switches_to_light_mode(self) -> None:
        self.assertIn("@media print", self.print_css)
        self.assertIn("color-scheme: light;", self.print_css)
        self.assertIn("--color-bg: #ffffff;", self.print_css)
        self.assertIn("--color-text: #1a1a1a;", self.print_css)


if __name__ == "__main__":
    unittest.main()
