def is_sorted(vals: list[int]) -> bool:
    """
    Return True if vals is sorted.
    O(n).
    """
    for i in range(len(vals) - 1):
        if vals[i] > vals[i + 1]:
            return False
    return True


if __name__ == "__main__":
    sorted_vals = [3, 6, 7, 11, 32, 33, 53]
    unsorted_vals = [3, 6, 7, 53, 32, 33, 11]

    assert is_sorted(sorted_vals)
    assert is_sorted(unsorted_vals) is False
