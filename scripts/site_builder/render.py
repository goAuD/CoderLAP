from __future__ import annotations

from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markdown import markdown


_ALLOWED_TAGS = {
    "a",
    "blockquote",
    "br",
    "code",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "li",
    "ol",
    "p",
    "pre",
    "strong",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
}

_ALLOWED_ATTRIBUTES = {
    "a": {"href", "title"},
    "code": {"class"},
    "th": {"colspan", "rowspan"},
    "td": {"colspan", "rowspan"},
}

_SAFE_URL_SCHEMES = {"http", "https", "mailto"}


def _sanitize_url(value: str) -> str:
    candidate = value.strip()
    normalized = "".join(ch for ch in candidate if ch > " " and ch != "\x7f")

    if not normalized:
        return candidate

    if normalized.startswith(("#", "/", "./", "../", "//")):
        return candidate

    scheme = urlsplit(normalized).scheme.lower()
    if scheme and scheme not in _SAFE_URL_SCHEMES:
        return "#"

    return candidate


class _RenderedMarkdownSanitizer(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._escaped_tag_stack: list[str] = []

    def render(self) -> str:
        return "".join(self._parts)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self._escaped_tag_stack:
            self._parts.append(escape(self.get_starttag_text()))
            self._escaped_tag_stack.append(tag)
            return

        if tag not in _ALLOWED_TAGS:
            self._parts.append(escape(self.get_starttag_text()))
            self._escaped_tag_stack.append(tag)
            return

        self._parts.append(self._build_tag(tag, attrs))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self._escaped_tag_stack or tag not in _ALLOWED_TAGS:
            self._parts.append(escape(self.get_starttag_text()))
            return

        self._parts.append(self._build_tag(tag, attrs, self_closing=True))

    def handle_endtag(self, tag: str) -> None:
        if self._escaped_tag_stack:
            self._parts.append(escape(f"</{tag}>"))
            if tag in self._escaped_tag_stack:
                while self._escaped_tag_stack:
                    popped_tag = self._escaped_tag_stack.pop()
                    if popped_tag == tag:
                        break
            return

        if tag in _ALLOWED_TAGS:
            self._parts.append(f"</{tag}>")
            return

        self._parts.append(escape(f"</{tag}>"))

    def handle_data(self, data: str) -> None:
        self._parts.append(escape(data))

    def handle_comment(self, data: str) -> None:
        self._parts.append(escape(f"<!--{data}-->"))

    def handle_decl(self, decl: str) -> None:
        self._parts.append(escape(f"<!{decl}>"))

    def handle_pi(self, data: str) -> None:
        self._parts.append(escape(f"<?{data}>"))

    def _build_tag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
        *,
        self_closing: bool = False,
    ) -> str:
        allowed_attrs = _ALLOWED_ATTRIBUTES.get(tag, set())
        rendered_attrs: list[str] = []

        for name, value in attrs:
            if name not in allowed_attrs:
                continue

            if value is None:
                continue

            sanitized_value = _sanitize_url(value) if name in {"href", "src"} else value
            rendered_attrs.append(f'{name}="{escape(sanitized_value, quote=True)}"')

        suffix = " />" if self_closing else ">"
        if rendered_attrs:
            return f"<{tag} {' '.join(rendered_attrs)}{suffix}"
        return f"<{tag}{suffix}"


def render_markdown(markdown_text: str) -> str:
    rendered_html = markdown(
        markdown_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )
    sanitizer = _RenderedMarkdownSanitizer()
    sanitizer.feed(rendered_html)
    sanitizer.close()
    return sanitizer.render()


def build_template_environment(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
