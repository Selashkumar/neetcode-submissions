class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyNext = 0
        sellNext = 0
        buyAfterCooldown = 0
        for i in range(len(prices) -1, -1, -1):
            oldBuy = buyNext
            buyNext = max(sellNext - prices[i], buyNext)
            sellNext = max(buyAfterCooldown + prices[i], sellNext)
            buyAfterCooldown = oldBuy
        return buyNext