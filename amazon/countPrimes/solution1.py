import math

class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    
    def __init__(self):
        self.cnt = 0
        self.dp = []
    def countPrimes(self, n):
        # write your code here
        self.dp = [False for i in xrange(n+1)]

        for x in xrange(2, n+1):
            if not self.dp[x]:
                self.cnt += 1
                for j in xrange(x*2, n+1, x):
                    self.dp[j] = True
        
        return self.cnt-1 if not self.dp[n] else self.cnt
            
