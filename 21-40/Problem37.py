"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time
import numpy as np
from Misc.useful import is_prime


def test_left_to_right(num):
    if num == 0:
        return True

    if is_prime(num):
        return test_left_to_right(num % (10 ** (len(str(num)) - 1)))

    return False


def test_right_to_left(num):
    if num == 0:
        return True
    elif is_prime(num):
        return test_right_to_left(num // 10)

    return False


# driver function for our program
def main():
    """
    Driver function for our program.  This program is designed to sum the numbers
    between 1 and 1,000,000 that have the given property as you truncate from left
    to right, and right the left, the number remains prime.
    """
    start_time = time.time()
    numbers = np.array([])

    # loop from 11 to 1,000,000
    for num in range(11, 1000001):
        if test_left_to_right(num) and test_right_to_left(num):
            numbers = np.append(numbers, num)

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (np.sum(numbers), end_time))
    print(numbers)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
