def fib_default(k, solved=None):
    if solved is None:
        solved = {0: 0, 1: 1}

    if k in solved:
        return solved[k]

    solved[k] = fib_default(k - 1, solved) + fib_default(k - 2, solved)

    return solved[k]


def fib_helper(k):
    solved = {0: 0, 1: 1}
    return _fib_helper(k, solved)


def _fib_helper(k, solved):
    if k in solved:
        return solved[k]

    solved[k] = _fib_helper(k - 1, solved) + _fib_helper(k - 2, solved)

    return solved[k]


if __name__ == "__main__":
    sols = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}

    for key in sols:
        assert fib_default(key) == sols[key]
        assert fib_helper(key) == sols[key]
