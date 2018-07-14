import sys

class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        # Write your code here
        n = len(A)
        
        keep = [sys.maxint for _ in xrange(n)]
        swap = [sys.maxint for _ in xrange(n)]
        keep[0] = 0
        swap[0] = 1
        
        for i in xrange(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1]+1)
        
        return min(swap[n-1], keep[n-1])
        
        
