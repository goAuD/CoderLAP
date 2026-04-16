from __future__ import annotations

import json
import re
import shutil
import time
import unicodedata
from pathlib import Path
from typing import Any

from .loaders import load_registry_items, load_topic_markdown
from .navigation import build_navigation
from .render import build_template_environment, render_markdown
from .settings import BuildSettings, LanguageConfig

SEARCH_ALIASES_RELATIVE_PATH = Path("site/content/search/search_aliases.json")
MARKDOWN_HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
GENERIC_SEARCH_HEADINGS = {
    "lenyeg 30 masodpercben",
    "gyors vizualis kep",
    "mi az",
    "miert fontos",
    "mit nem tud mire kell figyelni",
    "mire kell figyelni",
    "vizsgan jol hasznalhato megfogalmazas",
    "gyakori vizsgahibak",
    "gyors onellenorzes",
    "rovid valaszok az onellenorzeshez",
    "forrasok",
    "schneller visueller uberblick",
    "zusammenfassung in 30 sekunden",
    "warum ist das wichtig",
    "worauf muss man achten",
    "prufungstaugliche formulierung",
    "haufige prufungsfehler",
    "schnelle selbstkontrolle",
    "kurzantworten zur selbstkontrolle",
    "quellen",
}


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _normalize_search_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    without_marks = "".join(char for char in normalized if not unicodedata.combining(char))
    cleaned = without_marks.lower().replace("ß", "ss")
    cleaned = re.sub(r"[_/\\.-]+", " ", cleaned)
    cleaned = re.sub(r"[`*_>#:+|()\[\]{}\"'?!,;]+", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def _display_label(label: str) -> str:
    return re.sub(r"^\d+_", "", str(label or "")).replace("_", " ").strip()


def _dedupe_terms(terms: list[str]) -> list[str]:
    unique_terms: list[str] = []
    seen: set[str] = set()
    for term in terms:
        cleaned = re.sub(r"\s+", " ", str(term or "").strip())
        normalized = _normalize_search_text(cleaned)
        if not cleaned or not normalized or normalized in seen:
            continue
        seen.add(normalized)
        unique_terms.append(cleaned)
    return unique_terms


def _extract_search_headings(markdown_text: str) -> list[str]:
    headings: list[str] = []
    for _, raw_heading in MARKDOWN_HEADING_PATTERN.findall(markdown_text):
        cleaned = re.sub(r"\s+", " ", raw_heading.replace("`", "").strip())
        normalized = _normalize_search_text(cleaned)
        if not normalized or normalized in GENERIC_SEARCH_HEADINGS:
            continue
        headings.append(cleaned)
    return headings


def _topic_markdown_variants(topic, repo_root: Path) -> list[Path]:
    base_path = topic.absolute_markdown_path(repo_root)
    candidates = [base_path]
    for lang_code in ("de", "hu"):
        lang_path = base_path.with_suffix(f".{lang_code}.md")
        if lang_path not in candidates:
            candidates.append(lang_path)
    return [candidate for candidate in candidates if candidate.is_file()]


def _topic_search_terms(topic, repo_root: Path) -> list[str]:
    terms = [
        topic.id,
        topic.title,
        topic.slug.replace("-", " "),
        topic.main_topic_number,
        topic.main_topic_dir,
        _display_label(topic.main_topic_dir),
        topic.subtopic_number,
        topic.subtopic_dir,
        _display_label(topic.subtopic_dir),
    ]
    for markdown_path in _topic_markdown_variants(topic, repo_root):
        markdown_text = load_topic_markdown(markdown_path)
        terms.extend(_extract_search_headings(markdown_text))
    return _dedupe_terms(terms)


def _load_search_alias_groups(repo_root: Path) -> list[list[str]]:
    alias_path = repo_root / SEARCH_ALIASES_RELATIVE_PATH
    if not alias_path.is_file():
        return []

    payload = json.loads(alias_path.read_text(encoding="utf-8"))
    groups = payload.get("groups", [])
    if not isinstance(groups, list):
        raise ValueError("Search alias payload must contain a 'groups' list.")

    normalized_groups: list[list[str]] = []
    for group in groups:
        if not isinstance(group, list):
            raise ValueError("Each search alias group must be a list.")
        if not all(isinstance(term, str) for term in group):
            raise ValueError("Search alias groups may only contain strings.")
        deduped = _dedupe_terms(group)
        if len(deduped) >= 2:
            normalized_groups.append(deduped)
    return normalized_groups


def _topic_index_entry(topic, repo_root: Path) -> dict[str, Any]:
    return {
        "id": topic.id,
        "title": topic.title,
        "slug": topic.slug,
        "main_topic_number": topic.main_topic_number,
        "main_topic_label": topic.main_topic_dir,
        "subtopic_label": topic.subtopic_dir,
        "source_count": topic.source_count,
        "review_status": topic.review_status,
        "translation_status": topic.translation_status,
        "search_terms": _topic_search_terms(topic, repo_root),
    }


def _recreate_output_dir(output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


def _load_legal_pages(legal_dir: Path) -> dict[str, str]:
    pages: dict[str, str] = {}
    if legal_dir.is_dir():
        for md_file in sorted(legal_dir.glob("*.md")):
            pages[md_file.stem] = md_file.read_text(encoding="utf-8")
    return pages


def _language_href(lang_config: LanguageConfig, relative_path: str = "") -> str:
    clean_path = relative_path.strip("/")
    if lang_config.is_default:
        return f"/{clean_path}/" if clean_path else "/"
    return f"/{lang_config.code}/{clean_path}/" if clean_path else f"/{lang_config.code}/"


def _build_lang_switcher(
    all_languages: tuple[LanguageConfig, ...],
    current_lang_code: str,
    relative_path: str = "",
) -> list[dict[str, str | bool]]:
    items: list[dict[str, str | bool]] = []
    for lang_config in all_languages:
        items.append(
            {
                "code": lang_config.code,
                "label": lang_config.code.upper(),
                "href": _language_href(lang_config, relative_path),
                "is_current": lang_config.code == current_lang_code,
            }
        )
    return items


def _build_language(
    lang_config: LanguageConfig,
    settings: BuildSettings,
    all_languages: tuple[LanguageConfig, ...],
    topics: list,
    topic_index: list[dict[str, Any]],
    search_alias_groups: list[list[str]],
    navigation: dict,
    env: Any,
    cache_bust: str,
) -> None:
    ui_strings = json.loads(lang_config.i18n_file.read_text(encoding="utf-8"))
    legal_pages = _load_legal_pages(lang_config.legal_content_dir)

    ui_lang = lang_config.code

    if lang_config.is_default:
        lang_output = settings.output_dir
        asset_prefix = "/assets"
        site_root = "/"
    else:
        lang_output = settings.output_dir / lang_config.code
        asset_prefix = "/assets"
        site_root = f"/{lang_config.code}/"

    lang_output.mkdir(parents=True, exist_ok=True)

    common_ctx = {
        "ui_lang": ui_lang,
        "asset_prefix": asset_prefix,
        "ui": ui_strings,
        "navigation": navigation,
        "cache_bust": cache_bust,
        "site_root": site_root,
        "current_lang": lang_config.code,
    }

    for topic in topics:
        md_path = topic.absolute_markdown_path(settings.repo_root)
        # Prefer language-specific file (e.g. README.de.md) over default README.md
        lang_md_path = md_path.with_suffix(f".{lang_config.code}.md")
        if lang_md_path.is_file():
            markdown_text = load_topic_markdown(lang_md_path)
        else:
            markdown_text = load_topic_markdown(md_path)
        content_html = render_markdown(
            markdown_text,
            suppress_redundant_summary_heading=True,
        )
        rendered = env.get_template("topic.html").render(
            **common_ctx,
            page_lang=topic.lang,
            page_title=topic.title,
            body_class="topic-page",
            topic=topic,
            content_html=content_html,
            topic_index=topic_index,
            lang_switcher=_build_lang_switcher(all_languages, lang_config.code, f"topics/{topic.slug}"),
        )
        _write_text(lang_output / "topics" / topic.slug / "index.html", rendered)

    home_html = env.get_template("home.html").render(
        **common_ctx,
        page_lang=ui_lang,
        page_title=ui_strings.get("home_title", "CoderLAP"),
        body_class="home-page",
        topic_index=topic_index,
        search_alias_groups=search_alias_groups,
        lang_switcher=_build_lang_switcher(all_languages, lang_config.code),
    )
    _write_text(lang_output / "index.html", home_html)

    for slug, markdown_text in legal_pages.items():
        rendered = env.get_template("legal.html").render(
            **common_ctx,
            page_lang=ui_lang,
            page_title=slug.title(),
            body_class="legal-page",
            legal_slug=slug,
            content_html=render_markdown(markdown_text),
            lang_switcher=_build_lang_switcher(all_languages, lang_config.code, slug),
        )
        _write_text(lang_output / slug / "index.html", rendered)

    write_json(lang_output / "data" / "topic-index.json", topic_index)
    write_json(lang_output / "data" / "navigation.json", navigation)


def build_site(
    settings: BuildSettings,
    ui_strings: dict[str, Any] | None = None,
    legal_pages: dict[str, str] | None = None,
) -> Path:
    topics = load_registry_items(settings.registry_path)
    navigation = build_navigation(topics)
    env = build_template_environment(settings.template_dir)
    topic_index = [_topic_index_entry(topic, settings.repo_root) for topic in topics]
    search_alias_groups = _load_search_alias_groups(settings.repo_root)

    _recreate_output_dir(settings.output_dir)
    shutil.copytree(settings.asset_dir, settings.output_dir / "assets")
    if settings.static_content_dir.is_dir():
        shutil.copytree(settings.static_content_dir, settings.output_dir, dirs_exist_ok=True)

    cache_bust = str(int(time.time()))

    if settings.languages:
        for lang_config in settings.languages:
            _build_language(
                lang_config, settings, settings.languages,
                topics, topic_index, search_alias_groups, navigation, env, cache_bust,
            )
    else:
        # Legacy single-language fallback
        if ui_strings is None or legal_pages is None:
            raise ValueError("ui_strings and legal_pages are required for single-language builds")
        _build_single_language(
            settings, ui_strings, legal_pages,
            topics, topic_index, search_alias_groups, navigation, env, cache_bust,
        )

    return settings.output_dir


def _build_single_language(
    settings: BuildSettings,
    ui_strings: dict[str, Any],
    legal_pages: dict[str, str],
    topics: list,
    topic_index: list[dict[str, Any]],
    search_alias_groups: list[list[str]],
    navigation: dict,
    env: Any,
    cache_bust: str,
) -> None:
    """Legacy single-language build path for backward compatibility."""
    ui_lang = str(ui_strings.get("lang", "en"))
    asset_prefix = "/assets"

    for topic in topics:
        markdown_text = load_topic_markdown(topic.absolute_markdown_path(settings.repo_root))
        content_html = render_markdown(
            markdown_text,
            suppress_redundant_summary_heading=True,
        )
        rendered = env.get_template("topic.html").render(
            ui_lang=ui_lang,
            page_lang=topic.lang,
            page_title=topic.title,
            asset_prefix=asset_prefix,
            body_class="topic-page",
            ui=ui_strings,
            topic=topic,
            content_html=content_html,
            navigation=navigation,
            topic_index=topic_index,
            cache_bust=cache_bust,
            site_root="/",
            lang_switcher=[],
            current_lang=ui_lang,
        )
        _write_text(settings.output_dir / "topics" / topic.slug / "index.html", rendered)

    home_html = env.get_template("home.html").render(
        ui_lang=ui_lang,
        page_lang=ui_lang,
        page_title=ui_strings.get("home_title", "CoderLAP"),
        asset_prefix=asset_prefix,
        body_class="home-page",
        ui=ui_strings,
        navigation=navigation,
        topic_index=topic_index,
        search_alias_groups=search_alias_groups,
        cache_bust=cache_bust,
        site_root="/",
        lang_switcher=[],
        current_lang=ui_lang,
    )
    _write_text(settings.output_dir / "index.html", home_html)

    for slug, markdown_text in legal_pages.items():
        rendered = env.get_template("legal.html").render(
            ui_lang=ui_lang,
            page_lang=ui_lang,
            page_title=slug.title(),
            asset_prefix=asset_prefix,
            body_class="legal-page",
            ui=ui_strings,
            legal_slug=slug,
            content_html=render_markdown(markdown_text),
            navigation=navigation,
            cache_bust=cache_bust,
            site_root="/",
            lang_switcher=[],
            current_lang=ui_lang,
        )
        _write_text(settings.output_dir / slug / "index.html", rendered)

    write_json(settings.output_dir / "data" / "topic-index.json", topic_index)
    write_json(settings.output_dir / "data" / "navigation.json", navigation)
