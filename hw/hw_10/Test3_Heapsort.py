import unittest
import random

from heapsort import heapsort


class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""

    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def assertSorts(self, alg, arr):
        """Asserts that alg(L) sorts L"""
        L_sorted = sorted(arr[:])
        alg(arr)
        self.assertEqual(arr, L_sorted)

    def test_empty(self):
        """Test sorting an empty list."""
        arr = []
        self.assertSorts(self.sorting_alg, arr)

    def test_sorted(self):
        """Test sorting a sorted list."""
        arr = [i for i in range(10000)]
        self.assertSorts(self.sorting_alg, arr)

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        arr = [i for i in range(10000, -1, -1)]
        self.assertSorts(self.sorting_alg, arr)

    def test_random(self):
        """Test sorting a randomly shuffled list."""
        n = 10000
        arr = [random.randint(0, n) for _ in range(n)]
        self.assertSorts(self.sorting_alg, arr)


class TestHeap(SortingTestFactory, unittest.TestCase):
    """Test class for the heapsort algorithm."""

    def setUp(self):
        """Set up the heapsort algorithm for testing."""
        super().setUp(heapsort)


if __name__ == "__main__":
    unittest.main()
