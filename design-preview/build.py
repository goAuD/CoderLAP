"""Build isolated design samples using the existing registry and lesson sources."""
from pathlib import Path
import json
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "dist" / "design-preview"
LESSON_ID = "LAP-15-17"


def build():
    if not (ROOT / "dist" / "index.html").exists():
        raise SystemExit("Run python scripts/build_site.py first.")
    items = json.loads((ROOT / "LAP_CONTENT_REGISTRY.json").read_text(encoding="utf-8"))["items"]
    lesson = next(item for item in items if item["id"] == LESSON_ID)
    modules = {}
    for item in items:
        number = item["main_topic_number"]
        modules.setdefault(number, {"number": number, "title": item["main_topic_dir"][3:].replace("_", " "), "items": []})
        modules[number]["items"].append(item)
    copy = json.loads((HERE / "copy.json").read_text(encoding="utf-8"))
    env = Environment(loader=FileSystemLoader(HERE), autoescape=select_autoescape(["html"]))
    template = env.get_template("page.html")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name in ["tokens.css", "preview.css", "preview.js"]:
        shutil.copyfile(HERE / name, OUTPUT / name)
    for lang in ("de", "hu"):
        path = ROOT / lesson["path"]
        if lang == "de":
            path = path.with_name("README.de.md")
        md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
        text = path.read_text(encoding="utf-8")
        # The title appears in the page header; all remaining source content is retained.
        content = md.convert(text.split("\n", 1)[1])
        for skin in ("studio", "campus"):
            for page in ("home", "lesson"):
                output = template.render(
                    skin=skin, page=page, lang=lang, ui=copy[lang], modules=list(modules.values()),
                    lesson=lesson, lesson_html=content, toc=md.toc_tokens,
                    total=len(items), root="/hu/" if lang == "hu" else "/",
                    filename=f"{skin}-{lang}-{page}.html",
                )
                (OUTPUT / f"{skin}-{lang}-{page}.html").write_text(output, encoding="utf-8")
    print(f"Built 8 design previews in {OUTPUT}")


if __name__ == "__main__":
    build()
