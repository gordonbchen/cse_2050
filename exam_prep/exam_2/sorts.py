from random import randint


def insertion_sort(vals: list[int]) -> None:
    """Insertion sort."""
    for i in range(1, len(vals)):
        while (i > 0) and (vals[i] < vals[i - 1]):
            vals[i], vals[i - 1] = vals[i - 1], vals[i]
            i -= 1


def bubble_sort(vals: list[int]) -> None:
    """Bubble sort."""
    for i in range(len(vals) - 1):
        swaps = 0
        for j in range(len(vals) - 1 - i):
            if vals[j] > vals[j + 1]:
                vals[j], vals[j + 1] = vals[j + 1], vals[j]
                swaps += 1

        if swaps == 0:
            break


def selection_sort(vals: list[int]) -> None:
    """Selection sort."""
    for i in range(len(vals) - 1):
        min_idx = i
        for j in range(i + 1, len(vals)):
            if vals[j] < vals[min_idx]:
                min_idx = j

        if min_idx != i:
            vals[min_idx], vals[i] = vals[i], vals[min_idx]


def quick_sort(vals: list[int], left: int = 0, right: int = None) -> None:
    """Quick sort."""
    if right is None:
        right = len(vals)

    if left >= right:
        return

    pivot = right - 1
    i = left
    j = pivot - 1

    while i < j:
        while vals[i] < vals[pivot]:
            i += 1
        while (i < j) and (vals[j] >= vals[pivot]):
            j -= 1

        if i < j:
            vals[i], vals[j] = vals[j], vals[i]

    if vals[i] >= vals[pivot]:
        vals[i], vals[pivot] = vals[pivot], vals[i]
        pivot = i

    quick_sort(vals, left, pivot)
    quick_sort(vals, pivot + 1, right)


def merge_sort(vals: list[int]) -> None:
    """Merge sort."""
    if len(vals) <= 1:
        return vals

    mid = len(vals) // 2
    left = vals[:mid]
    right = vals[mid:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            vals[i + j] = left[i]
            i += 1
        else:
            vals[i + j] = right[j]
            j += 1

    vals[i + j :] = left[i:] + right[j:]


if __name__ == "__main__":
    sort_funcs = [insertion_sort, bubble_sort, selection_sort, quick_sort, merge_sort]
    for sort_func in sort_funcs:
        print(f"\n{sort_func.__name__}")
        vals = [randint(0, 100) for i in range(20)]
        true_sorted = sorted(vals)
        sort_func(vals)

        assert true_sorted == vals
        print(vals)
