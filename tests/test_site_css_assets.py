from __future__ import annotations

import unittest
from pathlib import Path


class SiteCssAssetsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(__file__).resolve().parents[1]
        self.base_css = (self.repo_root / "site" / "assets" / "css" / "base.css").read_text(encoding="utf-8")
        self.components_css = (self.repo_root / "site" / "assets" / "css" / "components.css").read_text(encoding="utf-8")
        self.print_css = (self.repo_root / "site" / "assets" / "css" / "print.css").read_text(encoding="utf-8")
        self.base_html = (self.repo_root / "site" / "templates" / "base.html").read_text(encoding="utf-8")

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

    def test_base_html_includes_skip_link_and_main_landmark(self) -> None:
        self.assertIn('<a class="skip-link" href="#main-content">Skip to content</a>', self.base_html)
        self.assertLess(
            self.base_html.index('<a class="skip-link" href="#main-content">Skip to content</a>'),
            self.base_html.index('<header class="site-topbar">'),
        )
        self.assertIn('<main id="main-content" class="site-main" tabindex="-1">', self.base_html)
        self.assertIn('<nav class="site-topbar__nav"', self.base_html)

    def test_components_css_reveals_skip_link_for_keyboard_focus(self) -> None:
        self.assertRegex(
            self.components_css,
            r"\.skip-link\s*\{\s*"
            r"position: absolute;\s*"
            r"top: var\(--space-3\);\s*"
            r"left: var\(--space-4\);\s*"
            r"z-index: 30;\s*"
            r"padding: 0\.75rem 1rem;\s*"
            r"border-radius: 999px;\s*"
            r"background: var\(--color-surface-raised\);\s*"
            r"box-shadow: var\(--shadow-button\);"
            r"[^}]*transform: translateY\(-140%\);",
        )
        self.assertRegex(
            self.components_css,
            r"\.skip-link:focus,\s*\.skip-link:focus-visible\s*\{\s*transform: translateY\(0\);",
        )

    def test_base_css_keeps_universal_reduced_motion_override_inside_media_block(self) -> None:
        self.assertRegex(
            self.base_css,
            r"(?s)@media \(prefers-reduced-motion: reduce\)\s*\{\s*"
            r"html\s*\{\s*scroll-behavior: auto;\s*\}\s*"
            r"\*,\s*\*::before,\s*\*::after\s*\{\s*"
            r"animation-duration: 0\.01ms !important;\s*"
            r"animation-iteration-count: 1 !important;\s*"
            r"scroll-behavior: auto !important;\s*"
            r"transition-duration: 0\.01ms !important;\s*"
            r"\}\s*"
            r"button,\s*\.button,\s*\[role=\"button\"\]\s*\{\s*"
            r"transform: none !important;\s*"
            r"\}\s*\}",
        )


if __name__ == "__main__":
    unittest.main()
