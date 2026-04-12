from pathlib import Path
import unittest
import subprocess
import sys

from scripts.site_builder.settings import BuildSettings


class BuildSettingsTests(unittest.TestCase):
    def test_from_repo_root_maps_expected_paths(self) -> None:
        repo_root = Path("C:/GitHub/CoderLAP")
        settings = BuildSettings.from_repo_root(repo_root)

        self.assertEqual(settings.repo_root, repo_root)
        self.assertEqual(settings.registry_path, repo_root / "LAP_CONTENT_REGISTRY.json")
        self.assertEqual(settings.template_dir, repo_root / "site" / "templates")
        self.assertEqual(settings.asset_dir, repo_root / "site" / "assets")
        self.assertEqual(settings.static_content_dir, repo_root / "site" / "content" / "static" / "root")
        self.assertEqual(settings.output_dir, repo_root / "dist")
        self.assertEqual(settings.i18n_dir, repo_root / "site" / "i18n")
        self.assertEqual(settings.legal_content_dir, repo_root / "site" / "content" / "legal" / "en")

    def test_build_site_entrypoint_runs_from_repo_root(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        expected_output = f"Built site into {repo_root / 'dist'}"
        result = subprocess.run(
            [sys.executable, "scripts/build_site.py"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn(expected_output, result.stdout.strip())
