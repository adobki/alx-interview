#!/usr/bin/python3
""" Minimum Operations challenge """
from math import sqrt


def minOperations(n: int) -> int:
    """ Calculates minimum number of operations to get n characters """
    # Perform data validation
    if not isinstance(n, int) or n <= 1:
        return 0
    if n <= 5:
        return n

    # Check if n is a prime number
    root = sqrt(n)
    if not root % 1:
        # Check if square root of n is an even number
        if not root % 2:
            steps = (root / 2 + 2) + n / root
        else:
            steps = root + n / root
    else:
        # Check if n is divisible by 3
        if not n % 3:
            steps = n / 3 + 3
        else:
            # Check if n is an even number
            steps = n / 2 + 2 if not n % 2 else n

    return int(steps)


if __name__ == '__main__':
    n = 3.142
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = -2
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 0
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 1
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 2
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 4
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 49
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 68
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 69
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
    n = 100
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
