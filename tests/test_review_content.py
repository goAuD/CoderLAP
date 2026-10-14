from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import scripts.review_content as review


class ContentReviewTests(unittest.TestCase):
    def test_review_includes_module_introduction_and_respects_module_filter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = [
                root / "01_Basics" / "01_Bits" / "README.md",
                root / "18_Exercise" / "README.md",
                root / "18_Exercise" / "01_Setup" / "README.md",
            ]
            source = "# Topic\n\n" + "Learning content. " * 40
            source += "\n\n## Források\n\nhttps://example.org/source\n"
            for path in paths:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(source, encoding="utf-8")

            with patch.object(review, "REPO_ROOT", root):
                self.assertCountEqual(review.find_subtopic_readmes(), paths)
                self.assertCountEqual(review.find_subtopic_readmes("18"), paths[1:])
                intro = review.review_file(paths[1])
                self.assertEqual(intro["topic_id"], "LAP-18-00")
                self.assertEqual(intro["status"], "ok")
                self.assertEqual(review.review_file(paths[2])["topic_id"], "LAP-18-01")
