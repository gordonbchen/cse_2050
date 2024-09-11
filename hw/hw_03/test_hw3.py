import unittest

import hw3


class TestHW3(unittest.TestCase):
    """Tests for HW 3."""

    def test_generate_lists(self) -> None:
        """Test that generate_lists generates unique lists of the correct size."""
        size = 10_000
        for lst in hw3.generate_lists(size):
            self.assertEqual(len(lst), size)
            self.assertEqual(len(lst), len(set(lst)))

    def test_find_common_funcs(self) -> None:
        """Test that find_common and find_common_efficient are correct."""
        lists_common = (
            (([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 3),
            (([1, 2, 3, 4, 5], [11, 12, 13, 14, 15]), 0),
            (([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), 5),
            (([1, 2, 3, 4, 5], [2, 7, 5, 6, 3]), 3),
        )
        for (lists, n_common) in lists_common:
            self.assertEqual(n_common, hw3.find_common(*lists))
            self.assertEqual(n_common, hw3.find_common_efficient(*lists))


if __name__ == "__main__":
    unittest.main()
