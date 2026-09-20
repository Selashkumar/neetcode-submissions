class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key = (i, isBuy) val= maxProfit
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in dp:
                return dp[(i, isBuy)]
            cooldown = dfs(i+1,isBuy)
            if isBuy:
                buy = dfs(i+1, not isBuy) - prices[i]
                dp[(i, isBuy)] = max(cooldown, buy)
            else:
                sell = dfs(i+2, not isBuy) + prices[i]
                dp[(i, isBuy)] = max(cooldown, sell)
            return dp[(i, isBuy)]
        return dfs(0, True)