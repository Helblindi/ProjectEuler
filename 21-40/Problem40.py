"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
import time
import numpy as np
from Misc.useful import get_digits


# driver function for our program
def main():
    """
    """
    start_time = time.time()
    nums = np.array([])

    # first form long decimal
    for i in range(1, 200000):
        nums = np.append(nums, get_digits(i))

    val = nums[0] * nums[9] * nums[99] * nums[999] * nums[9999] * nums[99999] * nums[999999]

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (val, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
