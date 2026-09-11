from pathlib import Path
import unittest

from jinja2 import UndefinedError

from scripts.site_builder.render import build_template_environment, render_markdown


class RenderTests(unittest.TestCase):
    def test_topic_output_omits_exam_mistakes_and_nested_content_in_both_languages(self):
        for heading in ("Gyakori vizsgahibák", "Häufige Prüfungsfehler"):
            with self.subTest(heading=heading):
                source = (
                    "# Topic\n\nKeep before.\n\n## " + heading
                    + "\n\nOmit this paragraph.\n\n### " + heading
                    + "\n\nOmit nested section.\n\n### Nested detail\n\n- Omit this list."
                    + "\n\n## Self-check\n\nKeep after."
                )
                html = render_markdown(source, suppress_exam_mistakes=True)
                self.assertNotIn(heading, html)
                self.assertNotIn("Omit", html)
                self.assertNotIn("Nested detail", html)
                self.assertIn("Keep before.", html)
                self.assertIn("Keep after.", html)
                self.assertIn(heading, render_markdown(source))

    def test_topic_section_filter_handles_end_of_document_and_keeps_code_examples(self):
        source = (
            "```markdown\n## Gyakori vizsgahibák\nExample heading only.\n```"
            "\n\n## Gyakori vizsgahibák\n\nOmit through the end."
        )
        html = render_markdown(source, suppress_exam_mistakes=True)
        self.assertIn("## Gyakori vizsgahibák", html)
        self.assertIn("Example heading only.", html)
        self.assertNotIn("Omit through the end.", html)

    def test_render_markdown_linkifies_standalone_plain_url_lines(self) -> None:
        html = render_markdown("Source title\nhttps://example.com/path\nUsage note")

        self.assertIn('<a href="https://example.com/path">https://example.com/path</a>', html)

    def test_render_markdown_can_remove_redundant_summary_heading(self) -> None:
        html = render_markdown(
            "# Thema\n\n## Lényeg 30 másodpercben\n\nTartalom",
            suppress_redundant_summary_heading=True,
        )

        self.assertIn("<h1>Thema</h1>", html)
        self.assertNotIn("Lényeg 30 másodpercben", html)
        self.assertIn("<p>Tartalom</p>", html)

    def test_render_markdown_keeps_plain_urls_inside_fenced_code_unlinked(self) -> None:
        html = render_markdown("```text\nhttps://example.com/path\n```")

        self.assertIn("https://example.com/path", html)
        self.assertNotIn('<a href="https://example.com/path">', html)

    def test_render_markdown_escapes_raw_script_content(self) -> None:
        html = render_markdown(
            "# Title\n\n<script>alert(1)</script>",
        )

        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", html)

    def test_render_markdown_neutralizes_javascript_links(self) -> None:
        html = render_markdown("[click me](javascript:alert(1))")

        self.assertIn('<a href="#">click me</a>', html)
        self.assertNotIn("javascript:alert(1)", html)

    def test_render_markdown_preserves_angle_bracket_autolinks(self) -> None:
        html = render_markdown("<https://example.com>\n\n<mailto:test@example.com>")

        self.assertIn('<a href="https://example.com">https://example.com</a>', html)
        self.assertIn('<a href="mailto:test@example.com">test@example.com</a>', html)

    def test_render_markdown_preserves_html_code_examples_without_double_escaping(self) -> None:
        inline_html = render_markdown("`<div class=\"note\">`")
        fenced_html = render_markdown("```html\n<div class=\"note\">Hello</div>\n```")

        self.assertIn('<code>&lt;div class=&quot;note&quot;&gt;</code>', inline_html)
        self.assertNotIn("&amp;lt;", inline_html)
        self.assertIn("&lt;div class=&quot;note&quot;&gt;Hello&lt;/div&gt;", fenced_html)
        self.assertNotIn("&amp;lt;", fenced_html)

    def test_render_markdown_preserves_indented_html_code_without_double_escaping(self) -> None:
        html = render_markdown("    <div class=\"note\">")

        self.assertIn("&lt;div class=&quot;note&quot;&gt;", html)
        self.assertNotIn("&amp;lt;", html)

    def test_render_markdown_preserves_declarations_and_processing_instructions_as_text(self) -> None:
        html = render_markdown("<!DOCTYPE html>\n\n<?xml version=\"1.0\"?>")

        self.assertIn("&lt;!DOCTYPE html&gt;", html)
        self.assertIn('&lt;?xml version=&quot;1.0&quot;?&gt;', html)

    def test_render_markdown_recovers_after_malformed_inline_raw_html(self) -> None:
        html = render_markdown("prefix <div>oops\n\n# After")

        self.assertIn("prefix &lt;div&gt;oops", html)
        self.assertIn("<h1>After</h1>", html)

    def test_render_markdown_recovers_after_malformed_inline_script(self) -> None:
        html = render_markdown("prefix <script>alert(1)\n\n# After")

        self.assertIn("prefix &lt;script&gt;alert(1)", html)
        self.assertIn("<h1>After</h1>", html)

    def test_real_templates_render_with_required_context(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        templates = repo_root / "site" / "templates"

        env = build_template_environment(templates)
        html = env.get_template("home.html").render(
            ui_lang="hu",
            page_lang="hu",
            page_title="CoderLAP",
            asset_prefix="/assets",
            body_class="home-page",
            ui={
                "project_tagline": "Austrian LAP study base",
                "home_title": "Kezdőlap",
                "home_intro": "Hungarian source content rendered through Jinja.",
            },
        )

        self.assertIn('<link rel="stylesheet" href="/assets/css/base.css?v=0">', html)
        self.assertIn('<link rel="stylesheet" href="/assets/css/print.css?v=0" media="print">', html)
        self.assertIn('<script src="/assets/js/site.js?v=0" defer></script>', html)
        self.assertIn("Kezdőlap", html)
        self.assertIn('<html lang="hu">', html)

    def test_shared_assets_use_the_current_build_version(self) -> None:
        templates = Path(__file__).resolve().parents[1] / "site" / "templates"
        env = build_template_environment(templates)
        html = env.get_template("base.html").render(
            ui_lang="de", page_title="CoderLAP", asset_prefix="/assets",
            body_class="home-page", ui={}, cache_bust="release-42",
        )

        for asset in ("favicon.svg", "css/base.css", "css/layout.css",
                      "css/components.css", "css/print.css", "js/site.js"):
            with self.subTest(asset=asset):
                self.assertIn(f'/assets/{asset}?v=release-42"', html)
                self.assertNotIn(f'/assets/{asset}"', html)
        self.assertIn('src="/assets/favicon.svg?v=release-42"', html)

    def test_legal_template_uses_shared_main_landmark_only(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        templates = repo_root / "site" / "templates"

        env = build_template_environment(templates)
        html = env.get_template("legal.html").render(
            ui_lang="en",
            page_lang="en",
            page_title="Imprint",
            asset_prefix="/assets",
            body_class="legal-page",
            ui={
                "project_tagline": "Austrian LAP study base",
                "imprint_label": "Imprint",
                "privacy_label": "Privacy",
            },
            content_html="<h1>Imprint</h1>",
            navigation={},
        )

        self.assertEqual(html.count("<main"), 1)
        self.assertIn('<section class="page-shell">', html)

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
