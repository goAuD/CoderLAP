from __future__ import annotations

import json
import shutil
import time
from pathlib import Path
from typing import Any

from .loaders import load_registry_items, load_topic_markdown
from .navigation import build_navigation
from .render import build_template_environment, render_markdown
from .settings import BuildSettings, LanguageConfig


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _topic_index_entry(topic) -> dict[str, Any]:
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


def _build_language(
    lang_config: LanguageConfig,
    settings: BuildSettings,
    all_languages: tuple[LanguageConfig, ...],
    topics: list,
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

    # Build language switcher data for templates
    lang_switcher = []
    for lc in all_languages:
        if lc.is_default:
            prefix = "/"
        else:
            prefix = f"/{lc.code}/"
        lang_switcher.append({
            "code": lc.code,
            "label": lc.code.upper(),
            "prefix": prefix,
            "is_current": lc.code == lang_config.code,
        })

    topic_index = [_topic_index_entry(topic) for topic in topics]

    common_ctx = {
        "ui_lang": ui_lang,
        "asset_prefix": asset_prefix,
        "ui": ui_strings,
        "navigation": navigation,
        "cache_bust": cache_bust,
        "site_root": site_root,
        "lang_switcher": lang_switcher,
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
        )
        _write_text(lang_output / "topics" / topic.slug / "index.html", rendered)

    home_html = env.get_template("home.html").render(
        **common_ctx,
        page_lang=ui_lang,
        page_title=ui_strings.get("home_title", "CoderLAP"),
        body_class="home-page",
        topic_index=topic_index,
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

    _recreate_output_dir(settings.output_dir)
    shutil.copytree(settings.asset_dir, settings.output_dir / "assets")

    cache_bust = str(int(time.time()))

    if settings.languages:
        for lang_config in settings.languages:
            _build_language(
                lang_config, settings, settings.languages,
                topics, navigation, env, cache_bust,
            )
    else:
        # Legacy single-language fallback
        if ui_strings is None or legal_pages is None:
            raise ValueError("ui_strings and legal_pages are required for single-language builds")
        _build_single_language(
            settings, ui_strings, legal_pages,
            topics, navigation, env, cache_bust,
        )

    return settings.output_dir


def _build_single_language(
    settings: BuildSettings,
    ui_strings: dict[str, Any],
    legal_pages: dict[str, str],
    topics: list,
    navigation: dict,
    env: Any,
    cache_bust: str,
) -> None:
    """Legacy single-language build path for backward compatibility."""
    ui_lang = str(ui_strings.get("lang", "en"))
    asset_prefix = "/assets"
    topic_index = [_topic_index_entry(topic) for topic in topics]

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
