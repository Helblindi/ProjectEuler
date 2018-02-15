"""
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
                                a^2 + b^2 = c^2.
For examples, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import numpy as np

def is_pythagorian_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False


for a in range(1, 1000):
    for b in range(a+1, 1001):
        c = int(np.sqrt(a**2 + b**2))
        if is_pythagorian_triple(a, b, c):
            sum = a + b + c
            if sum == 1000:
                print("a:", a)
                print("b:", b)
                print("c:", c)
                product = a * b * c
                print("Product of a*b*c: ", product)


print("Process Finished")
