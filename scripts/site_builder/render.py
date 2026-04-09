from __future__ import annotations

from html import escape
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markdown import markdown


def render_markdown(markdown_text: str) -> str:
    return markdown(
        escape(markdown_text),
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def build_template_environment(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
