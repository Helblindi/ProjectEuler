"""

"""

"""
Plan:

"""

import time
import sys
sys.path.insert(0, '/Users/madisonsheridan/Workspace/ProjectEuler/Misc')
from useful import get_list_of_primes, is_prime


# driver function for our program
def main():
    start_time = time.time()
    p1_wins = 0
    p2_wins = 0
    ties = 0

    with open('../data_files/p054_poker.txt') as f:
        lines = f.readlines()

        for line in lines:
            l = line.split()
            p1 = l[0:5]
            p2 = l[5:10]

            # Check score for both p1 and p2
            p1_score, p1t = check_score(p1)
            p2_score, p2t = check_score(p2)

            # Compare scores
            if p1_score > p2_score:
                p1_wins += 1
            elif p1_score < p2_score:
                p2_wins += 1
            else:
                if p1t[0] > p2t[0]:
                    p1_wins += 1
                elif p1t[0] < p2t[0]:
                    p2_wins += 1
                else:
                    if p1t[1] > p2t[1]:
                        p1_wins += 1
                    elif p1t[1] < p2t[1]:
                        p2_wins += 1
                    else:
                        if p1t[2] > p2t[2]:
                            p1_wins += 1
                        elif p1t[2] < p2t[2]:
                            p2_wins += 1
                        else:
                            if p1t[3] > p2t[3]:
                                p1_wins += 1
                            elif p1t[3] < p2t[3]:
                                p2_wins += 1
                            else:
                                if p1t[4] > p2t[4]:
                                    p1_wins += 1
                                elif p1t[4] < p2t[4]:
                                    p2_wins += 1
                                else:
                                    ties += 1
        f.close()


    end_time = time.time() - start_time
    # print("Found %s in %2f seconds." % (max_family_number, end_time))


def check_score(cards):
    # TODO: Calculate score

    # TODO: Sort numerical values
    # returns score and ordered numerical values of cards for a tie breaker
    return 1, 0


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
