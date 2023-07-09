'''
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''


# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # corner case / base case
        if not root:
            return []

        result = []

        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))

        return result

    # 炫技
    def preorder2(self, root):
        return [root.val] + self.inorder2(root.left) + self.inorder2(root.right) if root else []


