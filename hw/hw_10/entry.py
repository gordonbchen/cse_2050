from __future__ import annotations

from typing import Any


class Entry:
    """An entry that stores an item and priority."""

    def __init__(self, item: Any, priority: int) -> None:
        """Init entry."""
        self.item = item
        self.priority = priority

    def __eq__(self, other: Entry) -> bool:
        """Return True if the other entry has the same priority."""
        return self.priority == other.priority

    def __lt__(self, other: Entry) -> bool:
        """Return True if self has a lower priority than other."""
        return self.priority < other.priority

    def __le__(self, other: Entry) -> bool:
        """Return True if self is less than or equal to self."""
        return (self == other) or (self < other)

    def __repr__(self) -> str:
        """Return a str repr of the entry."""
        return f"Entry(item={self.item}, priority={self.priority})"
