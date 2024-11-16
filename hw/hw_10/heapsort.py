def idx_left(L: list, idx: int, right: int) -> int | None:
    """Return the idx of the left child if it is less than right, or None."""
    left_idx = (idx * 2) + 1
    if left_idx < right:
        return left_idx
    return None


def idx_right(L: list, idx: int, right: int) -> int | None:
    """Return the idx of the right child if it is less than right, or None."""
    right_idx = (idx * 2) + 2
    if right_idx < right:
        return right_idx
    return None


def idx_max_child(L: list, idx: int, right: int) -> int | None:
    """Return the idx of the max child if it is less than right, or None."""
    left_idx, right_idx = idx_left(L, idx, right), idx_right(L, idx, right)
    if (left_idx, right_idx) == (None, None):
        return None

    if left_idx is None:
        return right_idx
    if right_idx is None:
        return left_idx

    if L[left_idx] > L[right_idx]:
        return left_idx
    return right_idx


def swap(L: list, i: int, j: int) -> None:
    """Swap idxs i and j in the list."""
    L[i], L[j] = L[j], L[i]


def downheap(L: list, idx: int, right: int) -> None:
    """
    Recursively downheap the item at idx, swapping with max child if this is less.
    Note that the heap is a max-heap.
    Stop before right.
    """
    max_child = idx_max_child(L, idx, right)
    if max_child is None:
        return

    if L[max_child] > L[idx]:
        swap(L, max_child, idx)
        downheap(L, max_child, right)


def heapsort(L: list) -> None:
    """
    Heapsort the list in-place.
    Create a max heap out of the list (using heapify).
    Swap the max item (root) with the last item, decrement right,
    and downheap, until no items remain.
    """
    # Heapify.
    for i in reversed(range(len(L) // 2)):
        downheap(L, i, len(L))

    right = len(L)
    while right > 1:
        right -= 1
        swap(L, 0, right)
        downheap(L, 0, right)
