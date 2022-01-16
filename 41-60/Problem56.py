"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""

"""
Plan:

"""

import time
import sys
import math
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import get_list_of_primes, is_prime


# driver function for our program
def main():
    start_time = time.time()
    max_sum = 0
    num = 0

    for a in range(1, 100):
        for b in range(1, 100):
            sum = 0
            num = pow(a,b)

            while num != 0:
                sum += (num % 10)
                num /= 10

            if sum > max_sum:
                max_sum = sum

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (max_sum, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
