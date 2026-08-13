class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minP = prices[0]
        for p in prices:
            res = max(res, p - minP)
            minP = min(p, minP)
        return res