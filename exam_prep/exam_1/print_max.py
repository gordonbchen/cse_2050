def print_max(alist: list[int]) -> int | None:
    """Return the max value < 10 in the list or None."""
    max_val = float("-inf")
    for i in alist:
        if i < 10:
            max_val = max(max_val, i)
    return max_val if max_val > float("-inf") else None


print(print_max([]))
print(print_max([10, 11, 12]))
print(print_max([-10, 1, 2, 3, 9, 10, 11]))
print(print_max([3, 3, 7, 3, 1, 9, 4, 3]))
