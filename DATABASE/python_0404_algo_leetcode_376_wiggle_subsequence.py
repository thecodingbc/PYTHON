from typing import List


class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:

        # Step 1) 1st number as the 1st single number subsequence
        all_lists = [[nums[0]]]

        # Step 2) handle those following numbers 1 by 1
        # Just append the number to those
        for i in nums[1:]:
            self.append_i_to_all_lists(i, all_lists)

        return len(all_lists[-1])







    def append_i_to_all_lists(self, i, all_lists):

        for a_list in all_lists[::-1]: # 最长的list 总在最后, 所有从后面开始添加，只要有1个可以把i append 进去，那么就不需要尝试前面短的list了

            if len(a_list) > 1 and (i - a_list[-1]) * (a_list[-1] - a_list[-2]) < 0:
                new_list = a_list[:]
                new_list.append(i)
                all_lists.append(new_list)
                return

            if len(a_list) == 1 and a_list[-1] != i:
                new_list = a_list[:]
                new_list.append(i)
                all_lists.append(new_list)


if __name__ == '__main__':
    s = Solution()
    s.wiggleMaxLength([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15])