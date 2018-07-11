class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <= 0:
            return 1
        dp = [0 for i in xrange(n+1)] if n > 3 else [0, 0, 0, 0]
        dp[1], dp[2] = 1, 2
        dp[3] = dp[1] + dp[2] + 1
        i = 4
        while i <= n:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            i += 1
        return dp[n]

