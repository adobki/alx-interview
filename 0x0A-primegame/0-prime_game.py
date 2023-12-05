#!/usr/bin/python3
"""Prime Game algorithm"""


def getPrimes(n: int) -> tuple:
    """
    Helper function to isolate the prime numbers in a range of integers
    :param n: Upper bound of range of integers
    :return: List of prime numbers and list of the composite integers.
    """

    numbers = list(range(2, n + 1))
    primes, composites = [], []
    if n < 4:
        return numbers, composites

    for num in numbers:
        if num < 4:
            primes.append(num)
        else:
            for x in range(2, num + 1):
                if not num % x:
                    composites.append(num) if x != num else primes.append(num)
                    break

    return primes, composites


def isWinner(x: int, nums: list) -> str:
    """
    Uses the provided game stats `x` and `nums` to calculate the winner of
    a Prime Game played between two players, Maria and Ben.

    A player loses a round when they have no turns left, so for each round,
        - **Player 2/P2/Ben** wins if number of turns == 0 or even number,
        - **Player 1/P1/Maria** wins if number of turns == odd number.

    The player with the highest number of rounds wins at the end of the
    game, or it ends a draw if their scores are tied.

    :param x: Number of rounds played
    :param nums: List of n's, where `n` is max int per round
    :return: Name of player that wins the most rounds if any, `None` if draw
    """
    if not isinstance(x, int) or x <= 0 \
            or not nums or not isinstance(nums, list):
        return None

    winner = 0
    for n in nums[:x]:
        if not isinstance(n, int):
            continue
        primes, composites = getPrimes(n)
        # winner += 1 if P1 has more turns, winner -=1 if P2 has more turns
        winner += -1 if not len(primes) else -1 if not len(primes) % 2 else 1

    # P1 wins if `winner` is positive, P2 if negative, or draw otherwise
    return 'Maria' if winner > 0 else 'Ben' if winner < 0 else None


if __name__ == '__main__':
    """Tests the code in this module"""
    nums = [4, 5, 1]
    print(isWinner(3, nums))
    nums = [2, 5, 1, 4, 3]
    print(isWinner(5, nums))

    nums = [2, 10, 5, 3]
    print(isWinner(2, nums))
    nums = [2, 10, 5, 3]
    print(isWinner(3, nums))
