"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import time


def main():
    start_time = time.time()
    # For this problem, we do not need to create 1001 x 1001 spiral to solve this.  All that we must do is
    # recognize the pattern for the values in the upper left, upper right, bottom left, and bottom right of
    # our layers
    # Where n is the layer we have:
    #   - Upper left: n^2 - n +1
    #   - Upper right: n^2
    #   - Bottom left: n^2 - 2n + 2
    #   - Bottom right: n^2 - 3n + 3
    # Thus the sum of these values is 4n^2 - 6n + 6
    # Now we must iterate from 3 to 1001 by 2
    # Total will start at 1 for the 1x1 layer

    total = 1

    # iterate from 3 up to but not including 1002, using a step size 2
    for i in range(3, 1002, 2):
        total += 4 * (i**2) - 6 * i + 6

    end_time = time.time() - start_time
    print("found %s in %2f seconds." % (total, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
