from __future__ import annotations

import json
from pathlib import Path

from .models import TopicRecord


def load_registry_items(registry_path: Path) -> list[TopicRecord]:
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    records = [
        TopicRecord(**item)
        for item in payload.get("items", [])
        if item.get("canonical", False)
    ]
    return sorted(records, key=lambda record: (int(record.main_topic_number), int(record.subtopic_number)))


def load_topic_markdown(markdown_path: Path) -> str:
    return markdown_path.read_text(encoding="utf-8")
