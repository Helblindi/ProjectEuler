"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (desired_totalp).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time


def main():
    start_time = time.time()

    desired_total = 200
    num_ways = 1

    # removed the 200p coins

    # number of 100p coins
    for a in range(3):
        # number of 50p coins
        # if we use a of the 100p coins, then the total amount (b) of 50p coins that we can use reduces dependant on a
        for b in range(int(1 + (desired_total - 100 * a) / 50)):
            # number of 20p coins
            for c in range(int(1 + (desired_total - 100 * a - 50 * b) / 20)):
                # number of 10p coins
                for d in range(int(1 + (desired_total - 100 * a - 50 * b - 20 * c) / 10)):
                    # number of 5p coins
                    for e in range(int(1 + (desired_total - 100 * a - 50 * b - 20 * c - 10 * d) / 5)):
                        # number of 2p coins
                        for f in range(int(1 + (desired_total - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e) / 2)):
                            num_ways += 1

    end_time = time.time() - start_time
    print("found %s in %2f seconds." % (num_ways, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
