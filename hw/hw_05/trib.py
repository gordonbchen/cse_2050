def trib(k: int, cache: dict[int, int] | None = None) -> int:
    """Return the kth tribonacci number."""
    if cache is None:
        cache = {1: 0, 2: 0, 3: 1}

    if k in cache:
        return cache[k]

    trib_val = sum(trib(k - i, cache) for i in range(1, 4))
    cache[k] = trib_val

    return trib_val


if __name__ == "__main__":
    for i in range(1, 101):
        print(i, trib(i))
