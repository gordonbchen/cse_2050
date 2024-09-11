import random
import time


def generate_lists(size: int) -> tuple[list[int], list[int]]:
    """Generate 2 lists of the given size containing unique integers."""
    return (random.sample(range(size * 2), size) for i in range(2))


def find_common(list1: list[int], list2: list[int]) -> int:
    """Find the number of common elements between the 2 lists."""
    n_common = 0                # 1
    for i in list1:             # n *
        for j in list2:         # n *
            if i == j:          # 1
                n_common += 1   # 1
                break           # 1
    return n_common             # 1
                                # ----
                                # 1 + (n)((n - 1)(1) + (1 + 1 + 1)) + 1 = 2 + n^2 + 2n = O(n^2)


def find_common_efficient(list1: list[int], list2: list[int]) -> int:
    """Find the number of common elements between the 2 lists."""
    combined_size = len(list1) + len(list2)         # 1 + 1 + 1 = 3
    unique_combined_size = len(set(list1 + list2))  # n + n + 1 = 2n + 1
    return combined_size - unique_combined_size     # 1 + 1 = 2
                                                    # ----
                                                    # 3 + 2n + 1 + 2 = 2n + 6 = O(n)


def measure_time() -> None:
    """
    Measure the time it takes for find_common and find_common_efficient
    to run on lists of sizes 10, 100, 1000, 10000, 20000.
    """
    sizes = [10, 100, 1000, 10000, 20000]
    find_common_times = []
    find_common_efficient_times = []

    for size in sizes:
        list1, list2 = generate_lists(size)

        t0 = time.time()
        find_common(list1, list2)
        find_common_times.append(time.time() - t0)

        t0 = time.time()
        find_common_efficient(list1, list2)
        find_common_efficient_times.append(time.time() - t0)

    print("List size\tfind_common time (s)\tfind_common_efficient time(s)")
    print("-" * 80)
    for i in range(len(sizes)):
        print(f"{sizes[i]}\t\t{find_common_times[i]:.3f}\t\t\t{find_common_efficient_times[i]:.3f}")


if __name__ == "__main__":
    measure_time()
