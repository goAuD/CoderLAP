from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from scripts.fetch_site_fonts import (
    NETWORK_TIMEOUT_SECONDS,
    build_output_path,
    copy_local_fonts,
    download_font,
    extract_font_urls,
    fetch_css,
)


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

    def test_extract_font_urls_filters_to_woff2_in_order(self) -> None:
        css_text = """
        @font-face { src: url(https://fonts.gstatic.com/a.woff2) format("woff2"); }
        @font-face { src: url(https://fonts.gstatic.com/b.ttf) format("truetype"); }
        @font-face { src: url(https://fonts.gstatic.com/c.woff2) format("woff2"); }
        """

        self.assertEqual(
            extract_font_urls(css_text),
            [
                "https://fonts.gstatic.com/a.woff2",
                "https://fonts.gstatic.com/c.woff2",
            ],
        )

    def test_copy_local_fonts_copies_only_woff2_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_dir = root / "source"
            output_dir = root / "output"
            source_dir.mkdir()
            output_dir.mkdir()
            (source_dir / "keep.woff2").write_bytes(b"font-data")
            (source_dir / "skip.txt").write_text("ignore me", encoding="utf-8")

            copied_paths = copy_local_fonts(source_dir, output_dir)

            self.assertEqual([path.name for path in copied_paths], ["keep.woff2"])
            self.assertEqual((output_dir / "keep.woff2").read_bytes(), b"font-data")
            self.assertFalse((output_dir / "skip.txt").exists())

    def test_download_font_uses_atomic_replace_and_cleans_failed_temp_file(self) -> None:
        class FakeResponse:
            def __enter__(self) -> "FakeResponse":
                return self

            def __exit__(self, exc_type, exc, tb) -> None:
                return None

        def fake_copyfileobj(source, destination) -> None:
            destination.write(b"partial-bytes")
            raise RuntimeError("download failed")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_path = root / "manrope-font.woff2"
            target_path.write_bytes(b"original-bytes")
            urlopen_mock = MagicMock(return_value=FakeResponse())

            with patch("scripts.fetch_site_fonts.urllib.request.urlopen", urlopen_mock), patch(
                "scripts.fetch_site_fonts.shutil.copyfileobj",
                side_effect=fake_copyfileobj,
            ):
                with self.assertRaises(RuntimeError):
                    download_font("https://fonts.gstatic.com/font.woff2", target_path)

            self.assertEqual(target_path.read_bytes(), b"original-bytes")
            self.assertEqual([path.name for path in root.iterdir()], ["manrope-font.woff2"])

    def test_download_font_reaches_os_replace_on_success(self) -> None:
        class FakeResponse:
            def __enter__(self) -> "FakeResponse":
                return self

            def __exit__(self, exc_type, exc, tb) -> None:
                return None

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_path = root / "manrope-font.woff2"
            urlopen_mock = MagicMock(return_value=FakeResponse())
            replace_mock = MagicMock()

            with patch("scripts.fetch_site_fonts.urllib.request.urlopen", urlopen_mock), patch(
                "scripts.fetch_site_fonts.os.replace",
                replace_mock,
            ):
                with patch("scripts.fetch_site_fonts.shutil.copyfileobj") as copyfileobj_mock:
                    copyfileobj_mock.side_effect = lambda source, destination: destination.write(b"font-data")
                    download_font("https://fonts.gstatic.com/font.woff2", target_path)

            replace_mock.assert_called_once()
            temp_path, replaced_target = replace_mock.call_args.args
            self.assertEqual(replaced_target, target_path)
            self.assertTrue(str(temp_path).startswith(str(target_path.parent)))
            self.assertEqual(target_path.exists(), False)

    def test_fetch_css_passes_explicit_timeout(self) -> None:
        fake_response = MagicMock()
        fake_response.__enter__.return_value.read.return_value = b"@font-face {}"
        fake_response.__exit__.return_value = None

        with patch("scripts.fetch_site_fonts.urllib.request.urlopen", return_value=fake_response) as urlopen_mock:
            self.assertEqual(fetch_css("https://fonts.googleapis.com/css2?family=Manrope"), "@font-face {}")

        _, kwargs = urlopen_mock.call_args
        self.assertEqual(kwargs["timeout"], NETWORK_TIMEOUT_SECONDS)

    def test_download_font_passes_explicit_timeout(self) -> None:
        fake_response = MagicMock()
        fake_response.__enter__.return_value = BytesIO(b"font-data")
        fake_response.__exit__.return_value = None

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target_path = root / "source-sans-3-font.woff2"
            with patch("scripts.fetch_site_fonts.urllib.request.urlopen", return_value=fake_response) as urlopen_mock:
                with patch("scripts.fetch_site_fonts.os.replace"):
                    download_font("https://fonts.gstatic.com/font.woff2", target_path)

        _, kwargs = urlopen_mock.call_args
        self.assertEqual(kwargs["timeout"], NETWORK_TIMEOUT_SECONDS)


if __name__ == "__main__":
    unittest.main()
