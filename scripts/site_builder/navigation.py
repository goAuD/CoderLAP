from __future__ import annotations

from collections import OrderedDict
from collections import Counter

from .models import TopicRecord


def _sort_key(topic: TopicRecord) -> tuple[int, int, str]:
    return (int(topic.main_topic_number), int(topic.subtopic_number), topic.id)


def _validate_unique_topic_ids(topics: list[TopicRecord]) -> None:
    counts = Counter(topic.id for topic in topics)
    duplicates = [topic_id for topic_id, count in counts.items() if count > 1]
    if duplicates:
        duplicate_list = ", ".join(sorted(duplicates))
        raise ValueError(f"Duplicate topic ids are not allowed: {duplicate_list}")


def build_navigation(topics: list[TopicRecord]) -> dict:
    _validate_unique_topic_ids(topics)
    ordered_topics = sorted(topics, key=_sort_key)

    main_topics: OrderedDict[str, dict] = OrderedDict()
    topic_map: dict[str, dict] = {}

    for index, topic in enumerate(ordered_topics):
        main_topic = main_topics.setdefault(
            topic.main_topic_number,
            {
                "number": topic.main_topic_number,
                "label": topic.main_topic_dir,
                "topics": [],
            },
        )
        main_topic["topics"].append(
            {
                "id": topic.id,
                "title": topic.title,
                "slug": topic.slug,
                "subtopic_number": topic.subtopic_number,
                "subtopic_dir": topic.subtopic_dir,
            }
        )

        topic_map[topic.id] = {
            "id": topic.id,
            "slug": topic.slug,
            "previous_id": ordered_topics[index - 1].id if index > 0 else None,
            "next_id": ordered_topics[index + 1].id if index + 1 < len(ordered_topics) else None,
        }

    return {
        "main_topics": list(main_topics.values()),
        "topics": topic_map,
    }
