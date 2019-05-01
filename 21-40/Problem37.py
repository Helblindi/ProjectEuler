"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time
from Misc.useful import is_prime


# driver function for our program
def main():
    """
    Driver function for our program.  This program is designed to sum the numbers
    between 1 and 1,000,000 that have the property that both the number and the
    binary representation of said number are palindroms.
    """
    start_time = time.time()
    total_numbers = 0

    # loop from 1 to 1,000,000 because 1 is not prime!
    for num in range(11, 1000001):
        break

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
