"""
The number, 197, is called a circlar prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import time


# driver function for our program
def main():
    start_time = time.time()

    num_circ_primes = 0

    # loop from 2 to 1,000,000 because 1 is not prime!
    for i in range(2, 1000001):
        if is_circular_prime(i):
            num_circ_primes += 1

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (num_circ_primes, end_time))


# check to see if a given value is a circular prime
def is_circular_prime(num):
    # for speeds sake, don't even proceed to checking other values if the number itself is not prime
    if not is_prime(num):
        return False

    circ_vals = get_circular_values(num)
    for val in circ_vals:
        if not is_prime(val):
            return False

    print(num, ' is a circular prime!')

    return True


# function to return all the circular values from a given number
def get_circular_values(num):
    circ_vals = []
    copy = num
    _len = len(str(num)) - 1

    # what is the syntax for a do-while loop?? -------------------------------
    digit = copy % 10
    copy //= 10
    copy += (digit * 10**_len)
    circ_vals.append(copy)

    while copy != num:
        digit = copy % 10
        copy //= 10
        copy += (digit * 10**_len)
        circ_vals.append(copy)

    return circ_vals


# function to tell us if we have a prime number or not
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
