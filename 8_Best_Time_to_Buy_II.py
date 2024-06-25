"""
122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        init: int = prices[0]
        profit: int = 0

        for i in prices[1:]:
            if init < i:
                profit += (i-init)
            init = i
        return profit

# Complexity O(n)