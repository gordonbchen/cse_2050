import time


def time_function(func, args, n_trials: int = 10) -> float:
    """Return the number of seconds it takes to run func with args."""
    min_time = float("inf")

    for i in range(n_trials):
        t0 = time.time()
        func(args)
        min_time = min(min_time, time.time() - t0)

    return min_time


def time_function_flexible(func, args: tuple, n_trials: int = 10) -> float:
    """Return the number of seconds it takes to run func with a tuple of args."""
    min_time = float("inf")

    for i in range(n_trials):
        t0 = time.time()
        func(*args)
        min_time = min(min_time, time.time() - t0)

    return min_time


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)]  # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
