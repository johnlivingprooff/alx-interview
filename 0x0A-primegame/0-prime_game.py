#!/usr/bin/python3
"""Prime Game"""


def sieve(max_n):
    """Returns a list of booleans indicating
    if a number is prime up to max_n."""
    if max_n <= 0:
        return []
    isPrime = [True for _ in range(max_n + 1)]
    isPrime[0], isPrime[1] = False, False
    i = 2
    while i * i <= max_n:
        if isPrime[i]:
            for j in range(i * i, max_n + 1, i):
                isPrime[j] = False
        i += 1
    return isPrime


def isWinner(x, nums):
    """Determines the winner of the game"""

    if x < 1 or nums is None:
        return None

    max_num = max(nums)
    prime_list = sieve(max_num)
    nums_len = len(nums)

    Maria, Ben = 0, 0

    for eachRound in range(x):
        n = nums[eachRound % nums_len]
        prime_count = [p for p in range(2, n + 1) if prime_list[p]]

        if len(prime_count) % 2 == 1:
            Maria += 1
        else:
            Ben += 1

    if Maria == Ben:
        return None
    return "Maria" if Maria > Ben else "Ben"
