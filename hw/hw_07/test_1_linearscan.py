import unittest
import random

from magicsort import MagicCase
from magicsort import INVERSION_BOUND
from magicsort import linear_scan

random.seed(658)  # Fixing the random seed to guarntee behvaior on random tests


class TestLinearScan(unittest.TestCase):
    def test_empty_list_sorted(self):
        """Tests linear_scan() on an empty list"""
        L = []
        expected_output = MagicCase.SORTED
        actual_output = linear_scan(L)
        self.assertEqual(actual_output, expected_output)

    def test_sorted(self):
        """Tests linear_scan() on a sorted list"""
        for _ in range(10):
            L = list(range(random.randint(50, 100)))
            expected_output = MagicCase.SORTED
            actual_output = linear_scan(L)
            self.assertEqual(actual_output, expected_output)

    def test_constant_num_inversions(self):
        """Tests linear_scan() on a list with fewer than INVERSION_BOUND inversions."""
        IB = INVERSION_BOUND
        for _ in range(10):
            L = list(range(100))
            rand_idx = random.randrange(0, len(L) - IB)
            L = L[:rand_idx] + list(reversed(range(IB))) + L[rand_idx:]
            expected_output = MagicCase.CONSTANT_INVERSIONS
            actual_output = linear_scan(L)
            self.assertEqual(actual_output, expected_output)

    def test_reversed_small(self):
        """Tests linear_scan() on reverse-sorted list"""
        L = list(reversed(range(10)))
        expected_output = MagicCase.REVERSE_SORTED
        actual_output = linear_scan(L)
        self.assertEqual(actual_output, expected_output)

    def test_reversed_large_random(self):
        """Tests linear_scan() on a large, random reverse-sorted list"""
        for _ in range(10):
            L = list(reversed(range(random.randint(50, 100))))
            expected_output = MagicCase.REVERSE_SORTED
            actual_output = linear_scan(L)
            self.assertEqual(actual_output, expected_output)

    def test_general_case(self):
        """Tests linear_scan() on a sorted list"""
        NUM_INV = INVERSION_BOUND + 2
        for _ in range(10):
            L = list(range(100))
            rand_idx = random.randrange(0, len(L) - NUM_INV)
            L = L[:rand_idx] + list(reversed(range(NUM_INV))) + L[rand_idx:]
            # case 0: not sorted/reverse-sorted and has too many inversions
            expected_output = MagicCase.GENERAL
            actual_output = linear_scan(L)
            self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
