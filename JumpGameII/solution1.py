import sys
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A:
            return 0
        
        dp = [sys.maxint for i in xrange(len(A))]
        dp[0] = 0
        i, j = 0, 0
        while i < len(A):
            step = A[i]
            j = i + 1
            while j <= i + step and j < len(A):
                dp[j] = min(dp[j], dp[i] + 1)
                j += 1
            i += 1
        return dp[len(A)-1]
