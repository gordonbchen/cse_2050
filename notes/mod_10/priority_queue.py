from __future__ import annotations

from typing import Any, Iterable


class Entry:
    """An entry that stores an item and a priority."""

    def __init__(self, item: Any, priority: int) -> None:
        self.priority = priority
        self.item = item

    def __lt__(self, other: Entry) -> bool:
        """Compare items based on priority."""
        return self.priority < other.priority


class HeapPriorityQueue:
    """A priority queue represented by a min heap."""

    def __init__(self) -> None:
        self._entries = []

    def _get_parent(self, idx: int) -> int:
        """Return the parent index."""
        return (idx - 1) // 2

    def _get_children(self, idx: int) -> Iterable:
        """Return a range function with idxs of children."""
        left = (2 * idx) + 1
        right = (2 * idx) + 2
        return range(left, min(len(self._entries), right + 1))

    def insert(self, item: Any, priority: int) -> None:
        """
        Insert the item into the priority queue.
        Append the item and recursively up heap.
        """
        self._entries.append(Entry(item, priority))
        self._up_heap(len(self._entries) - 1)

    def _up_heap(self, idx: int) -> None:
        """
        Recursively upheap.
        Find the parent and swap if it is less than the parent.
        """
        parent = self._get_parent(idx)
        if (idx > 0) and (self._entries[idx] < self._entries[parent]):
            self._swap(parent, idx)
            self._up_heap(parent)

    def _swap(self, i: int, j: int) -> None:
        """Swap entries at indexes i and j."""
        self._entries[i], self._entries[j] = self._entries[j], self._entries[i]

    def get_min(self) -> Any:
        """Return the item with the minimum priority."""
        return self._entries[0].item

    def remove_min(self) -> Any:
        """
        Remove and return the item with the minimum priority.
        Swap the root with the last element. Remove the last element (old root).
        Recursively down heap the element at the root.
        """
        self._swap(0, -1)
        min_item = self._entries.pop().item
        self._down_heap(0)
        return min_item

    def _down_heap(self, idx: int) -> None:
        """
        Recursively down heap.
        Find children and swap with the minimum child.
        """

        children = self._get_children(idx)
        if len(children) > 0:
            min_child = min(children, key=lambda x: self._entries[x])
            if self._entries[min_child] < self._entries[idx]:
                self._swap(min_child, idx)
                self._down_heap(min_child)
