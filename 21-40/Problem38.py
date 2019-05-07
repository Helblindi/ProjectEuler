"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import time
from Misc.useful import is_pandigital


def calc_concatenated_product(num, lis):
    val = ""
    for i in lis:
        val += str(num * i)

    return int(val)


# driver function for our program
def main():
    """
    """
    start_time = time.time()
    max_val = 0
    num_it = 1
    list_it = [1, 2]
    max_val_num = 0
    max_val_list = []

    while True:
        val = calc_concatenated_product(num_it, list_it)

        # check if the number is within range
        if len(str(val)) <= 9:

            # Check if we have a candidate for max_val
            if is_pandigital(val) and val > max_val:
                # if larger, set it to be the new max_val
                max_val = val
                max_val_num = num_it
                max_val_list = list_it

            # in all cases, increment num_it
            num_it += 1

        elif num_it == 1:
            # ending our loop
            break
        else:
            # reset num_it and increment list_it
            num_it = 1
            list_it.append(len(list_it) + 1)

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (max_val, end_time))
    # print("The arguments that give us these values are num =", max_val_num, "and list =", *max_val_list)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
