
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        largest_sum = nums[0]
        sub_array_sum = 0

        for i in nums:
            if sub_array_sum > 0:
                sub_array_sum += i
            else:
                sub_array_sum = i
            largest_sum = max(largest_sum, sub_array_sum)

        return largest_sum