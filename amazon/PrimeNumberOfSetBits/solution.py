class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        dp = [False for x in xrange(R+1)]
        dp[0], dp[1] = True, True
        for i in xrange(2, R+1):
            if not dp[i]:
                for j in xrange(i+i, R+1, i):
                    dp[j] = True
        
        ans = 0
        for i in xrange(L, R+1):
            nb = bin(i).count("1")
            if not dp[nb]:
                ans += 1
        
        return ans
