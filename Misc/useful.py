"""
This file is where we will collect our functions that we have made to assist in solving the ProjectEuler questions.
"""
from math import sqrt
from itertools import count, islice


# https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True
