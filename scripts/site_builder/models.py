from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath, PureWindowsPath


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
        posix_path = PurePosixPath(self.path)
        windows_path = PureWindowsPath(self.path)
        if posix_path.is_absolute() or windows_path.is_absolute() or windows_path.drive:
            raise ValueError(f"Markdown path must stay repository-relative: {self.path}")
        root = repo_root.resolve()
        candidate = (root / self.path).resolve(strict=False)
        if not candidate.is_relative_to(root):
            raise ValueError(f"Markdown path escapes repository root: {self.path}")
        return candidate
