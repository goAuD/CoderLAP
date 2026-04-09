from pathlib import Path
import unittest

from jinja2 import UndefinedError

from scripts.site_builder.render import build_template_environment, render_markdown


class RenderTests(unittest.TestCase):
    def test_render_markdown_escapes_raw_html_while_supporting_tables_and_code(self) -> None:
        html = render_markdown(
            "# Title\n\n<script>alert(1)</script>\n\n| A | B |\n| - | - |\n| 1 | 2 |\n\n`code`",
        )

        self.assertIn("<table>", html)
        self.assertIn("<code>code</code>", html)
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", html)

    def test_real_templates_render_with_required_context(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        templates = repo_root / "site" / "templates"

        env = build_template_environment(templates)
        html = env.get_template("home.html").render(
            ui_lang="hu",
            page_title="CoderLAP",
            asset_prefix="/assets",
            body_class="home-page",
            ui={
                "project_tagline": "Austrian LAP study base",
                "home_title": "Kezdőlap",
                "home_intro": "Hungarian source content rendered through Jinja.",
            },
        )

        self.assertIn('<link rel="stylesheet" href="/assets/css/base.css">', html)
        self.assertIn('<link rel="stylesheet" href="/assets/css/print.css" media="print">', html)
        self.assertIn('<script src="/assets/js/site.js" defer></script>', html)
        self.assertIn("Kezdőlap", html)

    def test_real_templates_fail_when_required_context_is_missing(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        templates = repo_root / "site" / "templates"

        env = build_template_environment(templates)

        with self.assertRaises(UndefinedError):
            env.get_template("home.html").render(
                ui_lang="hu",
                page_title="CoderLAP",
                asset_prefix="/assets",
                body_class="home-page",
            )


if __name__ == "__main__":
    unittest.main()
