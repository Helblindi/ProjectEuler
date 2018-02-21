"""
Largest Palindrome Product
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


# function which return reverse of a string
def reverse(s):
    return s[::-1]


# function to check if a number is a palindrome
def is_palindrome(s):
    # Calling reverse function
    s = str(s)
    rev = reverse(s)

    # Checking if both string are equal or not
    if s == rev:
        return True
    return False


# iterate through all multiples of 3 digit numbers
palindrome = 0
for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        if is_palindrome(num):
            if num > palindrome:
                palindrome = num

print(palindrome)
