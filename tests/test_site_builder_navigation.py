from __future__ import annotations

import unittest

from scripts.site_builder.models import TopicRecord
from scripts.site_builder.navigation import build_navigation


class NavigationTests(unittest.TestCase):
    def test_build_navigation_creates_prev_next_links(self) -> None:
        topics = [
            TopicRecord(
                "LAP-01-01",
                "hu",
                "ASCII",
                "01/A/README.md",
                "01",
                "01_Grundlagen",
                "01",
                "01_ASCII",
                "01-01-ascii",
                "draft",
                "not_started",
                1,
                None,
                True,
            ),
            TopicRecord(
                "LAP-01-02",
                "hu",
                "Bit",
                "01/B/README.md",
                "01",
                "01_Grundlagen",
                "02",
                "02_Bit",
                "01-02-bit",
                "draft",
                "not_started",
                1,
                None,
                True,
            ),
            TopicRecord(
                "LAP-02-01",
                "hu",
                "OS",
                "02/A/README.md",
                "02",
                "02_Betriebssysteme",
                "01",
                "01_OS",
                "02-01-os",
                "draft",
                "not_started",
                1,
                None,
                True,
            ),
        ]

        navigation = build_navigation(topics)

        self.assertEqual(navigation["topics"]["LAP-01-02"]["previous_id"], "LAP-01-01")
        self.assertEqual(navigation["topics"]["LAP-01-02"]["next_id"], "LAP-02-01")
        self.assertEqual(len(navigation["main_topics"]), 2)


if __name__ == "__main__":
    unittest.main()
