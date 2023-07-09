# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: list) -> int:

        total_profit = 0

        trend = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):

            if prices[i] > prices[i-1] and trend <= 0:
                buy_price = prices[i-1]
                trend = 1
            elif prices[i] < prices[i-1] and trend >= 0:
                total_profit += prices[i-1] - buy_price
                trend = -1

        if trend > 0:
            total_profit += prices[-1] - buy_price

        return total_profit