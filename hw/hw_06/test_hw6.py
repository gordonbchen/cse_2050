import unittest

from typing import Callable

from hw6 import bubble_sort, selection_sort, insertion_sort, merge


class SortingTestFactory:
    """Factory that generates test cases for sorting algorithms."""

    def setUp(
        self, sorting_alg: Callable[[list[list[int]]], tuple[list[int], int]]
    ) -> None:
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self) -> None:
        """Test that the merge function correctly merges 3 sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0], matrix[1], matrix[2]))

    def is_sorted(self, L) -> bool:
        """Check if a list is sorted."""
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self) -> None:
        """Test sorting an empty list."""
        matrix = [[], [], []]
        sorted_vals, swaps = self.sorting_alg(matrix)
        self.assertEqual(sorted_vals, [])
        self.assertEqual(swaps, 0)

    def test_sorted(self):
        """Test sorting a sorted list."""
        matrix = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ]

        sorted_vals, swaps = self.sorting_alg(matrix)
        self.assertEqual(sorted_vals, [1, 2, 3, 4, 5])
        self.assertEqual(swaps, 0)

    def test_reverse_sorted(self):
        """Test sorting a reversed list."""
        matrix = [
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
        ]

        sorted_vals, swaps = self.sorting_alg(matrix)
        self.assertEqual(sorted_vals, [1, 2, 3, 4, 5])

        # Swap assertion for bubble and insertion.
        self.assertEqual(swaps, 10)

    def test_random(self):
        """Test sorting a random list."""
        matrix = [
            [4, 5, 2, 3, 1],
            [4, 5, 2, 3, 1],
            [4, 5, 2, 3, 1],
        ]

        sorted_vals, swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_vals))

        # Swap assertion for bubble and insertion.
        self.assertEqual(swaps, 8)


class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self) -> None:
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm."""

    def setUp(self) -> None:
        """Set up the bubble sort algorithm for testing."""
        super().setUp(insertion_sort)


class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm."""

    def setUp(self) -> None:
        """Set up the selection sort algorithm for testing."""
        super().setUp(selection_sort)

    def test_reverse_sorted(self):
        """Test sorting a reversed list."""
        matrix = [
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
        ]

        sorted_vals, swaps = self.sorting_alg(matrix)
        self.assertEqual(sorted_vals, [1, 2, 3, 4, 5])

        # Swap assertion for selection sort.
        self.assertEqual(swaps, 2)

    def test_random(self):
        """Test sorting a random list."""
        matrix = [
            [4, 5, 2, 3, 1],
            [4, 5, 2, 3, 1],
            [4, 5, 2, 3, 1],
        ]

        sorted_vals, swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_vals))

        # Swap assertion for bubble and insertion.
        self.assertEqual(swaps, 4)


if __name__ == "__main__":
    unittest.main()
