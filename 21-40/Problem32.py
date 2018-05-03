"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it
once in your sum.
"""
import time


def main():
    start_time = time.time()

    end_time = time.time() - start_time
    print("found %s in %2f seconds." % (0, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
