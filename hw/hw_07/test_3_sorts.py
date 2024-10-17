import unittest
import random

from magicsort import magic_insertionsort
from magicsort import magic_mergesort
from magicsort import magic_quicksort

random.seed(658)  # Fixing the random seed to guarntee behvaior on random tests


class TestMagicBoundedSort:
    """Test Factory for insertion, magic, and quick-sorts only sorting a sublist"""

    def test_empty_list(self):
        """Tests sorting alg on empty list"""
        L = []
        expected_output = []
        self.sorting_alg(L, 0, len(L))
        self.assertEqual(L, expected_output)

    def test_whole_list(self):
        """Tests sorting alg on full, 5-item list"""
        L = list(reversed(range(5)))
        expected_output = list(range(5))
        self.sorting_alg(L, 0, len(L))
        self.assertEqual(L, expected_output)

    def test_middle_of_list(self):
        """Tests sorting alg on middle of 20 item list"""
        L = list(reversed(range(20)))
        left = 5
        right = 15
        first_half = [19, 18, 17, 16, 15]
        sorted_middle = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        second_half = [4, 3, 2, 1, 0]
        expected_output = first_half + sorted_middle + second_half
        self.sorting_alg(L, left, right)
        self.assertEqual(L, expected_output)

    def test_random_lists_and_bounds(self):
        """Tests sorting alg on various random lists and indices"""
        for _ in range(20):
            N = random.randint(75, 100)
            L = list(reversed(range(N)))
            left = random.randint(0, N // 2)
            right = random.randint(left, N)
            first_half = L[:left]
            sorted_middle = sorted(L[left:right])
            second_half = L[right:]
            expected_output = first_half + sorted_middle + second_half
            self.sorting_alg(L, left, right)
            self.assertEqual(L, expected_output)


class TestMagicInsertionSort(TestMagicBoundedSort, unittest.TestCase):
    def setUp(self):
        self.sorting_alg = magic_insertionsort


#########################################################################
# Uncomment the classes below when you're ready to test each algorithm. #
#########################################################################


class TestMagicMergeSort(TestMagicBoundedSort, unittest.TestCase):
    def setUp(self):
        self.sorting_alg = magic_mergesort


class TestMagicQuickSort(TestMagicBoundedSort, unittest.TestCase):
    def setUp(self):
        self.sorting_alg = magic_quicksort


if __name__ == "__main__":
    unittest.main()
