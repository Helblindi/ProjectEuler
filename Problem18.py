"""
By starting at the top of the triangle below and moving to adjacent
 numbers on the row below, the maximum total from top to bottom is 23.

                       3
                      7 4
                     2 4 6
                    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
import time
start = time.time()


def max_sum(rows):
    for i in range(len(rows) - 2, -1, -1):
        for j in range(i + 1):
            rows[i][j] += max([rows[i + 1][j], rows[i + 1][j + 1]])
    return rows[0][0]


file = open('data_files/MaximumPathSum1', 'r')
rows = []

for line in file:
    rows.append([int(x) for x in line.split()])

elapsed = (time.time() - start)
print('Found %s rows in %2f seconds' % (max_sum(rows), elapsed))
