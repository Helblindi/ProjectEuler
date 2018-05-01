"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

https://www.geeksforgeeks.org/permutation-and-combination-in-python/
"""
import time
from itertools import permutations


start_time = time.time()

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

perm = sorted(perm)

end_time = time.time() - start_time

print("found %s in %2f seconds." % (perm[999999], end_time))
