from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

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
        self.site_js = (repo_root / "site" / "assets" / "js" / "site.js").read_text(encoding="utf-8")
        self.ui = {
            "project_tagline": "Osztrak LAP tanulobazis",
            "home_title": "CoderLAP",
            "home_intro": "Bongeszd esmet gyorsan a temakat.",
            "empty_state_label": "Nincs talalat.",
            "search_placeholder": "Temak keresese",
            "search_label": "Kereses",
            "filter_label": "Modul szurese",
            "sidebar_label": "Temakorok",
            "content_label": "Temakorok",
            "back_to_catalog": "Vissza a katalogushoz",
            "print_label": "Tema nyomtatasa",
            "module_pack_label": "Modulcsomag",
            "module_pack_print_label": "Modulcsomag nyomtatasa",
            "module_pack_contents_label": "A csomag temai",
            "module_pack_intro": "Egybefuzott nyomtathato modulnezet.",
            "previous_label": "Elozo",
            "next_label": "Kovetkezo",
            "topic_pagination_label": "Temak kozotti lapozas",
            "imprint_label": "Impresszum",
            "privacy_label": "Adatvedelem",
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
                "search_terms": ["ASCII", "karakterkodolas"],
            },
            {
                "id": "LAP-01-02",
                "title": "Binaris",
                "slug": "01-02-binaris",
                "main_topic_number": "01",
                "main_topic_label": "01_Grundlagen",
                "subtopic_label": "02_Binaer",
                "source_count": 2,
                "review_status": "draft",
                "translation_status": "not_started",
                "search_terms": ["Binaris", "binary"],
            },
            {
                "id": "LAP-01-03",
                "title": "Hexadezimalis",
                "slug": "01-03-hexadezimalis",
                "main_topic_number": "01",
                "main_topic_label": "01_Grundlagen",
                "subtopic_label": "03_Hexadezimal",
                "source_count": 2,
                "review_status": "draft",
                "translation_status": "not_started",
                "search_terms": ["Hexadezimalis", "hexadecimal"],
            },
        ]
        self.navigation = {
            "main_topics": [
                {
                    "number": "01",
                    "label": "01_Grundlagen",
                    "pack_slug": "01-grundlagen",
                    "topics": [
                        {
                            "id": "LAP-01-01",
                            "title": "ASCII",
                            "slug": "01-01-ascii",
                            "subtopic_number": "01",
                            "subtopic_dir": "01_ASCII",
                        },
                        {
                            "id": "LAP-01-02",
                            "title": "Binaris",
                            "slug": "01-02-binaris",
                            "subtopic_number": "02",
                            "subtopic_dir": "02_Binaer",
                        },
                        {
                            "id": "LAP-01-03",
                            "title": "Hexadezimalis",
                            "slug": "01-03-hexadezimalis",
                            "subtopic_number": "03",
                            "subtopic_dir": "03_Hexadezimal",
                        },
                    ],
                }
            ],
            "topics": {
                "LAP-01-01": {
                    "id": "LAP-01-01",
                    "slug": "01-01-ascii",
                    "previous_id": None,
                    "next_id": "LAP-01-02",
                },
                "LAP-01-02": {
                    "id": "LAP-01-02",
                    "slug": "01-02-binaris",
                    "previous_id": "LAP-01-01",
                    "next_id": "LAP-01-03",
                },
                "LAP-01-03": {
                    "id": "LAP-01-03",
                    "slug": "01-03-hexadezimalis",
                    "previous_id": "LAP-01-02",
                    "next_id": None,
                },
            },
        }

    def _extract_json_payload(self, html: str, hook: str) -> dict[str, str]:
        match = re.search(
            rf'<script type="application/json" {hook}>(.*?)</script>',
            html,
            re.DOTALL,
        )
        self.assertIsNotNone(match)
        return json.loads(match.group(1))

    def test_home_template_exposes_search_filter_and_results_hooks(self) -> None:
        html = self.env.get_template("home.html").render(
            ui_lang="en",
            page_title="CoderLAP",
            asset_prefix="/assets",
            body_class="home-page",
            ui=self.ui,
            navigation=self.navigation,
            topic_index=self.topic_index,
            search_alias_groups=[["api", "schnittstelle", "programozasi felulet"]],
        )

        self.assertIn("data-search-input", html)
        self.assertIn("data-module-filter", html)
        self.assertIn("data-topic-results", html)
        self.assertIn("data-catalog-controls", html)
        self.assertIn("data-sidebar-container", html)
        self.assertIn("data-sidebar-panel", html)
        self.assertIn("data-topic-index-json", html)
        self.assertIn("data-navigation-json", html)
        self.assertIn("data-search-aliases-json", html)
        self.assertIn("data-ui-copy-json", html)
        self.assertIn(">Temakorok<", html)
        self.assertIn(">Kereses<", html)
        self.assertIn(">Modul szurese<", html)
        self.assertIn('placeholder="Temak keresese"', html)
        self.assertRegex(html, r'data-catalog-controls[^>]*hidden')
        self.assertRegex(html, r'data-sidebar-container[^>]*hidden')
        self.assertRegex(html, r'data-search-input[^>]*disabled')
        self.assertRegex(html, r'data-module-filter[^>]*disabled')
        self.assertNotIn('<main class="page-shell">', html)
        self.assertNotIn('<section class="catalog-shell" aria-label="Sidebar">', html)

        ui_copy = self._extract_json_payload(html, "data-ui-copy-json")
        self.assertEqual(ui_copy["empty_state_label"], self.ui["empty_state_label"])
        self.assertEqual(ui_copy["search_placeholder"], self.ui["search_placeholder"])
        self.assertEqual(ui_copy["search_label"], self.ui["search_label"])
        self.assertEqual(ui_copy["filter_label"], self.ui["filter_label"])
        self.assertEqual(ui_copy["sidebar_label"], self.ui["sidebar_label"])
        self.assertEqual(ui_copy["module_pack_label"], self.ui["module_pack_label"])

    def test_topic_template_exposes_print_trigger(self) -> None:
        html = self.env.get_template("topic.html").render(
            ui_lang="en",
            page_title="Binaris",
            asset_prefix="/assets",
            body_class="topic-page",
            ui=self.ui,
            topic=make_topic("LAP-01-02", "01-02-binaris", "Binaris"),
            content_html="<h1>Binaris</h1>",
            navigation=self.navigation,
            topic_index=self.topic_index,
            site_root="/",
            lang_switcher=[
                {"code": "de", "label": "DE", "href": "/topics/01-02-binaris/", "is_current": True},
                {"code": "hu", "label": "HU", "href": "/hu/topics/01-02-binaris/", "is_current": False},
            ],
        )

        self.assertIn("data-print-trigger", html)
        self.assertIn(">Vissza a katalogushoz<", html)
        self.assertIn(">Tema nyomtatasa<", html)
        self.assertIn(">Modulcsomag nyomtatasa<", html)
        self.assertIn('class="site-nav-link site-nav-link--button"', html)
        self.assertIn('aria-label="Temak kozotti lapozas"', html)
        self.assertRegex(html, r'>\s*Elozo: ASCII\s*<')
        self.assertRegex(html, r'>\s*Kovetkezo: Hexadezimalis\s*<')
        self.assertIn('href="/topics/01-01-ascii/"', html)
        self.assertIn('href="/topics/01-03-hexadezimalis/"', html)
        self.assertIn('href="/hu/topics/01-02-binaris/"', html)
        self.assertIn('href="/module-packs/01-grundlagen/"', html)
        self.assertNotIn('<nav class="topic-pagination" aria-label="Sidebar">', html)
        self.assertNotIn('<main class="page-shell">', html)

    def test_module_pack_template_exposes_print_trigger_and_topic_outline(self) -> None:
        html = self.env.get_template("module_pack.html").render(
            ui_lang="hu",
            page_lang="hu",
            page_title="01 · Grundlagen",
            asset_prefix="/assets",
            body_class="module-pack-page",
            ui=self.ui,
            module_pack={
                "number": "01",
                "display_label": "Grundlagen",
                "topics": [
                    {
                        "id": "LAP-01-01",
                        "title": "ASCII",
                        "slug": "01-01-ascii",
                        "subtopic_number": "01",
                        "content_html": "<h1>ASCII</h1><p>Tartalom</p>",
                    },
                    {
                        "id": "LAP-01-02",
                        "title": "Binaris",
                        "slug": "01-02-binaris",
                        "subtopic_number": "02",
                        "content_html": "<h1>Binaris</h1><p>Tartalom</p>",
                    },
                ],
            },
            navigation=self.navigation,
            site_root="/",
            lang_switcher=[
                {"code": "de", "label": "DE", "href": "/module-packs/01-grundlagen/", "is_current": True},
                {"code": "hu", "label": "HU", "href": "/hu/module-packs/01-grundlagen/", "is_current": False},
            ],
        )

        self.assertIn("data-print-trigger", html)
        self.assertIn(">Modulcsomag nyomtatasa<", html)
        self.assertIn(">A csomag temai<", html)
        self.assertIn('href="#01-01-ascii"', html)
        self.assertIn('href="#01-02-binaris"', html)
        self.assertIn('href="/hu/module-packs/01-grundlagen/"', html)
        self.assertIn('class="module-pack-topic"', html)

    def test_site_js_wires_progressive_enhancement_hooks(self) -> None:
        self.assertIn('[data-catalog-controls]', self.site_js)
        self.assertIn('[data-topic-index-json]', self.site_js)
        self.assertIn('[data-navigation-json]', self.site_js)
        self.assertIn('[data-search-aliases-json]', self.site_js)
        self.assertIn('[data-ui-copy-json]', self.site_js)
        self.assertIn('[data-sidebar-container]', self.site_js)
        self.assertIn('[data-sidebar-panel]', self.site_js)
        self.assertIn('function formatMainTopicLabel(label)', self.site_js)
        self.assertIn('function normalizeSearchValue(value)', self.site_js)
        self.assertIn('function buildAliasLookup(groups)', self.site_js)
        self.assertIn('function expandQueryTokens(query, aliasLookup)', self.site_js)
        self.assertIn('item._searchHaystack = buildTopicSearchHaystack(item);', self.site_js)
        self.assertIn('function createSidebarSection(mainTopic, modulePackLabel)', self.site_js)
        self.assertIn('uiCopy.module_pack_label || ""', self.site_js)
        self.assertIn('mainTopic.pack_slug', self.site_js)
        self.assertIn('.replace(/^\\d+_/, "")', self.site_js)
        self.assertIn('button.setAttribute("data-sidebar-toggle", "")', self.site_js)
        self.assertIn('button.textContent = sidebarLabel;', self.site_js)
        self.assertIn('searchInput.removeAttribute("disabled")', self.site_js)
        self.assertIn('moduleFilter.removeAttribute("disabled")', self.site_js)
        self.assertIn('controlsContainer.hidden = false', self.site_js)
        self.assertIn('sidebarContainer.hidden = false', self.site_js)
        self.assertIn('document.body.classList.remove("sidebar-open")', self.site_js)
        self.assertIn('searchInput.placeholder = uiCopy.search_placeholder || searchInput.placeholder;', self.site_js)
        self.assertIn('allOption.textContent = uiCopy.filter_label || "";', self.site_js)
        self.assertIn('setupResponsiveSidebar(sidebarContainer, sidebarPanel, uiCopy.sidebar_label || "");', self.site_js)
        self.assertIn('emptyState.textContent = uiCopy.empty_state_label || "";', self.site_js)
        self.assertIn('btn.className = "site-nav-link site-nav-link--button topic-done-btn";', self.site_js)
        self.assertNotIn('No topics found.', self.site_js)
        self.assertNotIn('Search topics', self.site_js)
        self.assertNotIn('"Sidebar"', self.site_js)
        self.assertNotIn("'Sidebar'", self.site_js)
        self.assertIn("window.print", self.site_js)


if __name__ == "__main__":
    unittest.main()
