import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
        
        dp = [0 for _ in xrange(len(prices))]
        dp[0] = prices[0]
        profit = 0
        for i in xrange(1, len(prices)):
            dp[i] = min(dp[i-1], prices[i])
            profit = max(profit, prices[i] - dp[i-1])
        
        return profit

