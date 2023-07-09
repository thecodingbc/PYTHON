# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        # Step 1) Sort nums list, so that I make sure the smallest numbers are in the front
        nums.sort()

        # Step 2) Flip all the negative number first.

        '''
        for i in nums:
        for i in range(len(nums)):
        
        I use 2nd solution to loop nums list
        
        I also need to remember how mnay chances have I left to flip a number in nums
        I cannot surpass the total chance count - k
        
        So I use another variable j to store how many flip chances I've used.
        '''

        j = 0

        for i in range(len(nums)):

            if nums[i] < 0 and j < k:
                nums[i] = -nums[i] # flip the negative number
                j += 1 # times counter ++

            else:
                break

        if j == k: # means, in my previous flip try, I've used up all my flip chances
            return sum(nums)


        l = k - j # l is the total count of left flip chances
        if l % 2 == 0:
            return sum(nums)


        nums.sort()
        nums[0] = -nums[0]
        return sum(nums)





