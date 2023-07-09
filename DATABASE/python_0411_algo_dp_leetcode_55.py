'''
------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array?
------------------------------------------------------------------------------

f(n)
param n : index n of array nums
f(n)    : the max index can be reached from index n

---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------

dp = [0] * len(nums)
dp[0] = nums[0]

------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to sub-problem?
------------------------------------------------------------------------

For index i, there are 2 cases:
Case 1) Not reachable from index i-1, dp[i-1] < i  => return False
Case 2) Reachable from index i-1, dp[i-1] >= i

For Case 1, we can simply return False
For Case 2, what value should we put for dp[i]?

dp[i] = max(dp[i-1], i + nums[i])

Attention: there should be a shortcut as well, as soon as dp[i] >= len(nums) -1, return True

'''






































from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:

        # define db array
        dp = [0] * len(nums)

        # init db array
        dp[0] = nums[0]

        # Simply loop the only state index i:
        for i in range (1, len(nums)):

            if dp[i-1] < i: # i is not reachable
                return False

            dp[i] = max(dp[i-1], i + nums[i])

            if dp[i] >= len(nums) - 1:
                return True

        return True
