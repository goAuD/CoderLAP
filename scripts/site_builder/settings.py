from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class LanguageConfig:
    code: str
    i18n_file: Path
    legal_content_dir: Path
    is_default: bool = False


@dataclass(frozen=True)
class BuildSettings:
    repo_root: Path
    registry_path: Path
    template_dir: Path
    asset_dir: Path
    output_dir: Path
    i18n_dir: Path
    legal_content_dir: Path
    languages: tuple[LanguageConfig, ...] = ()
    default_lang: str = "de"

    @classmethod
    def from_repo_root(cls, repo_root: Path) -> "BuildSettings":
        i18n_dir = repo_root / "site" / "i18n"
        legal_base = repo_root / "site" / "content" / "legal"

        languages = (
            LanguageConfig(
                code="de",
                i18n_file=i18n_dir / "de.json",
                legal_content_dir=legal_base / "de",
                is_default=True,
            ),
            LanguageConfig(
                code="hu",
                i18n_file=i18n_dir / "hu.json",
                legal_content_dir=legal_base / "hu",
            ),
        )

        return cls(
            repo_root=repo_root,
            registry_path=repo_root / "LAP_CONTENT_REGISTRY.json",
            template_dir=repo_root / "site" / "templates",
            asset_dir=repo_root / "site" / "assets",
            output_dir=repo_root / "dist",
            i18n_dir=i18n_dir,
            legal_content_dir=legal_base / "en",
            languages=languages,
            default_lang="de",
        )
