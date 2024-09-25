def find_sum_even(start: int, end: int) -> int:
    """Find the sum of even numbers from start to end."""
    return sum(i for i in range(start, end + 1) if i % 2 == 0)


def find_sum_even_fast(start: int, end: int) -> int:
    """Find the sum of even numbers from start to end (fast with math)."""
    if start % 2 == 1:
        start += 1
    if end % 2 == 1:
        end -= 1

    n = end - start + 1
    return (n - (n // 2)) * ((start + end) / 2)


print(find_sum_even(1, 10))
print(find_sum_even_fast(1, 10))
