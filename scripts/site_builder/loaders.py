from __future__ import annotations

import json
import re
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

STRING_FIELDS = {
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
}

TOPIC_NUMBER_PATTERN = re.compile(r"^\d{2}$")


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
    if not isinstance(item["canonical"], bool):
        raise ValueError("Registry item field 'canonical' must be a boolean.")
    if not isinstance(item["main_topic_number"], str) or not TOPIC_NUMBER_PATTERN.fullmatch(item["main_topic_number"]):
        raise ValueError("Registry item field 'main_topic_number' must be a two-digit numeric string.")
    if not isinstance(item["subtopic_number"], str) or not TOPIC_NUMBER_PATTERN.fullmatch(item["subtopic_number"]):
        raise ValueError("Registry item field 'subtopic_number' must be a two-digit numeric string.")
    for field_name in STRING_FIELDS:
        if not isinstance(item[field_name], str):
            raise ValueError(f"Registry item field '{field_name}' must be a string.")
    if not isinstance(item["source_count"], int) or isinstance(item["source_count"], bool):
        raise ValueError("Registry item field 'source_count' must be an integer.")
    if item["opened_at"] is not None and not isinstance(item["opened_at"], str):
        raise ValueError("Registry item field 'opened_at' must be a string or null.")
    return TopicRecord(**item)


def load_registry_items(registry_path: Path) -> list[TopicRecord]:
    payload = _load_registry_payload(registry_path)
    records: list[TopicRecord] = []
    for item in payload["items"]:
        if not isinstance(item, dict):
            raise ValueError("Registry items must be JSON objects.")
        if item.get("canonical") is False:
            continue
        record = _build_topic_record(item)
        records.append(record)
    return sorted(records, key=lambda record: (int(record.main_topic_number), int(record.subtopic_number)))


def load_topic_markdown(markdown_path: Path) -> str:
    try:
        return markdown_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Topic markdown not found: {markdown_path}") from None
    except UnicodeDecodeError as exc:
        raise ValueError(f"Invalid UTF-8 in {markdown_path}: {exc}") from exc
