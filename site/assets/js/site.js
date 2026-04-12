(function () {
  "use strict";

  /* ── Progress persistence (localStorage) ────────────────────────── */
  var PROGRESS_KEY = "coderlap_progress";

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(PROGRESS_KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function saveProgress(data) {
    try {
      localStorage.setItem(PROGRESS_KEY, JSON.stringify(data));
    } catch (e) {
      // quota exceeded — silently ignore
    }
  }

  function getStatus(topicId) {
    var data = loadProgress();
    var entry = data[topicId];
    return entry ? entry.status : null;
  }

  function setStatus(topicId, status) {
    var data = loadProgress();
    data[topicId] = { status: status, ts: Date.now() };
    saveProgress(data);
  }

  function markViewed(topicId) {
    if (!getStatus(topicId)) {
      setStatus(topicId, "viewed");
    }
  }

  function markDone(topicId) {
    setStatus(topicId, "done");
  }

  function countByStatus() {
    var data = loadProgress();
    var viewed = 0;
    var done = 0;
    var keys = Object.keys(data);
    for (var i = 0; i < keys.length; i++) {
      var s = data[keys[i]].status;
      if (s === "done") { done++; }
      else if (s === "viewed") { viewed++; }
    }
    return { viewed: viewed, done: done, total: viewed + done };
  }

  function parseJsonScript(selector) {
    var node = document.querySelector(selector);
    if (!node) {
      return null;
    }

    try {
      return JSON.parse(node.textContent || "");
    } catch (error) {
      return null;
    }
  }

  function clearChildren(node) {
    while (node.firstChild) {
      node.removeChild(node.firstChild);
    }
  }

  function formatMainTopicLabel(label) {
    return String(label || "")
      .replace(/^\d+_/, "")
      .replace(/_/g, " ")
      .trim();
  }

  /* ── Resolve site root from embedded JSON (language-aware) ──── */
  var SITE_ROOT = "/";

  function createCard(item, templateRoot) {
    var article;
    var meta;
    var titleLink;

    if (templateRoot) {
      article = templateRoot.querySelector(".topic-card").cloneNode(true);
      meta = article.querySelector(".topic-card__meta");
      titleLink = article.querySelector(".topic-card__link");
    } else {
      article = document.createElement("article");
      article.className = "topic-card";
      meta = document.createElement("p");
      meta.className = "topic-card__meta";
      titleLink = document.createElement("a");
      titleLink.className = "topic-card__link";
      var heading = document.createElement("h3");
      heading.className = "topic-card__title";
      heading.appendChild(titleLink);
      article.appendChild(meta);
      article.appendChild(heading);
    }

    meta.textContent = item.main_topic_number + " · " + formatMainTopicLabel(item.main_topic_label);
    titleLink.textContent = item.title;
    titleLink.setAttribute("href", SITE_ROOT + "topics/" + item.slug + "/");

    var status = getStatus(item.id);
    if (status === "done") {
      article.classList.add("topic-card--done");
    } else if (status === "viewed") {
      article.classList.add("topic-card--viewed");
    }

    return article;
  }

  function createSidebarSection(mainTopic) {
    var section = document.createElement("section");
    section.className = "sidebar-group";

    var heading = document.createElement("h3");
    heading.className = "sidebar-group__title";
    heading.textContent = mainTopic.number + " · " + formatMainTopicLabel(mainTopic.label);
    section.appendChild(heading);

    var list = document.createElement("ul");
    list.className = "sidebar-group__list";

    (mainTopic.topics || []).forEach(function (topic) {
      var item = document.createElement("li");
      var link = document.createElement("a");
      link.className = "sidebar-group__link";
      link.textContent = topic.subtopic_number + " · " + topic.title;
      link.setAttribute("href", SITE_ROOT + "topics/" + topic.slug + "/");

      var status = getStatus(topic.id);
      if (status === "done") {
        link.classList.add("sidebar-group__link--done");
      } else if (status === "viewed") {
        link.classList.add("sidebar-group__link--viewed");
      }

      item.appendChild(link);
      list.appendChild(item);
    });

    section.appendChild(list);
    return section;
  }

  function setupResponsiveSidebar(container, panel, label) {
    if (!container || !panel) {
      return;
    }

    var mediaQuery = typeof window.matchMedia === "function"
      ? window.matchMedia("(max-width: 63.99rem)")
      : null;
    var button = document.createElement("button");
    var sidebarLabel = typeof label === "string" ? label : "";

    button.type = "button";
    button.className = "catalog-sidebar__toggle";
    button.textContent = sidebarLabel;
    button.setAttribute("data-sidebar-toggle", "");
    button.setAttribute("aria-controls", "catalog-sidebar-panel");
    panel.id = panel.id || "catalog-sidebar-panel";
    button.setAttribute("aria-expanded", "true");
    container.insertBefore(button, panel);

    // Desktop: sidebar always visible, no toggle button
    // Mobile (<64rem): sidebar collapsed by default, toggle button visible
    function applyState() {
      button.hidden = true;
      panel.hidden = false;
      document.body.classList.remove("sidebar-open");
      document.body.classList.remove("sidebar-collapsed");
    }

    if (mediaQuery) {
      applyState(mediaQuery.matches);
      if (typeof mediaQuery.addEventListener === "function") {
        mediaQuery.addEventListener("change", function (event) {
          applyState(event.matches);
        });
      } else if (typeof mediaQuery.addListener === "function") {
        mediaQuery.addListener(function (event) {
          applyState(event.matches);
        });
      }
    }

    // Toggle button — only relevant on mobile to show/hide Content panel inline
    button.addEventListener("click", function () {
      var wasCollapsed = document.body.classList.contains("sidebar-collapsed");
      document.body.classList.toggle("sidebar-collapsed");
      panel.hidden = !wasCollapsed;
      button.setAttribute("aria-expanded", String(wasCollapsed));
    });

    // Quick view overlay — opens on any viewport via navbar link
    function openOverlay() {
      panel.hidden = false;
      document.body.classList.add("sidebar-open");
    }

    function closeOverlay() {
      document.body.classList.remove("sidebar-open");
    }

    // Close overlay when clicking a link inside the panel
    panel.addEventListener("click", function (event) {
      var target = event.target;
      if (!document.body.classList.contains("sidebar-open") || !target || target.tagName !== "A") {
        return;
      }
      closeOverlay();
    });

    // Close overlay when clicking the backdrop
    document.addEventListener("click", function (event) {
      if (!document.body.classList.contains("sidebar-open")) {
        return;
      }
      // Check if click is on the backdrop (::after of .site-shell)
      // The backdrop covers the whole screen, so if click target is outside the sidebar, close it
      var sidebar = container;
      if (!sidebar.contains(event.target) && !event.target.hasAttribute("data-quick-view-link")) {
        closeOverlay();
      }
    });

    // Navbar Quick view link toggles the overlay on any viewport
    var quickViewLink = document.querySelector("[data-quick-view-link]");
    if (quickViewLink) {
      quickViewLink.addEventListener("click", function (event) {
        event.preventDefault();
        if (document.body.classList.contains("sidebar-open")) {
          closeOverlay();
        } else {
          openOverlay();
        }
      });
    }
  }

  function setupHomeCatalog() {
    var controlsContainer = document.querySelector("[data-catalog-controls]");
    var searchInput = document.querySelector("[data-search-input]");
    var moduleFilter = document.querySelector("[data-module-filter]");
    var resultsContainer = document.querySelector("[data-topic-results]");
    var sidebarContainer = document.querySelector("[data-sidebar-container]");
    var sidebarPanel = document.querySelector("[data-sidebar-panel]");

    if (!controlsContainer || !searchInput || !moduleFilter || !resultsContainer) {
      return;
    }

    var topicIndex = parseJsonScript("[data-topic-index-json]");
    var navigation = parseJsonScript("[data-navigation-json]");
    var uiCopy = parseJsonScript("[data-ui-copy-json]") || {};
    if (!Array.isArray(topicIndex) || !navigation || !Array.isArray(navigation.main_topics)) {
      return;
    }

    SITE_ROOT = uiCopy.site_root || "/";

    var topics = Array.isArray(topicIndex) ? topicIndex.slice() : [];
    var mainTopics = navigation.main_topics.slice();
    var cardTemplateRoot = document.querySelector("#topic-card-template");

    searchInput.placeholder = uiCopy.search_placeholder || searchInput.placeholder;
    searchInput.removeAttribute("disabled");
    moduleFilter.removeAttribute("disabled");
    controlsContainer.hidden = false;

    clearChildren(moduleFilter);
    var allOption = document.createElement("option");
    allOption.value = "";
    allOption.textContent = uiCopy.filter_label || "";
    moduleFilter.appendChild(allOption);

    mainTopics.forEach(function (mainTopic) {
      var option = document.createElement("option");
      option.value = mainTopic.number;
      option.textContent = mainTopic.number + " · " + formatMainTopicLabel(mainTopic.label);
      moduleFilter.appendChild(option);
    });

    if (sidebarPanel) {
      clearChildren(sidebarPanel);
      mainTopics.forEach(function (mainTopic) {
        sidebarPanel.appendChild(createSidebarSection(mainTopic));
      });
      if (sidebarContainer) {
        sidebarContainer.hidden = false;
      }
      setupResponsiveSidebar(sidebarContainer, sidebarPanel, uiCopy.sidebar_label || "");
    }

    function renderResults() {
      var query = (searchInput.value || "").trim().toLowerCase();
      var selectedModule = moduleFilter.value;
      var filtered = topics.filter(function (item) {
        var matchesModule = !selectedModule || item.main_topic_number === selectedModule;
        if (!matchesModule) {
          return false;
        }

        if (!query) {
          return true;
        }

        var haystack = [
          item.id,
          item.title,
          item.main_topic_label,
          item.subtopic_label,
          item.main_topic_number
        ].join(" ").toLowerCase().replace(/_/g, " ");

        var words = query.split(/\s+/);
        for (var w = 0; w < words.length; w++) {
          if (words[w] && haystack.indexOf(words[w]) === -1) {
            return false;
          }
        }
        return true;
      });

      clearChildren(resultsContainer);

      if (!filtered.length) {
        var emptyState = document.createElement("p");
        emptyState.className = "catalog-results__empty";
        emptyState.textContent = uiCopy.empty_state_label || "";
        resultsContainer.appendChild(emptyState);
        return;
      }

      filtered.forEach(function (item) {
        resultsContainer.appendChild(createCard(item, cardTemplateRoot));
      });
    }

    searchInput.addEventListener("input", renderResults);
    moduleFilter.addEventListener("change", renderResults);
    renderResults();
  }

  function setupPrintTrigger() {
    var trigger = document.querySelector("[data-print-trigger]");
    if (!trigger) {
      return;
    }

    trigger.addEventListener("click", function () {
      if (typeof window.print === "function") {
        window.print();
      }
    });
  }

  function setupTopicProgress() {
    var topicId = document.body.getAttribute("data-topic-id");
    if (!topicId) {
      return;
    }

    // Auto mark as viewed
    markViewed(topicId);

    // Insert "Mark as done" button into .topic-actions
    var actions = document.querySelector(".topic-actions");
    if (!actions) {
      return;
    }

    var uiCopy = parseJsonScript("[data-ui-copy-json]") || {};
    var doneLabel = uiCopy.mark_done_label || "Done";
    var undoLabel = uiCopy.mark_undo_label || "Undo";

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "site-nav-link site-nav-link--button topic-done-btn";
    btn.setAttribute("data-done-toggle", "");

    function updateButton() {
      var status = getStatus(topicId);
      if (status === "done") {
        btn.textContent = "✓ " + undoLabel;
        btn.classList.add("topic-done-btn--active");
      } else {
        btn.textContent = doneLabel;
        btn.classList.remove("topic-done-btn--active");
      }
    }

    btn.addEventListener("click", function () {
      var status = getStatus(topicId);
      if (status === "done") {
        setStatus(topicId, "viewed");
      } else {
        markDone(topicId);
      }
      updateButton();
    });

    updateButton();
    actions.appendChild(btn);
  }

  // Quick View overlay for non-home pages (topic, legal).
  // On the home page, setupHomeCatalog already wires the overlay.
  function setupQuickViewAnywhere() {
    if (document.querySelector("[data-catalog-controls]")) {
      return;
    }

    var quickViewLink = document.querySelector("[data-quick-view-link]");
    if (!quickViewLink) {
      return;
    }

    var sidebar = null;
    var panel = null;
    var ready = false;

    function buildSidebar(mainTopics) {
      sidebar = document.createElement("aside");
      sidebar.className = "catalog-sidebar";
      sidebar.hidden = true;

      panel = document.createElement("div");
      panel.setAttribute("data-sidebar-panel", "");

      mainTopics.forEach(function (mainTopic) {
        panel.appendChild(createSidebarSection(mainTopic));
      });

      sidebar.appendChild(panel);

      var shell = document.querySelector(".site-shell");
      if (shell) {
        shell.appendChild(sidebar);
      }

      panel.addEventListener("click", function (event) {
        if (event.target && event.target.tagName === "A") {
          closeOverlay();
        }
      });
    }

    function openOverlay() {
      if (!sidebar) {
        return;
      }
      sidebar.hidden = false;
      document.body.classList.add("sidebar-open");
    }

    function closeOverlay() {
      document.body.classList.remove("sidebar-open");
      if (sidebar) {
        sidebar.hidden = true;
      }
    }

    document.addEventListener("click", function (event) {
      if (!document.body.classList.contains("sidebar-open")) {
        return;
      }
      if (sidebar && !sidebar.contains(event.target) && !event.target.hasAttribute("data-quick-view-link")) {
        closeOverlay();
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && document.body.classList.contains("sidebar-open")) {
        closeOverlay();
      }
    });

    quickViewLink.addEventListener("click", function (event) {
      event.preventDefault();

      if (document.body.classList.contains("sidebar-open")) {
        closeOverlay();
        return;
      }

      if (ready) {
        openOverlay();
        return;
      }

      var uiCopyQV = parseJsonScript("[data-ui-copy-json]") || {};
      var root = uiCopyQV.site_root || SITE_ROOT;
      fetch(root + "data/navigation.json")
        .then(function (res) { return res.json(); })
        .then(function (nav) {
          if (!nav || !Array.isArray(nav.main_topics)) {
            return;
          }
          SITE_ROOT = root;
          buildSidebar(nav.main_topics);
          ready = true;
          openOverlay();
        })
        .catch(function () {
          window.location.href = root + "#catalog-title";
        });
    });
  }

  function setupProgressCounter() {
    var heroPill = document.querySelector("[data-hero-progress]");
    var topicIndex = parseJsonScript("[data-topic-index-json]");
    var totalTopics = Array.isArray(topicIndex) ? topicIndex.length : 233;
    var counts = countByStatus();

    if (heroPill) {
      var pct = totalTopics > 0 ? Math.round((counts.done / totalTopics) * 100) : 0;
      var radius = 8;
      var circ = 2 * Math.PI * radius;
      var offset = circ - (pct / 100) * circ;

      heroPill.innerHTML =
        '<svg class="hero-progress-pill__ring" width="22" height="22" viewBox="0 0 22 22" aria-hidden="true">' +
          '<circle cx="11" cy="11" r="' + radius + '" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2.5"/>' +
          '<circle cx="11" cy="11" r="' + radius + '" fill="none" stroke="#c8b45a" stroke-width="2.5"' +
            ' stroke-dasharray="' + circ.toFixed(1) + '" stroke-dashoffset="' + offset.toFixed(1) + '"' +
            ' stroke-linecap="round" transform="rotate(-90 11 11)"/>' +
        '</svg>' +
        '<span>' + counts.done + ' / ' + totalTopics + '</span>';
      heroPill.classList.add("hero-progress-pill--active");
      heroPill.hidden = false;
    }
  }

  function setupBackToTop() {
    var btn = document.querySelector("[data-back-to-top]");
    if (!btn) {
      return;
    }
    btn.hidden = false;

    var visible = false;
    var threshold = 400;

    function onScroll() {
      var shouldShow = (window.pageYOffset || document.documentElement.scrollTop) > threshold;
      if (shouldShow !== visible) {
        visible = shouldShow;
        if (visible) {
          btn.classList.add("is-visible");
        } else {
          btn.classList.remove("is-visible");
        }
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  setupHomeCatalog();
  setupQuickViewAnywhere();
  setupPrintTrigger();
  setupTopicProgress();
  setupProgressCounter();
  setupBackToTop();
})();
