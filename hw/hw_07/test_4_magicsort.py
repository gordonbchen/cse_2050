import unittest
import random

from magicsort import INVERSION_BOUND
from magicsort import magicsort

random.seed(658)  # Fixing the random seed to guarntee behvaior on random tests


class TestMagicSort(unittest.TestCase):
    def test_already_sorted(self):
        """Tests magicsort on a sorted list"""
        L = list(range(100))
        sorted_L = L[:]
        expected_set = set()
        actual_set = magicsort(L)
        self.assertEqual(L, sorted_L)
        self.assertEqual(expected_set, actual_set)

    def test_reverse_only(self):
        """Tests magicsort on a revers sorted list"""
        L = list(reversed(range(100)))
        sorted_L = list(range(100))
        expected_set = {"reverse_list"}
        actual_set = magicsort(L)
        self.assertEqual(L, sorted_L)
        self.assertEqual(expected_set, actual_set)

    def test_insertion_only(self):
        """Tests magicsort on a list with only 1 inversion"""
        L = [0] + list(reversed(range(INVERSION_BOUND - 1))) + [0, 1, 2, 3]
        sorted_L = sorted(L)
        expected_set = {"magic_insertionsort"}
        actual_set = magicsort(L)
        self.assertEqual(L, sorted_L)
        self.assertEqual(expected_set, actual_set)

    def test_quicksort_invokes_mergesort(self):
        """Tests magicsort with bad pivots (should call mergesort)"""
        L = [0] + list(reversed(range(1000)))
        sorted_L = sorted(L)
        expected_set = {"magic_quicksort", "magic_mergesort", "magic_insertionsort"}
        actual_set = magicsort(L)
        self.assertEqual(L, sorted_L)
        self.assertEqual(expected_set, actual_set)

    def test_sorting_random_lists(self):
        """Tests magicsort on various random lists"""
        for _ in range(20):
            L = [random.randint(-500, 500) for i in range(100)]
            sorted_L = sorted(L)
            magicsort(L)
            self.assertEqual(L, sorted_L)


if __name__ == "__main__":
    unittest.main()
