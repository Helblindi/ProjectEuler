"""
The following iterative sequence is defined for the set of positive integers:

                        n → n/2 (n is even)
                        n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

            13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proven
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time


def get_collatz_chain_length(number):
    length = 1
    while number != 1:
        # case where number is even
        if number % 2 == 0:
            number = number / 2
        # case where number is odd
        else:
            number = 3 * number + 1

        # in either case, we have a new number in the chain
        length += 1

    # all we care about is the length of the chain, so return it
    return length


start = time.time()
max_chain_length = 0
max_chain_number = 0

for i in range(1, 1000000):
    if get_collatz_chain_length(i) > max_chain_length:
        max_chain_length = get_collatz_chain_length(i)
        max_chain_number = i


elapsed = (time.time() - start)

print("The number %s produces the max length of %s returned in %2f seconds." % (max_chain_number, max_chain_length, elapsed))



