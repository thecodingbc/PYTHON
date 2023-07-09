'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''


# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        '''
        'Optional' means: this is a nullable value, it means, root can be None.

        So when you see:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        it equals to
        def inorderTraversal(self, root: TreeNode) -> List[int]:

        it equals to
        def inorderTraversal(self, root):

        '''

        # corner case / base case
        if not root:
            return []

        result = []

        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))

        return result

    # 炫技
    def inorder2(self, root):
        return self.inorder2(root.left) + [root.val] + self.inorder2(root.right) if root else []


