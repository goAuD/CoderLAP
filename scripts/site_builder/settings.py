from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BuildSettings:
    repo_root: Path
    registry_path: Path
    template_dir: Path
    asset_dir: Path
    output_dir: Path
    i18n_dir: Path
    legal_content_dir: Path

    @classmethod
    def from_repo_root(cls, repo_root: Path) -> "BuildSettings":
        return cls(
            repo_root=repo_root,
            registry_path=repo_root / "LAP_CONTENT_REGISTRY.json",
            template_dir=repo_root / "site" / "templates",
            asset_dir=repo_root / "site" / "assets",
            output_dir=repo_root / "dist",
            i18n_dir=repo_root / "site" / "i18n",
            legal_content_dir=repo_root / "site" / "content" / "legal" / "en",
        )
