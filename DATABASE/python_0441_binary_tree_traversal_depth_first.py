'''

a binary tree = root node + left sub binary tree + right sub binary tree

'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder(root):

    # base case
    if root == None:
        return

    print(root.val, end=' ')  # Step 1) print the node data
    preorder(root.left)       # Step 2) Recursive call - traverse the left sub tree
    preorder(root.right)      # Step 3) Recursive call - traverse the right sub tree


def inorder(root):

    # base case
    if root == None:
        return

    inorder(root.left)       # Step 1) Recursive call - traverse the left sub tree
    print(root.val, end=' ')  # Step 2) print the node data
    inorder(root.right)      # Step 3) Recursive call - traverse the right sub tree


def postorder(root):

    # base case
    if root == None:
        return

    postorder(root.left)       # Step 1) Recursive call - traverse the left sub tree
    postorder(root.right)      # Step 2) Recursive call - traverse the right sub tree
    print(root.val, end=' ')  # Step 3) print the node data


# Driver code

# level 0 ----------------
root = Node(20)

# level 1 ----------------
root.left = Node(16)
root.right = Node(25)

# level 2 ----------------
root.left.left = Node(6)
root.left.right = Node(17)

root.right.left = Node(21)
root.right.right = Node(29)

# level 3 ----------------
root.left.left.left = Node(0)
root.left.left.right = Node(7)

root.right.right.left = Node(28)
root.right.right.right = Node(51)

# level 4 ----------------
root.right.right.right.left = Node(46)


print("Depth first pre_order -------------------------")
preorder(root) # write down output

print("\nDepth first in_order -------------------------")
inorder(root) # write down output

print("\nDepth first post_order -------------------------")
postorder(root) # write down output

'''
Homework

1) read ppt
2) read 0441 code
3) write down output without run my code
4) Work on these leetcode question:

https://leetcode.com/problems/binary-tree-inorder-traversal/
https://leetcode.com/problems/binary-tree-preorder-traversal/
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''
