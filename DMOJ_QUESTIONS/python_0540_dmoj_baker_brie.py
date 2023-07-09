'''
https://dmoj.ca/problem/ecoo17r3p1
'''

# import sys
# sys.stdin = open("python_0540_dmoj_baker_brie_input.txt", 'r')

for _ in range(10):

    # 1st line is composed of f and d
    x = input().split()
    f = int(x[0])
    d = int(x[1])

    # stores all the data
    info = []

    # loop d days
    for i in range(d):

        l = input().split()
        n = [int(x) for x in l] # list comprehension -> convert str list l to int list n
        info.append(n)
        # Now, info[i][j] means, the total baker sold on day i for franchise j

    # Now, all data is loaded into info nested list

    r = 0

    # No.1 Calculate whether baker sold total across all franchise on a daily basis
    # loop d days
    for o in range(d):
        t0 = sum(info[o])
        if t0 % 13 == 0:
            r += (t0 // 13)

    # No.2 Calculate baker sold total across all days on per franchise basis
    # Loop f franchise
    for o in range(f):
        t1 = 0
        for b in range(d):
            t1 += info[b][o]

        if t1 % 13 == 0:
            r += (t1 // 13)

    print(r)