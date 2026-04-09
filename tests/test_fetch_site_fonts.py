from pathlib import Path
import tempfile
import unittest

from scripts.fetch_site_fonts import build_output_path


class FetchSiteFontsTest(unittest.TestCase):
    def test_build_output_path_keeps_woff2_extension(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_path = build_output_path(
                root,
                family_slug="manrope",
                source_url="https://fonts.gstatic.com/s/manrope/v15/font.woff2",
            )

            self.assertEqual(output_path.name, "manrope-font.woff2")
            self.assertEqual(output_path.parent, root)


if __name__ == "__main__":
    unittest.main()
