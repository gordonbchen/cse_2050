import math

from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes


class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""

    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3


def linear_scan(L: list[int]) -> MagicCase:
    """Find the number of inversions and return the appropriate sorting case."""
    inversions = 0
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            inversions += 1

    if inversions == 0:
        return MagicCase.SORTED
    elif inversions == (len(L) - 1):
        return MagicCase.REVERSE_SORTED
    elif inversions <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    return MagicCase.GENERAL


def reverse_list(L: list[int], alg_set: set[str] = None) -> set[str]:
    """Reverse the list in-place."""
    for i in range(len(L) // 2):
        L[i], L[-1 - i] = L[-1 - i], L[i]

    if alg_set is None:
        alg_set = set()
    alg_set.add(reverse_list.__name__)
    return alg_set


def magic_insertionsort(
    L: list[int], left: int = 0, right: int = None, alg_set: set[str] = None
) -> set[str]:
    """Insertion sort the sublist in-place."""
    if right is None:
        right = len(L)

    for i in range(left + 1, right):
        while (i > left) and (L[i] < L[i - 1]):
            L[i], L[i - 1] = L[i - 1], L[i]
            i -= 1

    if alg_set is None:
        alg_set = set()
    alg_set.add(magic_insertionsort.__name__)
    return alg_set


def magic_mergesort(
    L: list[int], left: int, right: int, alg_set: set[str] = None
) -> None:
    """Magic merge sort in-place."""
    if alg_set is None:
        alg_set = set()
    alg_set.add(magic_mergesort.__name__)

    _magic_mergesort(L, left, right, alg_set)


def _magic_mergesort(L: list[int], left: int, right: int, alg_set: set[str]) -> None:
    """Magic merge sort in-place"""
    # Use insertion sort if the sublist has 20 or fewer items.
    if (right - left) <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return

    # Divide.
    mid_idx = (left + right) // 2
    left_vals = L[left:mid_idx]
    right_vals = L[mid_idx:right]

    # Conquer.
    _magic_mergesort(left_vals, 0, len(left_vals), alg_set)
    _magic_mergesort(right_vals, 0, len(right_vals), alg_set)

    # Combine.
    i = 0
    j = 0
    while (i < len(left_vals)) and (j < len(right_vals)):
        if left_vals[i] <= right_vals[j]:
            L[left + i + j] = left_vals[i]
            i += 1
        else:
            L[left + i + j] = right_vals[j]
            j += 1

    L[left + i + j : right] = left_vals[i:] + right_vals[j:]


def magic_quicksort(
    L: list[int],
    left: int = 0,
    right: int = None,
    depth: int = 0,
    alg_set: set[str] = None,
) -> set[str]:
    """Quicksort in-place."""
    if alg_set is None:
        alg_set = set()
    alg_set.add(magic_quicksort.__name__)

    if right is None:
        right = len(L)

    depth_threshold = 0 if len(L) == 0 else (math.log2(len(L)) + 1) * 3
    _magic_quicksort(L, left, right, depth_threshold, depth, alg_set)

    return alg_set


def _magic_quicksort(
    L: list[int],
    left: int,
    right: int,
    depth_threshold: int,
    depth: int,
    alg_set: set[str],
) -> None:
    """Quicksort in-place."""
    # Use insertion sort if the sublist has 20 or fewer items.
    if (right - left) <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return

    # Use merge sort if the depth exceeds max threshold.
    if depth > depth_threshold:
        magic_mergesort(L, left, right, alg_set)
        return

    # Partition.
    pivot = partition(L, left, right)
    _magic_quicksort(L, left, pivot, depth_threshold, depth + 1, alg_set)
    _magic_quicksort(L, pivot + 1, right, depth_threshold, depth + 1, alg_set)


def partition(L: list[int], left: int, right: int) -> int:
    """Find the pivot position."""
    pivot = right - 1
    i = left
    j = right - 2

    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while (L[j] >= L[pivot]) and (i < j):
            j -= 1

        if i < j:
            L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    return pivot


def magicsort(L: list[int]) -> set[str]:
    """Magic sort the list in-place. Return the set of sorting algorithms used."""
    sort_case = linear_scan(L)
    if sort_case == MagicCase.SORTED:
        return set()
    elif sort_case == MagicCase.REVERSE_SORTED:
        return reverse_list(L)
    elif sort_case == MagicCase.CONSTANT_INVERSIONS:
        return magic_insertionsort(L)
    else:
        return magic_quicksort(L)
