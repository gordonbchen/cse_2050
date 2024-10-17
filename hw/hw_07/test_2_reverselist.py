import unittest
import random

from magicsort import reverse_list

random.seed(658)  # Fixing the random seed to guarntee behvaior on random tests


class TestReverseList(unittest.TestCase):
    def test_empty_list(self):
        """Tests reverse_list on an empty list"""
        L = []
        expected_output = []
        reverse_list(L)
        self.assertEqual(L, expected_output)

    def test_odd_length_list(self):
        """Tests reverse_list on a list with an odd number of elements"""
        L = [0, 1, 2, 3, 4, 5, 6]
        expected_output = [6, 5, 4, 3, 2, 1, 0]
        reverse_list(L)
        self.assertEqual(L, expected_output)

    def test_even_length_list(self):
        """Tests reverse_list on a list with an even number of elements"""
        L = [0, 1, 2, 3, 4, 5]
        expected_output = [5, 4, 3, 2, 1, 0]
        reverse_list(L)
        self.assertEqual(L, expected_output)

    def test_random_lists(self):
        """Tests reverse_list on a random list"""
        for _ in range(20):
            L = list(range(random.randint(75, 100)))
            expected_output = [item for item in reversed(L)]
            reverse_list(L)
            self.assertEqual(L, expected_output)


if __name__ == "__main__":
    unittest.main()
