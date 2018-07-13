class Solution:
    """
    @param A: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """

    def maxRotateFunction(self, A):
        # Write your code here
        
        if not A:
            return 0
        
        ans = 0
        rs = 0
        
        for i, a in enumerate(A):
            rs += a
            ans += i * a
        
        f = ans
        for i in xrange(1, len(A), 1):
            ans = ans + rs - len(A) * A[len(A)-i]
            f = max(f, ans)
        
        return f
