def fib(n: int) -> int:
    cache = {0: 1, 1: 1}
    return _fib(n, cache)


def _fib(n: int, cache: dict[int, int]) -> int:
    if n not in cache:
        cache[n] = _fib(n - 1, cache) + _fib(n - 2, cache)
    return cache[n]


if __name__ == "__main__":
    for i in range(100):
        print(i, fib(i))
