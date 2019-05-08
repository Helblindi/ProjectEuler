"""
This file is where we will collect our functions that we have made to assist in solving the ProjectEuler questions.
"""
from math import sqrt
from itertools import count, islice
import numpy as np


# https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


# numpy implementation of the sieve of eratosthenes
def sieve(n):
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i*i::i] = False
    return np.flatnonzero(flags)


# Helper function for the is_pandigital function
def get_digits(num):
    num_array = np.array([])

    while num != 0:
        digit = num % 10
        num //= int(10)
        num_array = np.append(num_array, int(float(digit)))

    return np.flip(num_array)


# Checks if a given number is pandigital or not
def is_pandigital(num):
    num_array = get_digits(num)
    if (len(set(num_array)) == len(num_array) == max(num_array)) and min(num_array) == 1:
        return True
    else:
        return False


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  rem_lst is
        # remaining list
        rem_lst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(rem_lst):
            l.append([m] + p)
    return l
