"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""

import time


# driver function for our program
def main():
    start_time = time.time()

    num = 0

    for i in range(1, 1000000):
        if check_multiple(i, 2) and check_multiple(i, 3) and \
           check_multiple(i, 4) and check_multiple(i, 5) and \
           check_multiple(i,6):
           num = i
           break

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (num, end_time))


def check_multiple(num, mult):
    s_num = str(num)

    temp_num = num * mult
    s_temp_num = str(temp_num)

    l_num = list(s_num)
    l_temp_num = list(s_temp_num)

    return compare_lists(l_num, l_temp_num)



def compare_lists(l1, l2):
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
