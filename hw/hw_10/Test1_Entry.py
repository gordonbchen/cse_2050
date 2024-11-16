import unittest
import random

from entry import Entry

random.seed(658)  # fix seed so we always fail with the same numbers (makes debugging easier)


class TestEntry(unittest.TestCase):
    def setUp(self):
        """A few entries to test"""
        self.e1 = Entry(item="jake", priority=0)
        self.e2 = Entry(item="rachel", priority=0)
        self.e3 = Entry(item="jake", priority=1)

    def test_eq(self):
        """Tests that equality is defined by priority"""
        self.assertEqual(self.e1, self.e2)
        self.assertNotEqual(self.e1, self.e3)
        self.assertNotEqual(self.e2, self.e3)

    def test_lt(self):
        """Tests that less than only looks at priority"""
        self.assertLess(self.e1, self.e3)
        self.assertGreater(self.e3, self.e1)
        self.assertFalse(self.e1 < self.e2)

    def test_repr(self):
        """Tests string representation"""
        self.assertEqual(repr(self.e1), "Entry(item=jake, priority=0)")
        self.assertEqual(repr(self.e2), "Entry(item=rachel, priority=0)")
        self.assertEqual(repr(self.e3), "Entry(item=jake, priority=1)")


if __name__ == "__main__":
    unittest.main()
