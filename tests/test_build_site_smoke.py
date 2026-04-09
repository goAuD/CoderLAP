from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys


def test_build_site_generates_expected_outputs() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    dist_dir = repo_root / "dist"

    if dist_dir.exists():
        shutil.rmtree(dist_dir)

    result = subprocess.run(
        [sys.executable, "scripts/build_site.py"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout.strip() == str(dist_dir)
    assert (dist_dir / "index.html").exists()
    assert (dist_dir / "data" / "topic-index.json").exists()
    assert (dist_dir / "topics" / "01-01-zeichensatz_ascii" / "index.html").exists()
    assert (dist_dir / "imprint" / "index.html").exists()
    assert (dist_dir / "privacy" / "index.html").exists()
