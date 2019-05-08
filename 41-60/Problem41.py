"""
We shall say that an n-digit number is pandigital if it makes
use of all the digits 1 to n exactly once. For example, 2143
is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import time
from Misc.useful import is_prime
from Misc.useful import permutation


# driver function for our program
def main():
    """
    Generates all possible pandigital numbers and test to see first
    if they are prime.  If they are prime then it checks if it is
    bigger than the max num.
    """
    start_time = time.time()
    max_num = 0

    # Generate all possible 7th pandigital numbers to test
    data1 = list('1234567')
    for p in permutation(data1):
        # p is in form ['1', '2', '3', '4', '5', '6', '7'], must be concatenated
        num = int(''.join(p))
        # check value
        if is_prime(num) and num > max_num:
            max_num = num

    # Generate all possible 8th pandigital numbers to test
    data2 = list('12345678')
    for p in permutation(data2):
        num = int(''.join(p))
        if is_prime(num) and num > max_num:
            max_num = num

    # Generate all possible 9th pandigital numbers to test
    data3 = list('123456789')
    for p in permutation(data3):
        num = int(''.join(p))
        if is_prime(num) and num > max_num:
            max_num = num

    # calculate end time and print results
    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (max_num, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
