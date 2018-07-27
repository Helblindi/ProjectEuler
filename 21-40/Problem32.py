"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it
once in your sum.
"""
import time


def main():
    start_time = time.time()

    products = []

    for a in range(1, 100000):
        for b in range(a, 100000):
            if len(str(a) + str(b) + str(a*b)) > 9:
                break
            if is_pandigital_product(a, b):
                products.append(a*b)
                print("%i x %i = %i" % (a, b, a * b))

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum(set(products)), end_time))


def get_digits(num):
    num_array = []

    while num != 0:
        digit = num % 10
        num //= 10
        num_array.append(digit)

    return num_array


def is_pandigital(num):
    num_array = get_digits(num)
    if (len(set(num_array)) == len(num_array) == max(num_array)) and min(num_array) == 1:
        return True
    else:
        return False


def is_pandigital_product(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    numbers = int(numbers)
    return is_pandigital(numbers)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
