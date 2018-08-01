"""
145 is a curious number, as 1! + 4!+ 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import time


def main():
    start_time = time.time()

    _sum = 0

    # loop from 3 to 999
    for i in range(3, 100000):
        # looped until 10,000,000 and still only found 145 and 40,585
        if is_curious(i):
            print(i, ' is curious!')
            _sum += i

    # print('test to check if a number is curious')
    # num = 146
    # print('is ', num, ' curious? ', is_curious(num))

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (_sum, end_time))


def is_curious(num):
    digits = get_digits(num)
    val = 0
    for digit in digits:
        ind_val = 1
        for i in range(1, digit + 1):
            ind_val *= i
        val += ind_val

    return num == val


def get_digits(num):
    num_array = []

    while num != 0:
        digit = num % 10
        num //= 10
        num_array.append(digit)

    return num_array


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()