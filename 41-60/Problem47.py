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


# driver function for our program
def main():
    """
    """
    start_time = time.time()
    num = 0

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (num, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
