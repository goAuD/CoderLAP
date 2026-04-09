from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from .loaders import load_registry_items, load_topic_markdown
from .navigation import build_navigation
from .render import build_template_environment, render_markdown
from .settings import BuildSettings


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


def build_site(
    settings: BuildSettings,
    ui_strings: dict[str, Any],
    legal_pages: dict[str, str],
) -> Path:
    topics = load_registry_items(settings.registry_path)
    navigation = build_navigation(topics)
    env = build_template_environment(settings.template_dir)

    _recreate_output_dir(settings.output_dir)
    shutil.copytree(settings.asset_dir, settings.output_dir / "assets")

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
        )
        _write_text(settings.output_dir / slug / "index.html", rendered)

    write_json(settings.output_dir / "data" / "topic-index.json", topic_index)
    write_json(settings.output_dir / "data" / "navigation.json", navigation)

    return settings.output_dir
