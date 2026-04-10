#!/usr/bin/env python3
"""Automated content review for all 233 subtopic README.md files.

Checks:
  1. Expected sections present
  2. Minimum content length
  3. At least one source URL in Források
  4. Heading consistency (## level headings)

Usage:
    python scripts/review_content.py
    python scripts/review_content.py --module 01
    python scripts/review_content.py --json > review_report.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Sections that every topic document should have (Hungarian headings)
REQUIRED_SECTIONS = [
    "Források",
]

RECOMMENDED_SECTIONS = [
    "Vizsgán jól használható megfogalmazás",
    "Gyakori vizsgahibák",
    "Gyors önellenőrzés",
    "Rövid válaszok az önellenőrzéshez",
]

MIN_CONTENT_LENGTH = 500  # characters, excluding frontmatter
URL_PATTERN = re.compile(r"https?://[^\s)\]>\"]+")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
H2_PATTERN = re.compile(r"^##\s+(.+)$", re.MULTILINE)


def find_subtopic_readmes(module_filter: str | None = None) -> list[Path]:
    """Find all subtopic README.md files, optionally filtered by module number."""
    results = []
    for main_dir in sorted(REPO_ROOT.iterdir()):
        if not main_dir.is_dir() or not re.match(r"^\d{2}_", main_dir.name):
            continue
        if module_filter and not main_dir.name.startswith(f"{module_filter}_"):
            continue
        for sub_dir in sorted(main_dir.iterdir()):
            if not sub_dir.is_dir() or not re.match(r"^\d{2}_", sub_dir.name):
                continue
            readme = sub_dir / "README.md"
            if readme.is_file():
                results.append(readme)
    return results


def extract_sections(text: str) -> list[str]:
    """Extract all ## level heading titles from markdown text."""
    return [m.group(1).strip() for m in H2_PATTERN.finditer(text)]


def extract_sources_section(text: str) -> str:
    """Extract the text under ## Források heading."""
    match = re.search(r"^## Források\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def review_file(path: Path) -> dict:
    """Review a single README.md and return findings."""
    rel = path.relative_to(REPO_ROOT)
    text = path.read_text(encoding="utf-8")
    sections = extract_sections(text)
    sources_text = extract_sources_section(text)
    source_urls = URL_PATTERN.findall(sources_text)
    all_urls = URL_PATTERN.findall(text)

    # Build topic ID from path
    parts = rel.parts  # e.g. ('01_Grundlagen...', '01_Zeichensatz_ASCII', 'README.md')
    main_num = parts[0][:2] if len(parts) >= 2 else "??"
    sub_num = parts[1][:2] if len(parts) >= 2 else "??"
    topic_id = f"LAP-{main_num}-{sub_num}"

    issues = []
    warnings = []

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            issues.append(f"Missing required section: ## {section}")

    # Check recommended sections
    for section in RECOMMENDED_SECTIONS:
        if section not in sections:
            warnings.append(f"Missing recommended section: ## {section}")

    # Check content length
    content_length = len(text.strip())
    if content_length < MIN_CONTENT_LENGTH:
        issues.append(f"Content too short: {content_length} chars (min {MIN_CONTENT_LENGTH})")

    # Check sources
    if "Források" in sections and not source_urls:
        issues.append("Források section exists but contains no URLs")
    elif "Források" not in sections:
        pass  # Already flagged above

    # Check for H1 title
    h1_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    if not h1_match:
        issues.append("Missing H1 title")

    # Count tables
    table_count = text.count("| --- ") + text.count("|---|") + text.count("| :---")

    return {
        "topic_id": topic_id,
        "path": str(rel),
        "main_module": parts[0] if len(parts) >= 2 else "unknown",
        "content_length": content_length,
        "section_count": len(sections),
        "sections": sections,
        "source_url_count": len(source_urls),
        "total_url_count": len(all_urls),
        "table_count": table_count,
        "issues": issues,
        "warnings": warnings,
        "status": "ok" if not issues else "issues",
    }


def print_summary(results: list[dict]) -> None:
    """Print a human-readable summary of the review."""
    total = len(results)
    ok = sum(1 for r in results if r["status"] == "ok")
    with_issues = total - ok

    print(f"\n{'=' * 65}")
    print(f"  Content Review Summary")
    print(f"{'=' * 65}")
    print(f"  Total files reviewed:  {total}")
    print(f"  OK:                    {ok}")
    print(f"  With issues:           {with_issues}")
    print(f"{'=' * 65}\n")

    if with_issues == 0:
        print("  All files passed review checks.\n")
        return

    # Group by module
    from collections import defaultdict
    by_module: dict[str, list[dict]] = defaultdict(list)
    for r in results:
        if r["issues"]:
            by_module[r["main_module"]].append(r)

    for module in sorted(by_module.keys()):
        entries = by_module[module]
        print(f"  [{module}]")
        for entry in entries:
            print(f"    {entry['topic_id']}  ({entry['content_length']} chars)")
            for issue in entry["issues"]:
                print(f"      ✗ {issue}")
        print()

    # Stats
    missing_sources = sum(1 for r in results if "Források" not in r["sections"])
    missing_exam = sum(
        1 for r in results
        if "Vizsgán jól használható megfogalmazás" not in r["sections"]
    )
    missing_selfcheck = sum(
        1 for r in results if "Gyors önellenőrzés" not in r["sections"]
    )
    short_files = sum(1 for r in results if r["content_length"] < MIN_CONTENT_LENGTH)

    print(f"  Section coverage across all {total} files:")
    print(f"    Missing '## Források':                      {missing_sources}")
    print(f"    Missing '## Vizsgán jól használható ..':     {missing_exam}")
    print(f"    Missing '## Gyors önellenőrzés':             {missing_selfcheck}")
    print(f"    Files < {MIN_CONTENT_LENGTH} chars:                         {short_files}")
    print()

    # Tables per module
    tables_by_module: dict[str, int] = defaultdict(int)
    for r in results:
        tables_by_module[r["main_module"]] += r["table_count"]
    print(f"  Table count by module:")
    for mod in sorted(tables_by_module.keys()):
        count = tables_by_module[mod]
        if count > 0:
            print(f"    {mod[:30]:<32} {count} tables")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Review CoderLAP content files")
    parser.add_argument("--module", help="Filter by module number, e.g. 01, 11")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    readmes = find_subtopic_readmes(args.module)
    if not readmes:
        print(f"No README.md files found{' for module ' + args.module if args.module else ''}.")
        sys.exit(1)

    results = [review_file(r) for r in readmes]

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print_summary(results)


if __name__ == "__main__":
    main()
