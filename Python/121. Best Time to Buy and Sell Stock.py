from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_tracker = -1
        res = 0
        for p in range(n-1, -1, -1):
            if prices[p] > max_tracker:
                max_tracker = prices[p]
            else:
                res = max(max_tracker - prices[p], res)
        return res