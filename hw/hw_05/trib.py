def trib(k: int) -> int:
    """Return the kth tribonacci number."""
    return _trib(k, cache={1: 0, 2: 0, 3: 1})


def _trib(k: int, cache: dict[int, int]) -> int:
    """Return the kth tribonacci number."""
    if k in cache:
        return cache[k]

    cache[k] = sum(_trib(k - i, cache) for i in range(1, 4))
    return cache[k]


if __name__ == "__main__":
    for i in range(1, 101):
        print(i, trib(i))
