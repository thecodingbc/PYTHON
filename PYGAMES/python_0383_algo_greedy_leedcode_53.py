'''
https://leetcode.com/problems/maximum-subarray/
'''

'''

array: [-2,1,-3,4,-1,2,1,-5,4]


This is a step-by-step strategy, I need to handle those numbers one-by-one.
I keep a sub_array, and I try to keep sum(sub_array) as big as possible.

Here comes my greedy algo:

Each time, BEFORE we add a new value i into my sub_array, there are 4 situations:

1) WHEN : sum(sub_array) <= 0     AND  i >= 0
   THEN : sub_array.clear()
          sub_array.append(i)
   BECAUSE : sum(sub_array) <= 0, keep those numbers in sub_array will only cause a negative effect.
             I can throw away all those existing numbers in my sub_array, keep only i in it.
             After these 2 steps, sub_array will have a bigger sum, so no need to remember the current sum(sub_array) 
        
2) WHEN : sum(sub_array) <= 0     AND i < 0
   THEN : save_sum(sub_array)
          sub_array.clear()
          sub_array.append(i)
   BECAUSE: sum(sub_array) <= 0, keep those numbers in sub_array will only cause a negative effect. 
            I can throw away all those existing numbers in my sub_array, keep only i in it.
            After these 2 steps, sub_array CAN possibly have a even smaller sum. So I need to remember the current sum(sub_array) before these 2 steps.
            
3) WHEN: sum(sub_array) > 0     AND i >= 0
   THEN: sub_array.append(i)
   BECAUSE: obviously
   
4) WHEN: sum(sub_array) > 0     AND i < 0
   THEN: save_sum(sub_array)
         sub_array.append(i)
   BECAUSE: Even though i is negative, I still need to take it into my sub_array, in case there are some really big number after i.
            After the step, sub_array WILL have a smaller sum. So I need to remember the current sum(sub_array) before the step.  
'''


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        '''
        1) as this is a step-by-step strategy, I need to loop all those numbers one by one.
        2) I keep a sub_array, and I try to keep sum(sub_array) as big as possible
        3) whenever sum(sub_array) becomes smaller, I try to save the current sum(sub_array) into a possible_result list.
        '''

        sub_array = []
        largest_sum = float("-inf")

        sub_array_sum = 0

        for i in nums:

            if i < 0 and len(sub_array) > 0 and sub_array_sum > largest_sum:
                    largest_sum = sub_array_sum

            if sub_array_sum <= 0:
                sub_array.clear()
                sub_array_sum = 0

            sub_array.append(i)
            sub_array_sum += i

        if len(sub_array) > 0 and sub_array_sum > largest_sum:
            largest_sum = sub_array_sum

        return largest_sum


# TEST PROGRAM --------------------------
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    result = s.maxSubArray(nums)
    print(result)