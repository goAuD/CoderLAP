from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import unittest


class BuildSiteSmokeTests(unittest.TestCase):
    def test_build_site_generates_expected_outputs(self) -> None:
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

        self.assertIn(f"Built site into {dist_dir}", result.stdout.strip())
        # Default language (DE) at root
        self.assertTrue((dist_dir / "index.html").exists())
        self.assertTrue((dist_dir / "data" / "topic-index.json").exists())
        self.assertTrue((dist_dir / "topics" / "01-01-zeichensatz_ascii" / "index.html").exists())
        self.assertTrue((dist_dir / "imprint" / "index.html").exists())
        self.assertTrue((dist_dir / "privacy" / "index.html").exists())
        self.assertTrue((dist_dir / "robots.txt").exists())
        self.assertTrue((dist_dir / ".well-known" / "security.txt").exists())
        # Hungarian under /hu/
        self.assertTrue((dist_dir / "hu" / "index.html").exists())
        self.assertTrue((dist_dir / "hu" / "topics" / "01-01-zeichensatz_ascii" / "index.html").exists())


if __name__ == "__main__":
    unittest.main()
