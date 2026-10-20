"""Basic metrics for recorded workflow events."""

from collections import Counter
from typing import Any


def event_counts(events: list[dict[str, Any]]) -> dict[str, int]:
    """Return counts grouped by event_type."""
    return dict(Counter(event.get("event_type", "unknown") for event in events))
