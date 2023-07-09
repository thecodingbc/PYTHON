

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0

        for i in range(len(gas)):

            total += gas[i] - cost[i] # we can save gas after station i

            if total < 0: # once total gas goes negative, meaning 'start' is not the correct answer, let's try i+i
                total = 0
                start = i + 1

        return start


    
