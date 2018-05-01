"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working
out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain
a name score.

For example, when the list is sorted into alphabetical
order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a
score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import os
import time
import string
start = time.time()


def get_alphabetic_value(word):
    value = 0
    for i in word:
        # https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
        value += string.ascii_uppercase.index(i) + 1

    return value


path = "D:\Program Files\PyCharm Projects\ProjectEuler\data_files"

# https://stackoverflow.com/questions/38156102/how-do-i-get-pycharm-to-find-a-file-that-i-want-to-use-in-my-code
file_name = os.path.join(path, "names.txt")


# http://www.pythonforbeginners.com/cheatsheet/python-file-handling
text_file = open(file_name, 'r')

# read the file into a list while replacing quotations and splitting by the comma delimiter
words = text_file.read().replace('"', '').split(',')

# sort the list alphabetically
words = sorted(words)

total = 0
for word in words:
    total += (words.index(word)+1) * get_alphabetic_value(word)

elapsed = (time.time() - start)
print("Result %s produced in %2f seconds" % (total, elapsed))
