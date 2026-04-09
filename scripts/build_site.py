from pathlib import Path

from scripts.site_builder.settings import BuildSettings


def main() -> None:
    settings = BuildSettings.from_repo_root(Path(__file__).resolve().parents[1])
    print(settings.output_dir)


if __name__ == "__main__":
    main()
