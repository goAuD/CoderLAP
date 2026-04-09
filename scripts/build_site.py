from __future__ import annotations

from pathlib import Path
import sys


def _ensure_repo_root_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    repo_root_str = str(repo_root)
    if repo_root_str not in sys.path:
        sys.path.insert(0, repo_root_str)


_ensure_repo_root_on_path()

from scripts.site_builder.settings import BuildSettings
from scripts.site_builder.build import build_site

import json


def main() -> None:
    settings = BuildSettings.from_repo_root(Path(__file__).resolve().parents[1])
    ui_strings = json.loads((settings.i18n_dir / "en.json").read_text(encoding="utf-8"))
    legal_pages = {
        "imprint": (settings.legal_content_dir / "imprint.md").read_text(encoding="utf-8"),
        "privacy": (settings.legal_content_dir / "privacy.md").read_text(encoding="utf-8"),
    }
    output_dir = build_site(settings, ui_strings, legal_pages)
    print(output_dir)


if __name__ == "__main__":
    main()
