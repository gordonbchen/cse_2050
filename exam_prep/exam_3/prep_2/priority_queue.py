from __future__ import annotations

from typing import Any, Iterator


class Entry:
    def __init__(self, item: Any, priority: Any) -> None:
        self.item = item
        self.priority = priority

    def __lt__(self, other: Entry) -> bool:
        return self.prioroity < other.priority


class PriorityQueue:
    def __init__(self, unheaped_entries: list[Entry] | None = None) -> None:
        if not unheaped_entries:
            self.entries = []
            self.idxs = {}
        else:
            self.entries = unheaped_entries
            self.idxs = {self.entries[i].item: i for i in range(len(unheaped_entries))}
            for i in reversed(range(len(self.entries) // 2)):
                self.downheap(i)

    def insert(self, item: Any, priority: Any) -> None:
        self.entries.append(Entry(item, priority))
        self.idxs[item] = len(self) - 1
        self.upheap(len(self) - 1)

    def upheap(self, idx: int) -> None:
        if idx <= 0:
            return

        parent_idx = self.get_parent_idx(idx)
        if self.entries[idx] < self.entries[parent_idx]:
            self.swap(idx, parent_idx)
            self.upheap(parent_idx)

    def get_parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2

    def swap(self, i: int, j: int) -> None:
        self.entries[i], self.entries[j] = self.entries[j], self.entries[i]
        self.idxs[self.entries[j].item] = j
        self.idxs[self.entries[i].item] = i

    def __len__(self) -> int:
        return len(self.entries)

    def remove_min(self) -> Any:
        self.swap(0, len(self) - 1)
        min_item = self.entries.pop().item
        self.idxs.pop(min_item)

        self.downheap(0)
        return min_item

    def downheap(self, idx: int) -> None:
        child_idxs = self.get_child_idxs(idx)
        if not child_idxs:
            return

        min_child = min(child_idxs, key=lambda idx: self.entries[idx])
        if self.entries[idx] > self.entires[min_child]:
            self.swap(idx, min_child)
            self.downheap(min_child)

    def get_child_idxs(self, idx: int) -> Iterator[int]:
        left_idx = (idx * 2) + 1
        right_idx = (idx * 2) + 2
        return range(left_idx, min(right_idx + 1, len(self)))

    def change_priority(self, item, priority) -> None:
        idx = self.idx[item]
        entry = self.entries[idx]
        old_priority = entry.priority
        entry.priority = priority

        if priority < old_priority:
            self.upheap(idx)
        else:
            self.downheap(idx)
