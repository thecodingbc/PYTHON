'''
https://leetcode.com/problems/wiggle-subsequence


No1. I need to remember the current trend? Is it going up? going down? Initially, it is flat (0).

When it is going up, trend = 1
When it is going down, trend = -1


'''

class Solution:

    def wiggleMaxLength(self, nums: list) -> int:

        # 1st number is always part of the LWS, so init value is 1
        lws_value = 1


        '''
        When it is going up, trend = 1
        When it is going down, trend = -1
        '''
        trend = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and trend <= 0:
                lws_value += 1
                trend = 1
            elif nums[i] < nums[i-1] and trend >= 0:
                lws_value += 1
                trend = -1

        return lws_value

