(function () {
  "use strict";

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

  function createCard(item, templateRoot) {
    var article;
    var meta;
    var titleLink;
    var subtopic;

    if (templateRoot) {
      article = templateRoot.querySelector(".topic-card").cloneNode(true);
      meta = article.querySelector(".topic-card__meta");
      titleLink = article.querySelector(".topic-card__link");
      subtopic = article.querySelector(".topic-card__subtopic");
    } else {
      article = document.createElement("article");
      article.className = "topic-card";
      meta = document.createElement("p");
      meta.className = "topic-card__meta";
      titleLink = document.createElement("a");
      titleLink.className = "topic-card__link";
      subtopic = document.createElement("p");
      subtopic.className = "topic-card__subtopic";
      var heading = document.createElement("h3");
      heading.className = "topic-card__title";
      heading.appendChild(titleLink);
      article.appendChild(meta);
      article.appendChild(heading);
      article.appendChild(subtopic);
    }

    meta.textContent = item.main_topic_number + " · " + item.main_topic_label;
    titleLink.textContent = item.title;
    titleLink.setAttribute("href", "/topics/" + item.slug + "/");
    subtopic.textContent = item.subtopic_label;

    return article;
  }

  function createSidebarSection(mainTopic) {
    var section = document.createElement("section");
    section.className = "sidebar-group";

    var heading = document.createElement("h3");
    heading.className = "sidebar-group__title";
    heading.textContent = mainTopic.number + " · " + mainTopic.label;
    section.appendChild(heading);

    var list = document.createElement("ul");
    list.className = "sidebar-group__list";

    (mainTopic.topics || []).forEach(function (topic) {
      var item = document.createElement("li");
      var link = document.createElement("a");
      link.className = "sidebar-group__link";
      link.textContent = topic.subtopic_number + " · " + topic.title;
      link.setAttribute("href", "/topics/" + topic.slug + "/");
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
      ? window.matchMedia("(max-width: 900px)")
      : null;
    var button = document.createElement("button");
    var isOpen = true;

    button.type = "button";
    button.className = "catalog-sidebar__toggle";
    button.textContent = label || "Sidebar";
    button.setAttribute("data-sidebar-toggle", "");
    button.setAttribute("aria-controls", "catalog-sidebar-panel");
    panel.id = panel.id || "catalog-sidebar-panel";
    button.setAttribute("aria-expanded", "true");
    container.insertBefore(button, panel);

    function applyState(matchesMobile) {
      isOpen = !matchesMobile;
      panel.hidden = matchesMobile;
      button.hidden = !matchesMobile;
      button.setAttribute("aria-expanded", String(!matchesMobile));
      document.body.classList.toggle("sidebar-collapsed", matchesMobile);
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

    button.addEventListener("click", function () {
      isOpen = !isOpen;
      panel.hidden = !isOpen;
      button.setAttribute("aria-expanded", String(isOpen));
      document.body.classList.toggle("sidebar-open", isOpen);
    });

    panel.addEventListener("click", function (event) {
      var target = event.target;
      if (!mediaQuery || !mediaQuery.matches || !target || target.tagName !== "A") {
        return;
      }

      isOpen = false;
      panel.hidden = true;
      button.setAttribute("aria-expanded", "false");
      document.body.classList.remove("sidebar-open");
    });
  }

  function setupHomeCatalog() {
    var searchInput = document.querySelector("[data-search-input]");
    var moduleFilter = document.querySelector("[data-module-filter]");
    var resultsContainer = document.querySelector("[data-topic-results]");
    var sidebarContainer = document.querySelector("[data-sidebar-container]");
    var sidebarPanel = document.querySelector("[data-sidebar-panel]");

    if (!searchInput || !moduleFilter || !resultsContainer) {
      return;
    }

    var topicIndex = parseJsonScript("[data-topic-index-json]");
    var navigation = parseJsonScript("[data-navigation-json]");
    var uiCopy = parseJsonScript("[data-ui-copy-json]") || {};
    var topics = Array.isArray(topicIndex) ? topicIndex.slice() : [];
    var mainTopics = navigation && Array.isArray(navigation.main_topics) ? navigation.main_topics : [];
    var cardTemplateRoot = document.querySelector("#topic-card-template");

    searchInput.placeholder = uiCopy.search_placeholder || searchInput.placeholder || "Search topics";

    clearChildren(moduleFilter);
    var allOption = document.createElement("option");
    allOption.value = "";
    allOption.textContent = uiCopy.filter_label || "Filter";
    moduleFilter.appendChild(allOption);

    mainTopics.forEach(function (mainTopic) {
      var option = document.createElement("option");
      option.value = mainTopic.number;
      option.textContent = mainTopic.number + " · " + mainTopic.label;
      moduleFilter.appendChild(option);
    });

    if (sidebarPanel) {
      clearChildren(sidebarPanel);
      mainTopics.forEach(function (mainTopic) {
        sidebarPanel.appendChild(createSidebarSection(mainTopic));
      });
      setupResponsiveSidebar(sidebarContainer, sidebarPanel, uiCopy.sidebar_label || "Sidebar");
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
          item.subtopic_label
        ].join(" ").toLowerCase();

        return haystack.indexOf(query) !== -1;
      });

      clearChildren(resultsContainer);

      if (!filtered.length) {
        var emptyState = document.createElement("p");
        emptyState.className = "catalog-results__empty";
        emptyState.textContent = "No topics found.";
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

  setupHomeCatalog();
  setupPrintTrigger();
})();
