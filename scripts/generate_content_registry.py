from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_JSON = ROOT / "LAP_CONTENT_REGISTRY.json"
OUTPUT_CSV = ROOT / "LAP_CONTENT_REGISTRY.csv"

TOPIC_PATTERN = re.compile(r"^(?P<main>\d{2})_.+$")
SUBTOPIC_PATTERN = re.compile(r"^(?P<sub>\d{2})_.+$")
TITLE_PATTERN = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)
OPENED_PATTERN = re.compile(r"^Megnyitva:\s*`(?P<date>\d{4}-\d{2}-\d{2})`", re.MULTILINE)


@dataclass
class RegistryItem:
    id: str
    lang: str
    title: str
    path: str
    main_topic_number: str
    main_topic_dir: str
    subtopic_number: str
    subtopic_dir: str
    slug: str
    review_status: str
    translation_status: str
    source_count: int
    opened_at: str | None
    canonical: bool


def get_translation_status(subtopic_dir: Path) -> str:
    german_sidecar = subtopic_dir / "README.de.md"
    return "de_complete" if german_sidecar.exists() else "de_missing"


def count_sources(markdown: str) -> int:
    if "## Források" not in markdown:
        return 0

    sources_section = markdown.split("## Források", 1)[1]
    next_heading = re.search(r"^##\s+", sources_section, re.MULTILINE)
    if next_heading:
        sources_section = sources_section[: next_heading.start()]

    return len(re.findall(r"^\d+\.\s", sources_section, re.MULTILINE))


def get_markdown_title(markdown: str, fallback: str) -> str:
    match = TITLE_PATTERN.search(markdown)
    if match:
        return match.group("title").strip()
    return fallback


def get_opened_at(markdown: str) -> str | None:
    match = OPENED_PATTERN.search(markdown)
    if match:
        return match.group("date")
    return None


def _read_markdown(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"Invalid UTF-8 in {path}: {exc}") from exc


def build_registry() -> list[RegistryItem]:
    items: list[RegistryItem] = []

    for topic_dir in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        topic_match = TOPIC_PATTERN.match(topic_dir.name)
        if not topic_match:
            continue

        main_number = topic_match.group("main")

        # Main-topic-level README.md registered as subtopic "00"
        main_readme = topic_dir / "README.md"
        if main_readme.exists():
            markdown = _read_markdown(main_readme)
            slug = f"{main_number}-00-{topic_dir.name[3:].lower().replace(' ', '-')}"
            item = RegistryItem(
                id=f"LAP-{main_number}-00",
                lang="hu",
                title=get_markdown_title(markdown, topic_dir.name[3:].replace("_", " ")),
                path=str(main_readme.relative_to(ROOT)).replace("\\", "/"),
                main_topic_number=main_number,
                main_topic_dir=topic_dir.name,
                subtopic_number="00",
                subtopic_dir=topic_dir.name,
                slug=slug,
                review_status="draft",
                translation_status=get_translation_status(topic_dir),
                source_count=count_sources(markdown),
                opened_at=get_opened_at(markdown),
                canonical=True,
            )
            items.append(item)

        for subtopic_dir in sorted(p for p in topic_dir.iterdir() if p.is_dir()):
            subtopic_match = SUBTOPIC_PATTERN.match(subtopic_dir.name)
            if not subtopic_match:
                continue

            readme = subtopic_dir / "README.md"
            if not readme.exists():
                continue

            markdown = _read_markdown(readme)
            sub_number = subtopic_match.group("sub")
            slug = f"{main_number}-{sub_number}-{subtopic_dir.name[3:].lower()}"
            slug = slug.replace(" ", "-")

            item = RegistryItem(
                id=f"LAP-{main_number}-{sub_number}",
                lang="hu",
                title=get_markdown_title(markdown, subtopic_dir.name[3:].replace("_", " ")),
                path=str(readme.relative_to(ROOT)).replace("\\", "/"),
                main_topic_number=main_number,
                main_topic_dir=topic_dir.name,
                subtopic_number=sub_number,
                subtopic_dir=subtopic_dir.name,
                slug=slug,
                review_status="draft",
                translation_status=get_translation_status(subtopic_dir),
                source_count=count_sources(markdown),
                opened_at=get_opened_at(markdown),
                canonical=True,
            )
            items.append(item)

    return items


def write_json(items: list[RegistryItem]) -> None:
    payload = {
        "generated_at": str(date.today()),
        "generator": "scripts/generate_content_registry.py",
        "id_format": "LAP-<MAIN>-<SUB>",
        "item_count": len(items),
        "source_root": ".",
        "items": [asdict(item) for item in items],
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(items: list[RegistryItem]) -> None:
    fieldnames = list(asdict(items[0]).keys()) if items else [
        "id",
        "lang",
        "title",
        "path",
        "main_topic_number",
        "main_topic_dir",
        "subtopic_number",
        "subtopic_dir",
        "slug",
        "review_status",
        "translation_status",
        "source_count",
        "opened_at",
        "canonical",
    ]

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(asdict(item))


def main() -> None:
    items = build_registry()
    write_json(items)
    write_csv(items)
    print(f"Generated registry for {len(items)} content files.")
    print(f"JSON: {OUTPUT_JSON}")
    print(f"CSV : {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
