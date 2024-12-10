class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class Heap:
    def __init__(self):
        self.entries = []

    def insert(self, item, priority):
        """Append element, and upheap last."""
        self.entries.append(Entry(item, priority))
        self.upheap(len(self.entries) - 1)

    def upheap(self, idx):
        """Recursively swap with parent if less than parent."""
        if idx <= 0:
            return

        parent_idx = self.get_parent_idx(idx)
        if self.entries[idx] < self.entries[parent_idx]:
            self.swap(idx, parent_idx)
            self.upheap(parent_idx)

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def swap(self, idx, parent_idx):
        self.entries[idx], self.entries[parent_idx] = self.entries[parent_idx], self.entries[idx]

    def get_min(self):
        return self.entries[0]

    def remove_min(self):
        """Swap first (min) with last, remove last, and downheap first."""
        self.swap(0, len(self.entries) - 1)
        min_entry = self.entries.pop()
        self.downheap(0)
        return min_entry.item

    def get_children_idxs(self, idx):
        left = (idx * 2) + 1
        right = (idx * 2) + 2
        return range(left, min(len(self.entries), right + 1))

    def downheap(self, idx):
        """Recursively swap with min child if greater than child."""
        children_idxs = self.get_children_idxs()
        if not children_idxs:
            return

        min_child = min(children_idxs, key=lambda x: self.entries[x])
        if self.entries[idx] > self.entries[min_child]:
            self.swap(idx, min_child)
            self.downheap(min_child)

    @staticmethod
    def heapify(entries):
        """Downheapify. Iterate down from non-leaf nodes to start and downheap."""
        heap = Heap()
        heap.entries = entries

        for i in reversed(range(len(entries) // 2)):
            heap.downheap(i)

        return heap
