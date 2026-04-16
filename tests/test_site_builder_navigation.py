from __future__ import annotations

import unittest

from scripts.site_builder.models import TopicRecord
from scripts.site_builder.navigation import build_navigation


def make_topic(
    topic_id: str,
    main_topic_number: str,
    subtopic_number: str,
    title: str,
    main_topic_dir: str,
    subtopic_dir: str,
    slug: str,
) -> TopicRecord:
    return TopicRecord(
        topic_id,
        "hu",
        title,
        f"{main_topic_number}/{subtopic_number}/README.md",
        main_topic_number,
        main_topic_dir,
        subtopic_number,
        subtopic_dir,
        slug,
        "draft",
        "not_started",
        1,
        None,
        True,
    )


class NavigationTests(unittest.TestCase):
    def test_build_navigation_sorts_topics_and_links_boundaries(self) -> None:
        topics = [
            make_topic("LAP-02-02", "02", "02", "Later", "02_Betriebssysteme", "02_Later", "02-02-later"),
            make_topic("LAP-01-02", "01", "02", "Middle", "01_Grundlagen", "02_Middle", "01-02-middle"),
            make_topic("LAP-01-01", "01", "01", "First", "01_Grundlagen", "01_First", "01-01-first"),
        ]

        navigation = build_navigation(topics)

        self.assertEqual(
            [main_topic["number"] for main_topic in navigation["main_topics"]],
            ["01", "02"],
        )
        self.assertEqual(navigation["main_topics"][0]["pack_slug"], "01-grundlagen")
        self.assertEqual(navigation["main_topics"][1]["pack_slug"], "02-betriebssysteme")
        self.assertEqual(
            [topic["id"] for topic in navigation["main_topics"][0]["topics"]],
            ["LAP-01-01", "LAP-01-02"],
        )
        self.assertEqual(navigation["topics"]["LAP-01-01"]["previous_id"], None)
        self.assertEqual(navigation["topics"]["LAP-01-01"]["next_id"], "LAP-01-02")
        self.assertEqual(navigation["topics"]["LAP-01-02"]["previous_id"], "LAP-01-01")
        self.assertEqual(navigation["topics"]["LAP-01-02"]["next_id"], "LAP-02-02")
        self.assertEqual(navigation["topics"]["LAP-02-02"]["previous_id"], "LAP-01-02")
        self.assertEqual(navigation["topics"]["LAP-02-02"]["next_id"], None)

    def test_build_navigation_rejects_duplicate_topic_ids(self) -> None:
        topics = [
            make_topic("LAP-01-01", "01", "01", "First", "01_Grundlagen", "01_First", "01-01-first"),
            make_topic("LAP-01-01", "01", "02", "Duplicate", "01_Grundlagen", "02_Duplicate", "01-02-duplicate"),
        ]

        with self.assertRaisesRegex(ValueError, "Duplicate topic ids are not allowed: LAP-01-01"):
            build_navigation(topics)


if __name__ == "__main__":
    unittest.main()
