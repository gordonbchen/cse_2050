import unittest

from trib import trib


class TestTrib(unittest.TestCase):
    """Test tribonacci function."""

    def test_first_ten(self):
        """Tests the first 10 numbers in the tribonacci series"""
        solutions = {
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 2,
            6: 4,
            7: 7,
            8: 13,
            9: 24,
            10: 44,
        }

        for k in solutions:
            self.assertEqual(trib(k), solutions[k])

    def test_100th_trib(self):
        """Test the 100th tribonacci number."""
        self.assertEqual(trib(100), 28992087708416717612934417)


if __name__ == "__main__":
    unittest.main()
