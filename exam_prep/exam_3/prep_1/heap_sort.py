import random


def heap_sort(items):
    """
    Build a max heap using downheapify.
    Swap root with last item, decrement heap size, and downheap the new root.
    """
    for i in reversed(range(len(items) // 2)):
        downheap(i, items, len(items))

    heap_size = len(items)
    for i in range(len(items) - 1):
        heap_size -= 1
        swap(0, heap_size, items)
        downheap(0, items, heap_size)


def downheap(idx, items, heap_size):
    children_idxs = get_children_idxs(idx, heap_size)
    if not children_idxs:
        return

    max_child_idx = max(children_idxs, key=lambda i: items[i])

    if items[idx] < items[max_child_idx]:
        swap(idx, max_child_idx, items)
        downheap(max_child_idx, items, heap_size)


def swap(i, j, items):
    items[i], items[j] = items[j], items[i]


def get_children_idxs(i, heap_size):
    left = (i * 2) + 1
    right = (i * 2) + 2
    return range(left, min(right + 1, heap_size))


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    heap_sort(nums)
    print(nums)

    for i in range(1_000):
        nums = [random.randint(-1_000, 1000) for i in range(random.randint(1, 100))]
        sorted_nums = sorted(nums)
        heap_sort(nums)
        assert nums == sorted_nums
