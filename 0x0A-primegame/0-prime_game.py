#!/usr/bin/python3
"""Prime Number Game Module."""


def isWinner(x, nums):
    """
    Determine the overall winner across multiple game rounds.

    Args:
        x (int): Number of rounds
        nums (list): Upper limits for each round

    Returns:
        str or None: Name of the player with most wins
    """
    def generate_primes(n):
        """Generate primes up to n using Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False

        return [p for p in range(2, n + 1) if sieve[p]]

    def play_round(n):
        """
        Play a single round of the prime game.

        Returns:
            str: Winner of the round
        """
        primes = generate_primes(n)
        return 'Maria' if len(primes) % 2 == 1 else 'Ben'

    if not x or not nums:
        return None

    maria_wins = sum(1 for n in nums[:x] if play_round(n) == 'Maria')
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return 'Maria'
    if ben_wins > maria_wins:
        return 'Ben'

    return None
