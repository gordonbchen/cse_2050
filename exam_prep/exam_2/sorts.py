import unittest

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


def quick_sort_random_index(vals: list[int], left: int = 0, right: int = None) -> None:
    """Quick sort."""
    if right is None:
        right = len(vals)

    if left >= right:
        return

    pivot = randint(left, right - 1)
    vals[pivot], vals[right - 1] = vals[right - 1], vals[pivot]

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

    quick_sort_random_index(vals, left, pivot)
    quick_sort_random_index(vals, pivot + 1, right)


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


class SortTestFactory:
    def test_empty(self) -> None:
        vals = []
        self.check_sort_func(vals)

    def test_single_element(self) -> None:
        vals = [0]
        self.check_sort_func(vals)

    def test_two_elements(self) -> None:
        vals = [1, 0]
        self.check_sort_func(vals)

    def test_sorted(self) -> None:
        vals = list(range(900))
        self.check_sort_func(vals)

    def test_reverse_sorted(self) -> None:
        vals = list(range(900, 0, -1))
        self.check_sort_func(vals)

    def test_random(self) -> None:
        for i in [499, 500, 1_000, 1_001]:
            vals = list(randint(-1_000, 1_000) for j in range(i))
            self.check_sort_func(vals)

    def check_sort_func(self, vals: list[int]) -> None:
        """Check that the sort func works on vals."""
        true_sorted = sorted(vals)
        self.sort_func(vals)
        self.assertEqual(true_sorted, vals)


class InsertionSortTests(SortTestFactory, unittest.TestCase):
    def setUp(self) -> None:
        self.sort_func = insertion_sort


class BubbleSortTests(SortTestFactory, unittest.TestCase):
    def setUp(self) -> None:
        self.sort_func = bubble_sort


class SelectionSortTests(SortTestFactory, unittest.TestCase):
    def setUp(self) -> None:
        self.sort_func = selection_sort


class QuickSortTests(SortTestFactory, unittest.TestCase):
    def setUp(self) -> None:
        self.sort_func = quick_sort


class QuickSortRandomIndexTests(SortTestFactory, unittest.TestCase):
    def setUp(self) -> None:
        self.sort_func = quick_sort_random_index


class MergeSortTests(SortTestFactory, unittest.TestCase):
    def setUp(self) -> None:
        self.sort_func = merge_sort


if __name__ == "__main__":
    unittest.main()
