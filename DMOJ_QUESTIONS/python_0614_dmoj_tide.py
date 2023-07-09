# https://dmoj.ca/problem/dmopc14c7p2

# Remove these 2 lines when you actually submit it on dmoj --------
import sys
sys.stdin = open('python_0614_dmoj_tide.txt', 'r')
# -----------------------------------------------------------------

i = int(input())
print(f"LOG - there are in total {i} tide readings")

readings = input().split()
l = [int(t) for t in readings]
print(f"LOG - the tide readings are: {l}")

min_tide = min(l)
max_tide = max(l)
print(f"LOG - min tide is: {min_tide}, max tide is: {max_tide}")

min_index = l.index(min_tide)
max_index = l.index(max_tide)
print(f"LOG - min tide index is: {min_index}, max tide index is: {max_index}")

flag = True

if min_index > max_index:
    flag = False

for i in range(min_index, max_index):
    if l[i+1] <= l[i]: # not strictly increasing sequence
        flag = False
        break

if flag:
    print(max_tide - min_tide)
else:
    print("unknown")


