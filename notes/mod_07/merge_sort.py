def merge_sort(vals: list[int]) -> list[int]:
    """Merge sort in-place."""
    # Base case.
    if len(vals) <= 1:
        return vals

    # Divide and conquer.
    mid_idx = len(vals) // 2
    left = vals[:mid_idx]
    right = vals[mid_idx:]
    merge_sort(left)
    merge_sort(right)

    # Combine.
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            vals[i + j] = left[i]
            i += 1
        else:
            vals[i + j] = right[j]
            j += 1

    vals[i + j :] = left[i:] + right[j:]

    return vals


if __name__ == "__main__":
    unsorted_list = [10, 1, 13, 20, 12, 5, 25, 8]
    print(f"Unsorted: {unsorted_list}")
    print(f"Sorted: {merge_sort(unsorted_list)}")
