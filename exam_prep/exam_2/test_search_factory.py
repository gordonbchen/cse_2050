import unittest

from binary_search import binary_search_iter, binary_search_recr


class TestSearchFactory:
    """A factory for testing searches."""

    def test_empty_list(self):
        """Test searching for an item in an empty list."""
        self.assertEqual(self.search_func([], 0), False)

    def test_single_item_list(self):
        """Test searching for an item in a list wtih 1 item."""
        L = [1]
        self.assertEqual(self.search_func(L, 0), False)
        self.assertEqual(self.search_func(L, 1), True)

    def test_smaller_items(self):
        """Test items smaller than the min in the list."""
        L = [1, 2, 3, 4, 5]
        self.assertEqual(self.search_func(L, 0), False)
        self.assertEqual(self.search_func(L, -1), False)

    def test_larger_items(self):
        """Test items larger than the max in the list."""
        L = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.search_func(L, 7), False)
        self.assertEqual(self.search_func(L, 8), False)

    def test_every_item(self):
        """Test every item in the list."""
        L = [1, 2, 3, 4, 5, 6, 7, 8, 10, 14, 77]
        for i in L:
            self.assertEqual(self.search_func(L, i), True)

    def test_between_items(self):
        """Test between every item in the list."""
        L = [2 * i for i in range(10)]
        for i in range(10):
            self.assertEqual(self.search_func(L, (2 * i) + 1), False)


class TestBinarySearchIter(TestSearchFactory, unittest.TestCase):
    """Tests for binary search (iter)."""

    def setUp(self) -> None:
        self.search_func = binary_search_iter


class TestBinarySearchRecr(TestSearchFactory, unittest.TestCase):
    """Tests for binary search (recr)."""

    def setUp(self) -> None:
        self.search_func = binary_search_recr


if __name__ == "__main__":
    unittest.main()
