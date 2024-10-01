import unittest

from solve_puzzle import solve_puzzle


class TestSolvePuzzle(unittest.TestCase):
    def testClockwise(self):
        """Tests a board solveable using only CW moves."""
        board = [3, 6, 4, 1, 3, 4, 2, 0]
        self.assertTrue(solve_puzzle(board))

    def testCounterClockwise(self):
        """Tests a board solveable using only CCW moves."""
        board = [4, 2, 5, 5, 5]
        self.assertTrue(solve_puzzle(board))

    def testMixed(self):
        """Tests a board solveable using only a combination of CW and CCW moves."""
        board = [4, 3, 5, 5, 5]
        self.assertTrue(solve_puzzle(board))

    def testUnsolveable(self):
        """Tests an unsolveable board."""
        board = [3, 4, 1, 2, 0]
        self.assertFalse(solve_puzzle(board))


if __name__ == "__main__":
    unittest.main()
