'''
https://dmoj.ca/problem/ecoo18r1p1
'''


# Remove these 2 lines when you actually submit it on dmoj --------
import sys
sys.stdin = open('python_0610_dmoj_willows_wild_ride.txt', 'r')
# -----------------------------------------------------------------


# because there are in total 10 datasets, so I loop 10 times

for i in range(10):

    i, j = input().split() # tuple unpacking
    i = int(i)
    j = int(j)

    print(f"LOG - the cat will play with the box for {i} days")
    print(f"LOG - in total, there are {j} days")

    k = [] # stores the box info

    for _ in range(j):
        t = input()
        if t == 'E':
            k.append(0)
        else:
            k.append(1)

    print(f"LOG - box info is: {k}")

    '''
    The cat is also at 2 status for each day
    0 - not playing
    1 - playing
    '''

    l = []

    for index, box in enumerate(k):

        day = index + 1

        if box == 0:
            print(f"LOG - on day {day}, there is no box")

            if len(l) < day:
                l.append(0)
                print(f"LOG - cat is doing nothing, add 0 to occupy the day. Cat's list l is: {l}")
            else:
                print(f"LOG - cat is still playing with the old box. Cat's list l is: {l}")


        else:
            print(f"LOG - on day {day}, there is a box coming, add {i} 1 to cat's list l")
            l.extend([1] * i)
            print(f"LOG - now, cat's list l is: {l}")

    print(len(l) - j)

    print(f"LOG ------------------------------------------------------")


'''
IMPORTANCE!!! --------------------------------
1) use enumerate(l) to loop list l
   so that you get both index and its value
----------------------------------------------
'''