#!/usr/bin/python3
"""make change into coins"""


def makeChange(coins, total):
    """calculate num of coins in change"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if coin <= total:
            count += total // coin
            total %= coin

    if total != 0:
        return -1

    return count
