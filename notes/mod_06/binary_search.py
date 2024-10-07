def linear_search(vals: list[int], target: int) -> bool:
    """
    Linear search. Returns True if item in list else False.
    O(n).
    """
    for i in vals:
        if i == target:
            return True
    return False


def binary_search_slice(vals: list[int], target: int) -> bool:
    """
    Recursive binary search using slices.
    sum(i from 1 to log(n) recursive calls, n/2^i) = O(n).
    """
    if len(vals) == 0:
        return False

    mid_idx = len(vals) // 2
    if vals[mid_idx] == target:
        return True
    elif vals[mid_idx] > target:
        return binary_search_slice(vals[:mid_idx], target)
    else:
        return binary_search_slice(vals[mid_idx + 1 :], target)


def binary_search_inds(
    vals: list[int], target: int, low_idx: int = 0, high_idx: int | None = None
) -> int:
    """
    Recursive binary search with no slices passing inds.
    O(log(n)).
    """
    if high_idx is None:
        high_idx = len(vals) - 1

    if low_idx > high_idx:
        return -1

    mid_idx = (low_idx + high_idx) // 2
    if vals[mid_idx] == target:
        return mid_idx
    elif vals[mid_idx] > target:
        return binary_search_inds(vals, target, low_idx, mid_idx - 1)
    else:
        return binary_search_inds(vals, target, mid_idx + 1, high_idx)


def binary_search_loop(vals: list[int], target: int) -> bool:
    """
    Binary search with looping instead of recursion.
    Lower memory overhead than recursive, fewer things in call stack.
    O(log(n)).
    """
    low_idx = 0
    high_idx = len(vals) - 1

    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if vals[mid_idx] == target:
            return mid_idx
        elif vals[mid_idx] > target:
            high_idx = mid_idx - 1
        else:
            low_idx = mid_idx + 1

    return -1


if __name__ == "__main__":
    vals = [4, 6, 7, 8, 12, 16, 18, 19]

    assert linear_search(vals, 18)
    assert linear_search(vals, 17) is False

    assert binary_search_slice(vals, 18)
    assert binary_search_slice(vals, 17) is False

    assert binary_search_inds(vals, 18) == 6
    assert binary_search_inds(vals, 17) == -1

    assert binary_search_loop(vals, 18) == 6
    assert binary_search_loop(vals, 17) == -1
