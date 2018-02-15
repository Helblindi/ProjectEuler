"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


# function to tell us if we have a prime number or not
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


primes = []
for i in range(2, 2000000):
    if is_prime(i):
        primes.append(i)

sum = 0
for j in range(0, len(primes)):
    sum += primes[j]

print("sum:", sum)
