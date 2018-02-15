"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.  What is the 10,000th prime number?
"""


# function to tell us if we have a prime number or not
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# initialize primes array and get user input
# which prime number we are looking for
primes = []
prime_number = input("Which prime number would you like?")
prime_number = int(prime_number)

# iterate through integers to find the primes and add them to our array
j = 2
while len(primes) <= prime_number:
    if is_prime(j):
        primes.append(j)

    j += 1

print(primes[prime_number - 1])
