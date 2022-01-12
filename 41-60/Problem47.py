"""
The first two consecutive numbers to have two distinct
prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three
distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four
distinct prime factors each. What is the first of these
numbers?
"""

import time
import sys
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import get_num_distinct_prime_factors


# driver function for our program
def main():
    """
    """
    start_time = time.time()
    count = 0
    num = 2
    first = 0

    while count < 4:
        n_prime_factors = get_num_distinct_prime_factors(num)
        if n_prime_factors == 4:
            count += 1
        else:
            count = 0

        if count == 1:
            first = num

        num += 1
        if num % 100000 == 0:
            print("On num: ", num)

        if num == 1000000:
            break

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (first, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
    # print(get_num_distinct_prime_factors(24))
