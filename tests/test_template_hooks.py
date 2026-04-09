from __future__ import annotations

from pathlib import Path
import unittest

from scripts.site_builder.models import TopicRecord
from scripts.site_builder.render import build_template_environment


def make_topic(topic_id: str, slug: str, title: str) -> TopicRecord:
    return TopicRecord(
        topic_id,
        "hu",
        title,
        "01_Grundlagen/01_ASCII/README.md",
        "01",
        "01_Grundlagen",
        "01",
        "01_ASCII",
        slug,
        "draft",
        "not_started",
        1,
        None,
        True,
    )


class TemplateHookTests(unittest.TestCase):
    def setUp(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        self.env = build_template_environment(repo_root / "site" / "templates")
        self.ui = {
            "project_tagline": "Austrian LAP study base",
            "home_title": "CoderLAP",
            "home_intro": "Browse and revise topics fast.",
            "search_placeholder": "Search topics",
            "search_label": "Search",
            "filter_label": "Filter",
            "sidebar_label": "Sidebar",
            "back_to_catalog": "Back to catalog",
            "print_label": "Print topic",
            "previous_label": "Previous",
            "next_label": "Next",
            "imprint_label": "Imprint",
            "privacy_label": "Privacy",
        }
        self.topic_index = [
            {
                "id": "LAP-01-01",
                "title": "ASCII",
                "slug": "01-01-ascii",
                "main_topic_number": "01",
                "main_topic_label": "01_Grundlagen",
                "subtopic_label": "01_ASCII",
                "source_count": 2,
                "review_status": "draft",
                "translation_status": "not_started",
            }
        ]
        self.navigation = {
            "main_topics": [
                {
                    "number": "01",
                    "label": "01_Grundlagen",
                    "topics": [
                        {
                            "id": "LAP-01-01",
                            "title": "ASCII",
                            "slug": "01-01-ascii",
                            "subtopic_number": "01",
                            "subtopic_dir": "01_ASCII",
                        }
                    ],
                }
            ],
            "topics": {
                "LAP-01-01": {
                    "id": "LAP-01-01",
                    "slug": "01-01-ascii",
                    "previous_id": None,
                    "next_id": None,
                }
            },
        }

    def test_home_template_exposes_search_filter_and_results_hooks(self) -> None:
        html = self.env.get_template("home.html").render(
            ui_lang="en",
            page_title="CoderLAP",
            asset_prefix="/assets",
            body_class="home-page",
            ui=self.ui,
            navigation=self.navigation,
            topic_index=self.topic_index,
        )

        self.assertIn("data-search-input", html)
        self.assertIn("data-module-filter", html)
        self.assertIn("data-topic-results", html)

    def test_topic_template_exposes_print_trigger(self) -> None:
        html = self.env.get_template("topic.html").render(
            ui_lang="en",
            page_title="ASCII",
            asset_prefix="/assets",
            body_class="topic-page",
            ui=self.ui,
            topic=make_topic("LAP-01-01", "01-01-ascii", "ASCII"),
            content_html="<h1>ASCII</h1>",
            navigation=self.navigation,
            topic_index=self.topic_index,
        )

        self.assertIn("data-print-trigger", html)


if __name__ == "__main__":
    unittest.main()
