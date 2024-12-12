#!/usr/bin/python3
"""Prime Number Game Module."""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def play_round(n):
    """
    Play a single round of the prime game.

    Args:
        n (int): Upper limit of numbers

    Returns:
        str: Winner of the round
    """
    nums = list(range(1, n + 1))
    player = 'Maria'

    while True:
        primes = [x for x in nums if is_prime(x)]

        if not primes:
            return 'Ben' if player == 'Maria' else 'Maria'

        prime = max(primes)

        nums = [x for x in nums if x % prime != 0]

        player = 'Ben' if player == 'Maria' else 'Maria'


def isWinner(x, nums):
    """
    Determine the overall winner across multiple game rounds.

    Args:
        x (int): Number of rounds
        nums (list): Upper limits for each round

    Returns:
        str or None: Name of the player with most wins
    """
    if not x or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    if ben_wins > maria_wins:
        return 'Ben'

    return None
