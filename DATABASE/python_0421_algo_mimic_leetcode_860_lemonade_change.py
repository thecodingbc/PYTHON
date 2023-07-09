# https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):

        five_do = ten_do = 0  # Chained Assignment.

        for bill in bills:

            if bill == 5:
                five_do += 1

            elif bill == 10:
                if not five_do: # when it int var is 0, it is False, otherwise it is True
                    return False
                five_do -= 1
                ten_do += 1

            else:
                if ten_do and five_do: # this equals to: if ten_do > 0 and five_do > 0
                    ten_do -= 1
                    five_do -= 1

                elif five_do >= 3:
                    five_do -= 3

                else:
                    return False

        return True
