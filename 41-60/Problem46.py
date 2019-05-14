"""
It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as
the sum of a prime and twice a square?
"""
import time
from Misc.useful import is_prime


def test_goldbachs_second_conjecture(num):
    """
    Determines if num can be written as the sum of a prime and twice a square
    :param num: number to be tested
    :return: boolean if it can be written as the sum of a prime and twice a square
    """
    i = 1
    while 2 * i ** 2 < num:
        if is_prime(num - 2 * i ** 2):
            return True
        i += 1
    return False


# driver function for our program
def main():
    """
    This function creates a list of the odd composite numbers under 10,000.
    It then iterates through those numbers and finds the first number that
    fails Goldbachs second conjecture using the helper function above.
    """
    start_time = time.time()
    num = 0
    odd_composite_nums = []
    for i in range(2, 10000):
        if not is_prime(i) and i % 2 == 1:
            odd_composite_nums.append(i)

    for j in odd_composite_nums:
        if not test_goldbachs_second_conjecture(j):
            num = j
            break

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (num, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
