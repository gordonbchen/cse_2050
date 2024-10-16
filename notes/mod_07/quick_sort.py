def quick_sort_naive(vals: list[int]) -> list[int]:
    """Quick sort."""
    # Base case.
    if len(vals) <= 1:
        return vals

    # Divide.
    pivot = vals[-1]
    less_than_pivot = [i for i in vals if i < pivot]
    equal_to_pivot = [i for i in vals if i == pivot]
    greater_than_pivot = [i for i in vals if i > pivot]

    # Conquer and combine.
    return (
        quick_sort_naive(less_than_pivot)
        + equal_to_pivot
        + quick_sort_naive(greater_than_pivot)
    )


def quick_sort(vals: list[int], left_idx: int = 0, right_idx: int = None) -> list[int]:
    """Quick sort."""
    if right_idx is None:
        right_idx = len(vals) - 1

    # Base case.
    if right_idx <= left_idx:
        return vals

    # Partition.
    pivot = partition(vals, left_idx, right_idx)

    # Conquer.
    quick_sort(vals, left_idx, pivot - 1)
    quick_sort(vals, pivot + 1, right_idx)
    return vals


def partition(vals: list[int], i: int, j: int) -> int:
    """Find the partition position."""
    pivot = j
    j -= 1

    while i < j:
        while vals[i] <= vals[pivot]:
            i += 1
        while (i < j) and (vals[j] >= vals[pivot]):
            j -= 1

        if vals[i] > vals[j]:
            vals[i], vals[j] = vals[j], vals[i]
            i += 1
            j -= 1

    if vals[i] > vals[pivot]:
        vals[i], vals[pivot] = vals[pivot], vals[i]

    return i


if __name__ == "__main__":
    unsorted_list = [10, 1, 13, 20, 12, 5, 25, 8]
    print(f"Unsorted: {unsorted_list}")
    print(f"Naive Sorted: {quick_sort_naive(unsorted_list)}")

    unsorted_list = [7, 3, 6, 5, 2, 1, 0, 4]
    print(f"Unsorted: {unsorted_list}")
    print(f"Sorted: {quick_sort(unsorted_list)}")
