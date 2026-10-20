"""In-memory event recorder for the initial prototype."""

from typing import Any


class InMemoryRecorder:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def record(self, event: dict[str, Any]) -> None:
        self.events.append(event)
