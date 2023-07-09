

# Example 1

a = b = c = 1
# equals to
a = 1
b = a
c = a

# the leftmost target is assigned first.

print(a,b,c)
a += 1
b += 2
c += 3
print(a,b,c)

# Example 2

a = b = c = []

a.append(1)
b.append(2)
c.append(3)

print(a) # [1, 2, 3]
print(b) # [1, 2, 3]
print(c) # [1, 2, 3]

'''
Don't use mutable object (list) in chained assignment. This will cause all pointers point to the same object.
For immutable object ( int / float / bool / str) , it is ok.
'''

