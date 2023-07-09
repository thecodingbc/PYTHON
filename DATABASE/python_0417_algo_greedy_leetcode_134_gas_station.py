# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        '''

        Shortcut return:

        because no matter which gas station you starts from, you always spend the fix amount of gas
        so, if sum(gas) < sum(cost), then you can never finish the route.
        Otherwise, you are sure to finish the circle.
        '''

        if sum(gas) < sum(cost):
            return -1

        '''
        The car drives clockwise.
        
        The more gas you collect,                   --> gas[i]
        the less distance you travel,               --> cost[i]
        the more gas will be left in the tank       --> gas[i] - cost[i]
        the safer you will be to finish the whole route.
        
        let's save this value gas[i] - cost[i], into a variable accumulated_gas_delta
        
        I hope to find the STARTING point, from which onwards, I can accumulate as higher as possible for all accumulated_gas_delta values.
        
        Because I need to find the STARTING point, so I can loop counterclockwise, I still continuously accumulate this accumulated_gas_delta.
        
        I find the highest value, that's the STARTING point where I should start my car. 
        
        '''





















        

        accumulated_gas_delta = 0
        accumulated_gas_delta_max = 0
        starting_point = 0

        for i in range(len(gas) - 1, -1, -1):

            accumulated_gas_delta += (gas[i] - cost[i])

            if accumulated_gas_delta > accumulated_gas_delta_max:
                accumulated_gas_delta_max = accumulated_gas_delta
                starting_point = i

        return starting_point


