from __future__ import annotations

import argparse
import re
import shutil
import urllib.request
from pathlib import Path
from typing import Iterable


GOOGLE_CSS_URLS = {
    "manrope": "https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap",
    "source-sans-3": "https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&display=swap",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

FONT_URL_PATTERN = re.compile(r"url\((https://fonts\.gstatic\.com[^)]+)\)")


def build_output_path(output_dir: Path, family_slug: str, source_url: str) -> Path:
    source_name = Path(urllib.request.url2pathname(source_url.split("?", 1)[0])).name
    suffix = Path(source_name).suffix or ".woff2"
    stem = Path(source_name).stem or "font"
    if stem == suffix.lstrip("."):
        stem = "font"
    return output_dir / f"{family_slug}-{stem}{suffix}"


def fetch_css(css_url: str) -> str:
    request = urllib.request.Request(css_url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")


def extract_font_urls(css_text: str) -> list[str]:
    return [match.group(1) for match in FONT_URL_PATTERN.finditer(css_text) if match.group(1).endswith(".woff2")]


def copy_local_fonts(source_dir: Path, output_dir: Path) -> list[Path]:
    copied_files: list[Path] = []
    if not source_dir.exists():
        return copied_files

    for source_path in sorted(source_dir.glob("*.woff2")):
        target_path = output_dir / source_path.name
        shutil.copy2(source_path, target_path)
        copied_files.append(target_path)
    return copied_files


def download_font(font_url: str, target_path: Path) -> None:
    request = urllib.request.Request(font_url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request) as response, target_path.open("wb") as target_file:
        shutil.copyfileobj(response, target_file)


def iter_target_fonts() -> Iterable[tuple[str, str, str]]:
    for family_slug, css_url in GOOGLE_CSS_URLS.items():
        css_text = fetch_css(css_url)
        for font_url in extract_font_urls(css_text):
            yield family_slug, css_url, font_url


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    output_dir = repo_root / "site" / "assets" / "fonts"
    output_dir.mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(description="Fetch local site fonts from Google Fonts CSS endpoints.")
    parser.add_argument(
        "--copy-from",
        dest="copy_from",
        type=Path,
        help="Optional directory containing local .woff2 assets to copy into site/assets/fonts before downloading.",
    )
    args = parser.parse_args()

    if args.copy_from is not None:
        copied_files = copy_local_fonts(args.copy_from, output_dir)
        for copied_file in copied_files:
            print(f"Copied {copied_file.name}")

    downloaded: set[Path] = set()
    for family_slug, _, font_url in iter_target_fonts():
        target_path = build_output_path(output_dir, family_slug, font_url)
        if target_path in downloaded or target_path.exists():
            continue

        download_font(font_url, target_path)
        downloaded.add(target_path)
        print(f"Downloaded {target_path.name}")


if __name__ == "__main__":
    main()
