#!/usr/bin/python3
"""Make Change algorithm"""


def makeChange(coins: list, total: int) -> int:
    """
    Returns minimum coins needed to make change of given amount
    :param coins: list of available coins (must be an int > 0)
    :param total: amount to be converted to change
    :return: change on success, 0 if total <= 0, -1 otherwise
    """
    if not isinstance(total, int) or total <= 0:
        return 0
    if not isinstance(coins, list) or not coins:
        return -1
    change, coins = 0, sorted(coins, reverse=True)
    for coin in coins:
        if total >= coin:
            change += total // coin
            total %= coin
        if total < 1:
            break
    return change if not total else -1


if __name__ == '__main__':
    """Tests the code in this module"""
    coins = [50, 25, 10, 5, 2, 1]
    print(makeChange(coins, 77))
    print(makeChange(coins, 76))
    print(makeChange(coins, -22))
    print(makeChange(coins, 2.2))

    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
