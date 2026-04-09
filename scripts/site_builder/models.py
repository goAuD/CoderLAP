from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TopicRecord:
    id: str
    lang: str
    title: str
    path: str
    main_topic_number: str
    main_topic_dir: str
    subtopic_number: str
    subtopic_dir: str
    slug: str
    review_status: str
    translation_status: str
    source_count: int
    opened_at: str | None
    canonical: bool

    def absolute_markdown_path(self, repo_root: Path) -> Path:
        return repo_root / self.path
