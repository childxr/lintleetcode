class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        
        ans = 1
        n = len(s)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]

        for i in xrange(n):
            dp[i][i] = 1
        
        for i in xrange(1, n):
            if s[i-1] == s[i]:
                dp[i-1][i] = 2
                ans = 2

        for l in xrange(3, n+1):
            for i in xrange(0, n+1-l):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(max(dp[i][j-1], dp[i+1][j]), 1)
                ans = max(dp[i][j], ans)
        
        return ans
