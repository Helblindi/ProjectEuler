"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
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

    sum = 0
    for n in range(1, 1001):
        sum = (sum + pow(n, n, 10000000000)) % 10000000000

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
