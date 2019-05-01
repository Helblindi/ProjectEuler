"""
This file is where we will collect our functions that we have made to assist in solving the ProjectEuler questions.
"""


def is_prime(n):
    """ Function to test primality of n. """
    if n == 0 or n == 1:  # n = 0 and n = 1 are not primes
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

