"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import is_palindrome, is_bin_palindrome


# driver function for our program
def main():
    """
    Driver function for our program.  This program is designed to sum the numbers
    between 1 and 1,000,000 that have the property that both the number and the
    binary representation of said number are palindroms.
    """
    start_time = time.time()

    sum = 0

    # loop from 2 to 1,000,000 because 1 is not prime!
    for num in range(1, 1000001):
        if is_palindrome(num) and is_bin_palindrome(num):
            sum += num

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
