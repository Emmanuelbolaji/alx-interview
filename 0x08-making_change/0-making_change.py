#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a total amount

    Args:
        coins (list): List of coin denominationscoins
        total (int): Target total amount

    Returns:
        int: Fewest number of coins needed to meet total
            Returns -1 if total cannot be met
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
