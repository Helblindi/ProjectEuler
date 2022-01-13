"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

"""
Plan:
    0. Set max prime parameter
    1. Iterate over list of primes:
        - Iteratively add further indices checking for a prime each time.
        - If prime, save number of consecutive primes and max prime.

"""


import time
import sys
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import get_list_of_primes, is_prime


# driver function for our program
def main():
    start_time = time.time()

    max_prime = 2
    max_num_indices = 0
    list_of_primes = get_list_of_primes(2, 1000000)
    for i in range(0, len(list_of_primes)):
        prime_sum = list_of_primes[i]
        j = i + 1
        while prime_sum < 1000000:
            if j < len(list_of_primes):
                prime_sum += list_of_primes[j]
                num_indices = j - i + 1

                if is_prime(prime_sum) and num_indices > max_num_indices:
                    max_num_indices = num_indices
                    max_prime = prime_sum

                j += 1
            else:
                prime_sum = 1000001


    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (max_prime, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
