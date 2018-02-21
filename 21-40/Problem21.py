"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5,
10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so
d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time


def get_div_sum(number):
    _sum = 0
    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            _sum += i

    return _sum


def main():
    start = time.time()
    overall_sum = 0
    for it in range(1, 10000):
        temp = get_div_sum(it)
        if it == get_div_sum(temp):
            if temp <= 10000:
                if it != temp:
                    # we have an amicable pair, but only add the first
                    # because the for loop will add temp later
                    overall_sum += it

    elapsed = (time.time() - start)
    print("The sum is %d and it was found in %2f seconds." % (overall_sum, elapsed))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()

