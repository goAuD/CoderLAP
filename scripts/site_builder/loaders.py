from __future__ import annotations

import json
from pathlib import Path

from .models import TopicRecord

REQUIRED_ITEM_FIELDS = {
    "id",
    "lang",
    "title",
    "path",
    "main_topic_number",
    "main_topic_dir",
    "subtopic_number",
    "subtopic_dir",
    "slug",
    "review_status",
    "translation_status",
    "source_count",
    "opened_at",
    "canonical",
}


def _load_registry_payload(registry_path: Path) -> dict:
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Registry payload must be a JSON object.")
    items = payload.get("items")
    if not isinstance(items, list):
        raise ValueError("Registry payload must contain an 'items' list.")
    return payload


def _build_topic_record(item: dict) -> TopicRecord:
    if not isinstance(item, dict):
        raise ValueError("Registry items must be JSON objects.")
    missing_fields = REQUIRED_ITEM_FIELDS - item.keys()
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Registry item is missing required fields: {missing}")
    if item["canonical"] is None:
        raise ValueError("Registry item is missing required field: canonical")
    return TopicRecord(**item)


def load_registry_items(registry_path: Path) -> list[TopicRecord]:
    payload = _load_registry_payload(registry_path)
    records: list[TopicRecord] = []
    for item in payload["items"]:
        record = _build_topic_record(item)
        if record.canonical:
            records.append(record)
    return sorted(records, key=lambda record: (int(record.main_topic_number), int(record.subtopic_number)))


def load_topic_markdown(markdown_path: Path) -> str:
    return markdown_path.read_text(encoding="utf-8")
