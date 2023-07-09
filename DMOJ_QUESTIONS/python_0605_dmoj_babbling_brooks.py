'''
https://dmoj.ca/problem/ccc00s2
'''

# Remove these 2 lines when you actually submit it on dmoj -----------
import sys
sys.stdin = open('python_0605_dmoj_babbling_brooks.txt', 'r')
# --------------------------------------------------------------------

# step 1) prepare data -------------------
n = int(input())

rivers = []

for i in range(n):
    rivers.append(int(input()))

# LOG 大法

print(f"LOG - the river is: {rivers}")

# Step 2) mimic the process ---------------

while True:

    command = int(input())

    if command == 77:
        print(f"LOG - got 77, program exit!")
        break

    elif command == 99:
        print(f"LOG - got 99, I will split a river")

        index = int(input()) - 1
        print(f"LOG - split river index: {index}")

        percentage = int(input())
        print(f"LOG - split to left: {percentage}%")

        left = rivers[index] * percentage / 100
        right = rivers[index] - left
        print(f"LOG - left sub river has: {left}, right sub river has: {right}")

        rivers[index] = left
        rivers.insert(index + 1, right)
        print(f"LOG - now the rivers become: {rivers}")


    elif command == 88:
        print(f"LOG - got 88, I will merge 2 rivers")

        index = int(input()) - 1
        print(f"LOG - merge river index: {index}")

        rivers[index] = rivers[index] + rivers[index + 1]
        print(f"LOG - After merge, now river[{index}] becomes {rivers[index]}")

        rivers.pop(index + 1)
        print(f"LOG - now the rivers become: {rivers}")


# Step 3) print the result ----------------------
for i in rivers:
    print(i, end= ' ')



'''
IMPORTANCE!!! ------------------------------
1) before submit your code, don't forget to remove
   a) read file code import sys / open
   b) all LOG code
   
2) insert v into list : rivers.insert(index, v)
3) delete from list   : rivers.pop(index)  
--------------------------------------------
'''