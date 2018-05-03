"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""
import time


def main():
    start_time = time.time()
    num = longest = 1
    for n in range(3, 1000, 2):
        # we know that all even numbers will not result in a repeated decimal
        if n % 5 == 0:
            # go to the next value in the loop
            continue

        p = 1
        while (10 ** p) % n != 1:
            p += 1
    
        if p > longest:
            num, longest = n, p

    end_time = time.time() - start_time

    print("found %s in %2f seconds." % (num, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
