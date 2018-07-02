class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        n = len(cost)
        # f(n) is the min cose when reaches to n
        # f(n) = min(f(n-1) + cost[n-1], f(n-2) + cost[n-2])
        # f(0) = 0
        # f(1) = 0
        
        # f(i, j), when reaches i via j step, j in [1, 2]
        # f(i, 1) = f(i-1, 1)
        
        
        
        dp = [0 for i in xrange(n+1)]
        
        
        for i in xrange(2, n+1):
            val1 = dp[i-1] + cost[i-1]
            val2 = dp[i-2] + cost[i-2]
            dp[i] = min(val1, val2)
            
        return dp[n]
