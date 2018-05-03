"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive
values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n=0.
"""
import time
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


def get_primes(number):
    """
    Get a list of prime values under a passed in number.
    :param number: value that the function will find primes under
    :return: list of all primes who's value is less than the given number
    """
    # First find non-primes since that is easier
    non_primes = set(j for i in range(2, 8) for j in range(i * 2, number, i))

    # Now find all numbers that are not in the first generated list
    primes = [x for x in range(2, number) if x not in non_primes]

    # return that list of primes
    return primes


def main():
    start_time = time.time()

    best_a = 0
    best_b = 0
    best_primes = 1

    for a in range(-1000, 1001):
        for b in get_primes(1000):
            n = 0
            primes = 0
            # loop through values of n until the equation is not prime
            while is_prime(n**2 + a*n + b):
                primes += 1
                n += 1

            if primes > best_primes:
                best_primes = primes
                best_a = a
                best_b = b
                print('best primes changed to: ', best_primes)

            # print('Found %s primes for a = %s and b = %s' % (primes, a, b))

    solution = best_a * best_b
    end_time = time.time() - start_time

    print("found %s in %2f seconds." % (solution, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
