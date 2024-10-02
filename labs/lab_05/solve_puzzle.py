def solve_puzzle(board: list[int], idx: int = 0, visited: set = None) -> bool:
    """Returns True if a given board is solveable."""
    if visited is None:
        visited = set()

    # Solved if at the last tile of the puzzle.
    if idx == len(board) - 1:
        return True

    # Unsolvable this way if the tile has already been visited before.
    if idx in visited:
        return False

    # Add idx to visited tiles.
    visited.add(idx)

    # Calculate possible idxs to go to.
    idx_cw = (idx + board[idx]) % len(board)
    idx_ccw = (idx - board[idx]) % len(board)

    # Explore both paths.
    return solve_puzzle(board, idx_cw, visited) or solve_puzzle(board, idx_ccw, visited)


if __name__ == "__main__":
    print(solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0]))
    print(solve_puzzle([3, 4, 1, 2, 0]))
