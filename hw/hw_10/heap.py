from __future__ import annotations

from typing import Any, Iterator

from entry import Entry


class Heap:
    """A min heap represented by a list."""

    def __init__(self) -> None:
        """Init the heap."""
        self._L: list[Entry] = []
        self._idx: dict[Any:int] = {}

    def __len__(self) -> int:
        """Return the number of entries in the heap."""
        return len(self._L)

    def __iter__(self) -> Iterator[Entry]:
        """iterate through the heap, yielding the minimum entry until the heap is empty."""
        while len(self) > 0:
            yield self.remove_min()

    def idx_parent(self, idx: int) -> int | None:
        """
        Return the idx of the parent node.
        Return None if there is no parent (root).
        """
        if idx == 0:
            return None
        return (idx - 1) // 2

    def idx_left(self, idx: int) -> int | None:
        """
        Return the idx of the left child.
        Return None if there is no left child.
        """
        left_idx = (2 * idx) + 1
        if left_idx >= len(self):
            return None
        return left_idx

    def idx_right(self, idx: int) -> int | None:
        """
        Return the idx of the right child.
        Return None if there is no right child.
        """
        right_idx = (2 * idx) + 2
        if right_idx >= len(self):
            return None
        return right_idx

    def idx_min_child(self, idx: int) -> int | None:
        """
        Return the idx of the child with the minimum priority.
        Return None if there are no children.
        """
        left_idx, right_idx = self.idx_left(idx), self.idx_right(idx)
        if (left_idx is None) and (right_idx is None):
            return None

        if left_idx is None:
            return right_idx
        if right_idx is None:
            return left_idx

        if self._L[left_idx] < self._L[right_idx]:
            return left_idx
        return right_idx

    def insert(self, item: Any, priority: int) -> None:
        """
        Insert the item into the heap.
        Assumes that no duplicate items are added.
        Append to the end of the heap, and recursively upheap.
        """
        assert item not in self._idx, "No duplicates should be added to the heap."
        self._L.append(Entry(item, priority))
        self._idx[item] = len(self) - 1
        self._upheap(len(self) - 1)

    def remove_min(self) -> Entry | None:
        """
        Remove and return the minimum entry.
        Returns None if there are no entries.
        Swap the root (min b/c min heap) with the final node,
        remove the final node from the list and dict,
        and recursively downheap from the root (if there still is one).
        """
        if len(self) == 0:
            return None

        self._swap(0, len(self) - 1)
        min_entry = self._L.pop()
        del self._idx[min_entry.item]

        if len(self) > 0:
            self._downheap(0)
        return min_entry

    def change_priority(self, item: Any, priority: int) -> int:
        """
        Change the priority of the given item, and upheap/downheap as required.
        Assumes that the item is already in the heap.
        Return the new idx of the item.
        """
        assert item in self._idx, "Item should already be in heap."

        idx = self._idx[item]
        entry = self._L[idx]
        old_priority = entry.priority
        entry.priority = priority
        if priority > old_priority:
            self._downheap(idx)
        else:
            self._upheap(idx)

        return self._idx[item]

    def _swap(self, i: int, j: int) -> None:
        """Swap entries at idxs i and j and update the dictionary of item, idx pairs."""
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[j].item] = j
        self._idx[self._L[i].item] = i

    def _upheap(self, idx: int) -> None:
        """Recursively upheap, swapping with parent if this is less."""
        if idx == 0:
            return

        parent_idx = self.idx_parent(idx)
        if self._L[idx] < self._L[parent_idx]:
            self._swap(idx, parent_idx)
            self._upheap(parent_idx)

    def _downheap(self, idx: int) -> None:
        """Recursively downheap, swapping with the minimum child if the child is less."""
        min_child = self.idx_min_child(idx)
        if min_child is None:
            return

        if self._L[min_child] < self._L[idx]:
            self._swap(min_child, idx)
            self._downheap(min_child)

    @staticmethod
    def heapify(entries: list[Entry]) -> Heap:
        """
        Create and return a heap from a list of unordered entries.
        Iterate down from the middle and recursively downheap.
        """
        heap = Heap()
        heap._L = entries
        heap._idx = {entries[i].item: i for i in range(len(entries))}

        for i in reversed(range(len(heap) // 2)):
            heap._downheap(i)

        return heap
