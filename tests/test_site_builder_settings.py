from pathlib import Path
import unittest

from scripts.site_builder.settings import BuildSettings


class BuildSettingsTests(unittest.TestCase):
    def test_from_repo_root_maps_expected_paths(self) -> None:
        repo_root = Path("C:/GitHub/CoderLAP")
        settings = BuildSettings.from_repo_root(repo_root)

        self.assertEqual(settings.repo_root, repo_root)
        self.assertEqual(settings.registry_path, repo_root / "LAP_CONTENT_REGISTRY.json")
        self.assertEqual(settings.template_dir, repo_root / "site" / "templates")
        self.assertEqual(settings.asset_dir, repo_root / "site" / "assets")
        self.assertEqual(settings.output_dir, repo_root / "dist")
        self.assertEqual(settings.i18n_dir, repo_root / "site" / "i18n")
        self.assertEqual(settings.legal_content_dir, repo_root / "site" / "content" / "legal" / "en")
