"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest
prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

"""
Plan:
    1. Loop over list_of_primes
    2. Generate possible wildcards
    3. Loop over possible wildcards and check primes in each wildcard.
"""

import time
import sys
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import get_list_of_primes, is_prime


# driver function for our program
def main():
    start_time = time.time()

    list_of_primes = get_list_of_primes(11, 1000000)
    max_family_number = 0
    for prime in list_of_primes:
        wildcard_strings = create_wildcard_strings(prime)
        for wildcard in wildcard_strings:
            family_number = compute_family_number(wildcard)
            if family_number > max_family_number:
                print('Changing max_family_number: ', wildcard)
                print('Family number: ', family_number)

                max_family_number = family_number


    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (max_family_number, end_time))


def create_wildcard_strings(num):
    """
    This function generates all the possible wildcard possibilities for a single
    prime.  The steps to do so are as follows:
        1. Turn prime into a string
        2. Create a set of distinct digits
        3. String replace each digit with star to create wildcard.

    The wildcard strings for the number 15187 would be:
    ['1518*', '151*7', '1*187', '*5*87']
    """
    s_num = str(num)
    num_digits = len(s_num)
    _digits = set(s_num)
    wildcard_strings = []

    for c in _digits:
        temp_num = s_num.replace(c, '*')
        wildcard_strings.append(temp_num)

    return wildcard_strings


def compute_family_number(wildcard):
    """
    This function computes the number of primes belong to this specific wildcard
    family.  For example, given the wildcard '*3' the following are prime:
    13, 23, 43, 53, 73, and 83.
    """
    num_primes = 0
    if wildcard[0] == '*':
        for i in range(1, 10):
            num = int(wildcard.replace('*', str(i)))
            if is_prime(num):
                num_primes += 1
    else:
        for i in range(0, 10):
            num = int(wildcard.replace('*', str(i)))
            if is_prime(num):
                num_primes += 1

    return num_primes


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
