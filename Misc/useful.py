"""
This file is where we will collect our functions that we have made to assist in solving the ProjectEuler questions.
"""
import string
from math import sqrt
from itertools import count, islice
from functools import reduce
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


def get_alphabetic_value(word):
    value = 0
    for i in word:
        # https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
        value += string.ascii_uppercase.index(i) + 1

    return value


def is_palindrome(n):
    """
    Tests if the given number n is a palindrome.

    First used in Problem 36.
    """
    return n == reverse_int(n)


def is_bin_palindrome(n):
    """
    Tests if the given binary number n is a palindrome.

    First used in Problem 36.
    """
    bin_n = dec_to_bin(n)
    return bin_n == reverse_int(bin_n)


def dec_to_bin(n):
    """
    Converts decimal to binary.

    First used in Problem 36.
    """
    return int(bin(n)[2:])


def reverse_int(n):
    """
    Reverses the values in an integer. 1234 = 4321.

    First used in Problem 36.
    """
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = n // 10
    return reverse


def check_substring_divisibility(num, start, end, modulus):
    """
    Function checks if a substring of a given number is divisible by the modulus value.
    First implemented in Problem 43.
    :param num: string or int
    :param start: substring initial index
    :param end: substring end index
    :param modulus: value to be modded
    :return: True or false if the substring value mod the modulus is 0
    """
    # First convert num to a string if it isn't
    # https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
    if not isinstance(num, str):
        num = str(num)

    # Now run the modulus check
    if int(num[start:end]) % modulus == 0:
        return True
    else:
        return False


def is_pentagonal(num):
    """
    Iteratively determines if the passed in parameter is a pentagonal number.
    :param num: number to be tested
    :return: if num is pentagonal
    """
    i = 1
    while True:
        m = i*(3*i - 1) / 2
        if m >= num:
            break
        i += 1

    return m == num


def get_factors(n):
    """
    Returns the factors of a given number.
    First used in Problem 47.

    :param n: number to find factors for.
    :return: set of factors of n
    """
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def get_num_distinct_prime_factors(n):
    """
    Returns the number of distinct prime factors of a given number.  Utilizes
    the get_factors function and the is_prime function.
    first used in Problem 47.

    :param n: number to find the distinct prime factors for.
    :return: length of the set of prime factors.
    """
    factors = get_factors(n)
    distinct_prime_factors = [num for num in factors if is_prime(num)]
    return len(distinct_prime_factors)


def get_list_of_primes(start, end):
    """
    Returns a list of primes between start and end.
    First used in Problem 49.

    :param start: Starting value for list.
    :param end: Ending value for list.
    :return: List of primes.

    If prime is in list, start <= prime <= end.
    """
    return [num for num in range(start, end + 1) if is_prime(num)]
