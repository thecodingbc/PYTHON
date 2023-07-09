'''


------------------------------------------------------------------------------
Question 1) How to define the dp function? / What's the meaning of the dp array?
------------------------------------------------------------------------------

*THE QUESTION ITSELF IS ALREADY THE ANSWER TO 'HOW TO DEFINE YOUR FUNCTION'. *
The question is,                                                          what's the max sub array sum of array nums?  RESTRICTION: The max sum sub array has to finish till the last value of the head array.
To rephrase it, or to say, to parameterize the question, it becomes       what's the max sub array sum for array nums' head array till index n? RESTRICTION: The max sum sub array has to finish till the last value of the head array.


nums = [-2, 2, -1, 4, -1]

head array / lead list
tail array / tail list

f(n) :
param n: index n of array nums
f(n)   : max sub array sum for array nums' head array till index n

so we need to find the value of max(all f(n) values)

our dp array:
dp = []
index i  :  index i of array nums
dp[i]    :  max sub array sum for array nums' head array till index i
we need find out max(dp)


example:

nums = [-2, 2, -1, 4, -1]  RESTRICTION: The max sum sub array has to finish till the last value of the head array.

f(0): head array of nums till index 0 is [-2]                     max sum sub array is [-2]             its sum is -2, so f(0)= -2,
f(0): head array of nums till index 0 is [-2, 2]                  max sum sub array is [2]              its sum is 2,  so f(1)= 2,
f(0): head array of nums till index 0 is [-2, 2, -1]              max sum sub array is [2, -1]          its sum is 1,  so f(2)= 1,
f(0): head array of nums till index 0 is [-2, 2, -1, 4]           max sum sub array is [2, -1, 4]       its sum is 5,  so f(3)= 5,
f(0): head array of nums till index 0 is [-2, 2, -1, 4, -1]       max sum sub array is [2, -1, 4, -1]   its sum is 4,  so f(4)= 4,


---------------------------------------------------------------------
Question 2) What's the base case? / How to initialize the dp array?
---------------------------------------------------------------------

dp = [0] * len(nums)
dp[0] = nums[0]



------------------------------------------------------------------------
Question 3) What's the state transition? From THE problem to sub-problem?
------------------------------------------------------------------------

Conclusion: our previous dp function definition is WRONG! We have to add a new restriction.
The max sum sub array has to finish till the last value of the head array.

f(n) = nums[n]               if  f(n-1) <= 0
f(n) = nums[n] + f(n-1)      if  f(n-1) > 0

'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]

        return max(dp)