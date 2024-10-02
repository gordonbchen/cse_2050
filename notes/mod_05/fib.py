def fib(n: int, cache: dict[int, int] | None = None) -> int:
    if cache is None:
        cache = {0: 1, 1: 1}

    if n in cache:
        return cache[n]

    fib_val = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = fib_val

    return fib_val


if __name__ == "__main__":
    for i in range(100):
        print(i, fib(i))
