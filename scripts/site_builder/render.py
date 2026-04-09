from __future__ import annotations

from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re
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
_FENCED_CODE_BLOCK_RE = re.compile(r"^[ ]{0,3}(```+|~~~+)")
_RAW_HTML_START_RE = re.compile(r"</?[A-Za-z][^>]*|<![^>]*>|<\?[^>]*\?>")
_RAW_HTML_SELF_CONTAINED_RE = re.compile(r"^[ ]{0,3}<([A-Za-z][A-Za-z0-9-]*)\b[^>]*>.*</\1>[ ]*$")
_RAW_HTML_START_TAG_RE = re.compile(r"^[ ]{0,3}<([A-Za-z][A-Za-z0-9-]*)\b[^>]*>[ ]*$")
_VOID_HTML_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


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


def _neutralize_raw_html_block_starts(markdown_text: str) -> str:
    lines = markdown_text.splitlines(keepends=True)
    in_fenced_code_block = False
    in_raw_html_block = False
    processed_lines: list[str] = []

    for index, line in enumerate(lines):
        if _FENCED_CODE_BLOCK_RE.match(line):
            in_fenced_code_block = not in_fenced_code_block
            in_raw_html_block = False
            processed_lines.append(line)
            continue

        if in_fenced_code_block:
            processed_lines.append(line)
            continue

        stripped_line = line.rstrip("\r\n")

        if in_raw_html_block:
            if not stripped_line.strip():
                in_raw_html_block = False
                processed_lines.append(line)
            else:
                trailing_newline = line[len(stripped_line) :]
                processed_lines.append(f"{escape(stripped_line)}{trailing_newline}")
            continue

        raw_html_start_index = _find_raw_html_start_outside_inline_code(stripped_line)
        if raw_html_start_index is None:
            processed_lines.append(line)
            continue

        trailing_newline = line[len(stripped_line) :]
        prefix = stripped_line[:raw_html_start_index]
        raw_fragment = stripped_line[raw_html_start_index:]
        processed_lines.append(f"{prefix}{escape(raw_fragment)}{trailing_newline}")
        if _is_self_contained_raw_html_line(raw_fragment):
            if (
                trailing_newline
                and index + 1 < len(lines)
                and lines[index + 1].strip()
            ):
                processed_lines.append(trailing_newline)
        else:
            in_raw_html_block = True

    return "".join(processed_lines)


def _is_self_contained_raw_html_line(line: str) -> bool:
    stripped = line.strip()

    if stripped.startswith(("<?", "<!")):
        return True

    if stripped.startswith("</"):
        return True

    start_tag_match = _RAW_HTML_START_TAG_RE.match(line)
    if start_tag_match and start_tag_match.group(1).lower() in _VOID_HTML_TAGS:
        return True

    if stripped.endswith("/>"):
        return True

    return bool(_RAW_HTML_SELF_CONTAINED_RE.match(line))


def _find_raw_html_start_outside_inline_code(line: str) -> int | None:
    index = 0
    active_backtick_run: int | None = None

    while index < len(line):
        if line[index] == "`":
            run_length = 1
            while index + run_length < len(line) and line[index + run_length] == "`":
                run_length += 1

            if active_backtick_run is None:
                active_backtick_run = run_length
            elif active_backtick_run == run_length:
                active_backtick_run = None

            index += run_length
            continue

        if active_backtick_run is None and line[index] == "<":
            match = _RAW_HTML_START_RE.match(line[index:])
            if match:
                return index

        index += 1

    return None


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
    markdown_text = _neutralize_raw_html_block_starts(markdown_text)
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
