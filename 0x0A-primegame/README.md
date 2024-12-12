Prime Number Game
Overview
A competitive game where players strategically remove prime numbers and their multiples from a set of consecutive integers. The game challenges players to make optimal moves based on prime number selection.
Game Rules

Players take turns selecting prime numbers
The selected prime and all its multiples are removed from the game set
The player unable to make a move loses the round
Optimal strategy is to choose the largest available prime

Implementation Details

Written in Python 3
No external package dependencies
Supports multiple game rounds with different integer ranges

Functions

is_prime(n): Checks primality of a number
play_prime_game(n): Simulates a single game round
isWinner(x, nums): Determines the overall winner across multiple rounds

Usage Example
pythonCopyx = 3
nums = [4, 5, 1]
winner = isWinner(x, nums)
print(winner)  # Outputs: 'Ben'
Constraints

Maximum rounds (x): 10,000
Maximum range (n): 10,000

Author
Osundiran Omobolaji
