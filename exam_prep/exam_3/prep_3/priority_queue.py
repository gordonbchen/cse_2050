from __future__ import annotations

from typing import Any


class Entry:
    def __init__(self, item: Any, priority: int) -> None:
        self.item = item
        self.priority = priority

    def __lt__(self, other: Entry) -> bool:
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self, entries: list | None = None) -> None:
        if not entries:
            self.entries = []
            self.idx = {}
        else:
            self.entries = entries
            self.idx = {entry.item: i for (i, entry) in enumerate(entries)}

            for i in reversed(range(len(self) // 2)):
                self._downheap(i)

    def __len__(self) -> int:
        return len(self.entries)

    def put(self, item: Any, priority: int) -> None:
        self.entries.append(Entry(item, priority))
        self.idx[item] = len(self) - 1
        self._upheap(len(self) - 1)

    def get(self) -> Any:
        self.swap(0, len(self) - 1)
        item = self.entries.pop().item
        self.idx.pop(item)

        self._downheap(0)
        return item

    def change_priority(self, item: Any, priority: int) -> None:
        item_idx = self.idx[item]
        entry = self.entries[item_idx]

        old_priority = entry.priority
        entry.priority = priority

        if priority < old_priority:
            self.upheap(item_idx)
        else:
            self.downheap(item_idx)

    def _upheap(self, idx: int) -> None:
        if idx <= 0:
            return

        parent_idx = (idx - 1) // 2
        if self.entries[idx] < self.entries[parent_idx]:
            self._swap(idx, parent_idx)
            self._upheap(parent_idx)

    def _downheap(self, idx: int) -> None:
        left_idx = (2 * idx) + 1
        right_idx = (2 * idx) + 2

        child_idxs = range(left_idx, min(right_idx + 1, len(self)))
        if not child_idxs:
            return

        min_child_idx = min(child_idxs, key=lambda i: self.entries[i])
        if self.entries[min_child_idx] < self.entries[idx]:
            self._swap(idx, min_child_idx)
            self._downheap(min_child_idx)

    def _swap(self, i: int, j: int) -> None:
        self.entries[i], self.entries[j] = self.entries[j], self.entries[i]
        self.idx[self.entries[i].item] = i
        self.idx[self.entries[j].item] = j
