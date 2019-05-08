"""
We shall say that an n-digit number is pandigital if it makes
use of all the digits 1 to n exactly once. For example, 2143
is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import time
from Misc.useful import is_pandigital
from Misc.useful import is_prime
from Misc.useful import sieve


# driver function for our program
def main():
    """
    """
    start_time = time.time()
    num = 0
    # for i in range(1234567, 987654322):
    #     if is_prime(i) and is_pandigital(i):
    #         num = i

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (num, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
