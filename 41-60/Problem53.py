"""
https://projecteuler.net/problem=53

Math Description.  How many combinatorial combinations are
greater than 1,000,000?
"""

"""
Plan:

"""

import scipy.special
import time


# driver function for our program
def main():
    start_time = time.time()

    count = 0

    for n in range(1, 101):
        for r in range(1, n + 1):
            if scipy.special.binom(n, r) >= 1000000.:
                count += 1

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (count, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
