class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return k
        if k <= 0:
            return 0
        
        dp = [0 for _ in xrange(n+1)]
        
        dp[1] = k
        dp[2] =  k * k
        
        for i in xrange(3, n+1):
            dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
        return dp[n]

