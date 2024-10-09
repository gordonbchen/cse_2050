def is_sorted(vals: list[int]) -> bool:
    """
    Return True if vals is sorted.
    O(n).
    """
    for i in range(len(vals) - 1):
        if vals[i] > vals[i + 1]:
            return False
    return True


def swap(vals: list[int], i: int, j: int) -> None:
    """Swap elements of vals at inds i and j in-place."""
    vals[i], vals[j] = vals[j], vals[i]


def bubble_sort(vals: list[int]) -> int:
    """
    In-place bubble sort. Return the number of swaps.
    Best case: O(n) comparisons, O(1) swaps.
    Worst case: O(n^2) comparisons, O(n^2) swaps.
    """
    total_swaps = 0
    for i in range(len(vals) - 1):
        iter_swaps = 0
        for j in range(len(vals) - 1 - i):
            if vals[j] > vals[j + 1]:
                swap(vals, j, j + 1)
                iter_swaps += 1

        if iter_swaps == 0:
            break

        total_swaps += iter_swaps
    return total_swaps


def selection_sort(vals: list[int]) -> int:
    """
    In-place selection sort. Returns the number of swaps.
    Best case: O(n^2) comparisons, O(1) swaps.
    Worst case: O(n^2) comparisons, O(n) swaps.
    """
    total_swaps = 0
    for i in range(len(vals) - 1):
        max_idx = 0
        for j in range(len(vals) - i):
            if vals[j] > vals[max_idx]:
                max_idx = j

        if (len(vals) - i - 1) != max_idx:
            swap(vals, -1 - i, max_idx)
            total_swaps += 1

    return total_swaps


def insertion_sort(vals: list[int]) -> int:
    """
    In-place insertion sort. Returns the number of swaps.
    Best case: O(n) comparisons, O(1) swaps.
    Worst case: O(n^2) comparisons, O(n^2) swaps.
    """
    total_swaps = 0
    for i in range(1, len(vals)):
        j = len(vals) - i - 1
        while (j < len(vals) - 1) and (vals[j] > vals[j + 1]):
            swap(vals, j, j + 1)
            j += 1
            total_swaps += 1

    return total_swaps


def get_sorted_vals() -> list[int]:
    return [1, 2, 3, 4, 5]


def get_unsorted_vals() -> list[int]:
    return [4, 5, 2, 3, 1]


if __name__ == "__main__":
    # Check is_sorted func.
    assert is_sorted(get_sorted_vals())
    assert is_sorted(get_unsorted_vals()) is False

    for sort_func in (bubble_sort, selection_sort, insertion_sort):
        print("\n" + sort_func.__name__)

        for val_getter in (get_sorted_vals, get_unsorted_vals):
            vals = val_getter()
            print(f"{val_getter.__name__}: swaps={sort_func(vals)}")
            assert is_sorted(vals)
