class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            profit = max(profit, max(prices[i+1:]) - prices[i])
        return profit