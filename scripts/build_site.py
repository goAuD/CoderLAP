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


def main() -> None:
    settings = BuildSettings.from_repo_root(Path(__file__).resolve().parents[1])
    output_dir = build_site(settings)
    print(f"Built site into {output_dir}")
    for lc in settings.languages:
        tag = "(default)" if lc.is_default else f"(/{lc.code}/)"
        print(f"  {lc.code} {tag}")


if __name__ == "__main__":
    main()
