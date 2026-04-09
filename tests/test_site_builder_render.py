from pathlib import Path
import tempfile
import unittest

from scripts.site_builder.render import build_template_environment, render_markdown


class RenderTests(unittest.TestCase):
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
