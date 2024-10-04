def find_min_coins(
    change: int, coins: list[int], cache: dict[int, int] | None = None
) -> int:
    """Find the minimum number of coins needed to make change."""
    if cache is None:
        cache = {coin: 1 for coin in coins}

    if change in cache:
        return cache[change]

    cache[change] = 1 + min(
        find_min_coins(change - coin, coins, cache) for coin in coins if coin < change
    )
    return cache[change]


if __name__ == "__main__":
    print(find_min_coins(12, [1, 5, 10]))
    print(find_min_coins(34, [1, 5, 10, 25]))
