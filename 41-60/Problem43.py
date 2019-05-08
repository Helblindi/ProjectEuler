"""
The number, 1406357289, is a 0 to 9 pandigital number because
it is made up of each of the digits 0 to 9 in some order, but
it also has a rather interesting sub-string divisibility
property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In
this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import time
from Misc.useful import permutation
from Misc.useful import check_substring_divisibility


# driver function for our program
def main():
    """
    Creates a list of the 0-9 digit pandigitals and then
    implements the check_substring_divisibility function
    in Misc.useful.py to check the substrings.
    """
    start_time = time.time()
    qualifying_pandigitals = []
    # Generate all possible 9th pandigital numbers to test
    for p in permutation(list('0123456789')):
        num = str(''.join(p))
        if check_substring_divisibility(num, 1, 4, 2) and \
                check_substring_divisibility(num, 2, 5, 3) and \
                check_substring_divisibility(num, 3, 6, 5) and \
                check_substring_divisibility(num, 4, 7, 7) and \
                check_substring_divisibility(num, 5, 8, 11) and \
                check_substring_divisibility(num, 6, 9, 13) and \
                check_substring_divisibility(num, 7, 10, 17):
            qualifying_pandigitals.append(int(num))
            print(num)

    # calculate end time and print results
    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum(qualifying_pandigitals), end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
