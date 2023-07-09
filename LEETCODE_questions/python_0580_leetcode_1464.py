'''
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
'''
import heapq
from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        l = heapq.nlargest(2, nums)
        return (l[0] - 1) * (l[1] - 1)