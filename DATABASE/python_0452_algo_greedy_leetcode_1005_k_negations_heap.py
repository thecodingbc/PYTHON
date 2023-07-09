import heapq
from typing import List




class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:


        '''

        BASE KNOWLEDGE:

        heapq is a standard python library

        heapq means 'heap queue'.  First in, First out.

        heap is a complete binary tree.
        1) All levels are full, except the last level.
        2) only the rightmost leaves may be missing in the last level.

        there are 2 kinds of heap - max heap & min heap
        max heap - parent node is always bigger than children nodes
        min heap - parent node is always smaller than children nodes

        so in max heap, the biggest number is the root node
        so in min heap, the smallest number is the root node
        '''


        '''
        Now we learn to use class Node to express a Tree, 
        We can also use list / array to express a Tree.
        '''

        heapq.heapify(nums) # reorder the nums list into a min heap, root node becomes the smallest value

        for _ in range(k):

            m = heapq.heappop(nums) # remove root node of the heap (smallest value of the nums), assign it variable m
            heapq.heappush(nums, -m) # add back -m to the heap

        return sum(nums)


