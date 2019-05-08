"""
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form
a word value. For example, the word value for SKY is 19 + 11
+ 25 = 55 = t10. If the word value is a triangle number then
we shall call the word a triangle word.

Using p042_words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English
words, how many are triangle words?
"""
import os
import time
from Misc.useful import get_alphabetic_value


# driver function for our program
def main():
    """
    Creates a list of triangle values.  Then pulls words
    from p042_words.txt and calculates their alphabetic
    value.  It then checks which words have a triangular
    alphabetic value.
    """
    start_time = time.time()

    path = "D:\Program Files\PyCharm Projects\ProjectEuler\data_files"

    # https://stackoverflow.com/questions/38156102/how-do-i-get-pycharm-to-find-a-file-that-i-want-to-use-in-my-code
    file_name = os.path.join(path, "p042_words.txt")

    # http://www.pythonforbeginners.com/cheatsheet/python-file-handling
    text_file = open(file_name, 'r')

    # read the file into a list while replacing quotations and splitting by the comma delimiter
    words = text_file.read().replace('"', '').split(',')

    triangle_numbers = []
    for i in range(1, 20):
        triangle_numbers.append(i*(i+1)*(1/2))
        print(i*(i+1)*(1/2))

    total_words = 0
    for word in words:
        if get_alphabetic_value(word) in triangle_numbers:
            total_words += 1

    # calculate end time and print results
    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (total_words, end_time))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
