import unittest

from process import Process


class TestProcess(unittest.TestCase):
    """Tests for the Process class."""

    def test_init_name(self) -> None:
        """Test initializing pid."""
        p = Process("hi")
        self.assertEqual(p.pid, "hi")
        self.assertEqual(p.cycles, 100)
        self.assertEqual(p.link, None)
        self.assertEqual(p.prev, None)

    def test_init_name_and_cycles(self) -> None:
        """Test initializing pid and cycles."""
        p = Process("hi", 200)
        self.assertEqual(p.pid, "hi")
        self.assertEqual(p.cycles, 200)
        self.assertEqual(p.link, None)
        self.assertEqual(p.prev, None)

    def test_eq(self) -> None:
        """Test process equality operator."""
        p1 = Process("hi", 200)
        p2 = Process("hi", 100)
        p3 = Process("hello", 200)

        self.assertEqual(p1, p2)
        self.assertFalse(p2 == p3)

    def test_repr(self) -> None:
        """Test process str represenation."""
        p = Process("hi", 200)
        self.assertEqual(repr(p), "Process(hi, 200)")


if __name__ == "__main__":
    unittest.main()
