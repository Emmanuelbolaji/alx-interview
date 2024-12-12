#!/usr/bin/python3
"""
Prime Number Game Module

Implements a game where players remove prime numbers and their multiples
from a set of consecutive integers.
"""


def is_prime(n):
    """
    Determine if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def play_prime_game(n):
    """
    Simulate a single round of the prime number game.

    Args:
        n (int): Upper limit of consecutive integers

    Returns:
        str: Winner of the game ('Maria' or 'Ben')
    """
    available = set(range(1, n + 1))
    current_player = 'Maria'

    while True:
        primes = [num for num in available if is_prime(num)]

    if not primes:
        return 'Ben' if current_player == 'Maria' else 'Maria'

    prime_choice = max(primes)

    to_remove = {num for num in available if num == prime_choice or num % prime_choice == 0}
    available -= to_remove

    current_player = 'Ben' if current_player == 'Maria' else 'Maria'


def isWinner(x, nums):
    """
    Determine the overall winner across multiple game rounds.

    Args:
        x (int): Number of rounds
        nums (list): Upper limits for each round

    Returns:
        str or None: Name of the player with most wins, or None if undetermined
    """
    if not x or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        winner = play_prime_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'

    return None


