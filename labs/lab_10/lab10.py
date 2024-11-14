from __future__ import annotations

from typing import Any


class Entry:
    """An entry in a priority queue. Stores an item and priority."""

    def __init__(self, item: Any, priority: int) -> None:
        """Init the entry with an item and priority."""
        self.item = item
        self.priority = priority

    def __lt__(self, other: Entry) -> bool:
        """Return True if self has a lower priority than other."""
        return self.priority < other.priority

    def __eq__(self, other: Entry) -> bool:
        """Return True if the entries have the same priority and item."""
        return (self.priority == other.priority) and (self.item == other.item)


class PQ_UL:
    """A priority queue represented by an unordered list."""

    def __init__(self) -> None:
        """Init the priority queue."""
        self._entries = []

    def __len__(self) -> int:
        """Return the number of items in the priority queue."""
        return len(self._entries)

    def insert(self, item: Any, priority: int) -> None:
        """Insert the item into the priority queue."""
        self._entries.append(Entry(item, priority))

    def find_min(self) -> Entry | None:
        """
        Return (don't remove) the entry with the minimum priority.
        Return None if the priority queue is empty.
        """
        if len(self) == 0:
            return None
        return min(self._entries)

    def remove_min(self) -> Entry | None:
        """
        Return and remove the entry with the minimum priority.
        Return None if the priority queue is empty.
        """
        if len(self) == 0:
            return None

        min_entry = min(self._entries)
        self._entries.remove(min_entry)
        return min_entry


class PQ_OL:
    """A priority queue represented by a reverse-ordered list."""

    def __init__(self) -> None:
        """Init the priority queue."""
        self._entries = []

    def __len__(self) -> int:
        """Return the number of items in the priority queue."""
        return len(self._entries)

    def insert(self, item: Any, priority: int) -> None:
        """
        Insert the item into the priority queue.
        Sort the entries to maintain order.
        """
        self._entries.append(Entry(item, priority))
        self._entries.sort(reverse=True)

    def find_min(self) -> Entry | None:
        """
        Return (don't remove) the entry with the minimum priority.
        Return None if the priority queue is empty.
        """
        if len(self) == 0:
            return None
        return self._entries[-1]

    def remove_min(self) -> Entry | None:
        """
        Return and remove the entry with the minimum priority.
        Return None if the priority queue is empty.
        """
        if len(self) == 0:
            return None

        return self._entries.pop()
