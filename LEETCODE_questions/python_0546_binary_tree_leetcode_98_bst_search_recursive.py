# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # base case
        if root is None:
            return None

        if root.val == val:
            return root

        # recursive call
        # if val < root.val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)

        return self.searchBST(root.left if val < root.val else root.right, val)