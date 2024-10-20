def fewest_coins(amount: int, coins: list[int]) -> int:
    """Return the fewest number of coins necessary to make the amount."""
    solved = {coin: 1 for coin in coins}
    return _fewest_coins(amount, coins, solved)


def _fewest_coins(amount: int, coins: list[int], solved: dict[int, int]) -> int:
    """Return the fewest number of coins necessary to make the amount."""
    if amount in solved:
        return solved[amount]

    min_coins = float("inf")
    for coin in coins:
        if amount < coin:
            continue

        min_coins = min(min_coins, 1 + _fewest_coins(amount - coin, coins, solved))

    solved[amount] = min_coins
    return min_coins


if __name__ == "__main__":
    print(fewest_coins(23, [1, 5, 10]))
    print(fewest_coins(12, [1, 5, 10]))
    print(fewest_coins(34, [1, 5, 10, 25]))
