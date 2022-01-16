"""

"""

"""
Plan:

Diagonal Numbers:
3, 5, 7, 9    [2] (+4)
13, 17, 21 25 [4] (+6)
31, 37, 43, 49 [6] (+8)
57, 65, 73, 81 [8] (+10)
91, 101, 111, 121 [10] (+12)
134,

"""

import time
import sys
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import is_prime


# driver function for our program
def main():
    run_optimized()


def run_optimized():
    start_time = time.time()

    num = 0.
    denom = 1.
    i = 1
    diag = 1
    prime_ratio = 1.

    while prime_ratio > .1:
        sum = int(2 * i)
        for j in range(0,4):
            diag += sum
            if is_prime(diag):
                num += 1

        denom += 4 # Added 4 diagonals
        i += 1     # iterate how we compute the next set of diagonals
        prime_ratio = float(num / denom)
        print('Prime ratio: ', prime_ratio, ' sum: ', sum)

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum + 1, end_time))


def run_unoptimized():
    start_time = time.time()

    diagonal_nums = [1]
    prime_ratio = 1.0
    i = 1
    num = 1
    while prime_ratio > .1:
        sum = 2 * i

        # compute new level
        for j in range(0,4):
            num += sum
            diagonal_nums.append(num)

        # calculate prime ratio
        prime_ratio = compute_prime_ratio(diagonal_nums)

    print('Prime ratio: ', prime_ratio)
    print('sum: ', sum)

    end_time = time.time() - start_time


def compute_prime_ratio(d_nums):
    num_primes = 0
    for num in d_nums:
        if is_prime(num):
            num_primes += 1
    print('num primes: ', num_primes)
    print('len: ', len(d_nums))
    return float(num_primes) / float(len(d_nums))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
