"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import time
import sys
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import get_digits, get_list_of_primes


# driver function for our program
def main():
    """
    """
    start_time = time.time()

    primes = get_list_of_primes(1000, 9999)
    for i in primes:
        for num in range(1, int((9999 - i) / 2) + 1):
            j = i + num
            k = j + num

            if j in primes and k in primes:
                i_digits = set(get_digits(i))
                j_digits = set(get_digits(j))
                k_digits = set(get_digits(k))

                if i_digits == j_digits and j_digits == k_digits:
                    # We've found a sequence of digits that satisfies the
                    # desired properties
                    print(i, j, k)

    end_time = time.time() - start_time
    # print("Found %s in %2f seconds." % (sum, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
