'''
https://leetcode.com/problems/jump-game/

Requirement:
You are given an integer array nums.
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''
from typing import List

'''
-------------
Analysis
-------------
nums = [2,3,1,1,4]

Step 1) We are at index 0, nums[0]=2, it means, maximum we can reach index: 0 + nums[0] = 2, then we move 1 step forward
Step 2) We are at index 1, nums[1]=3, it means, maximum we can reach index: 1 + nums[1] = 4, then we move 1 step forward
Step 3) We are at index 2, nums[2]=1, it means, maximum we can reach index: 2 + nums[2] = 3, then we move 1 step forward
... ...
'''






























class Solution:

    def canJump(self, nums: List[int]) -> bool:

        reachable_index = nums[0]

        if reachable_index >= len(nums) - 1:
            return True

        for i in range(len(nums)):
            if i > reachable_index: # if i is no longer reachable, return False
                return False

            if nums[i] + i > reachable_index: # greedy: set reachable_index as far as possible
                reachable_index = nums[i] + i
                if reachable_index >= len(nums) - 1:
                    return True

        return True




