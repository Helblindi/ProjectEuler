"""
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import time


# driver function for our program
def main():
    """
    """
    start_time = time.time()
    max_triangles = 0
    max_p = 10

    # main loop
    for p in range(10, 1001):
        num_triangles = 0

        # first iterate on the short side
        for a in range(1, p // 3 + 1):

            # next iterate over the middle length side
            for b in range(a, (p - a) // 2):

                # calculate hypotenuse and check
                c = p - a - b
                if c**2 == a**2 + b**2:

                    # We found a triangle!
                    num_triangles += 1

        # Validate results
        if num_triangles > max_triangles:
            max_triangles = num_triangles
            max_p = p

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (max_triangles, end_time))
    print("This occurs when the perimeter = %s." % max_p)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
