class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        m = len(A)
        if not m:
            return []
        n = len(A[0])
        if not n:
            return []
            
        ans = []
        
        start, end = 1, m-2
        
        while start <= end:
            
            mid = (end+start)/2

            col = self.findCol(mid, A)
            
            if A[mid-1][col] > A[mid][col]:
                end = mid-1
            
            elif A[mid+1][col] > A[mid][col]:
                start = mid+1
            
            else:
                ans += [mid, col]
                break
        
        return ans
        
    
    def findCol(self, r, A):
        n = len(A[0])
        c = 0
        for j in xrange(n):
            if A[r][j] > A[r][c]:
                c = j
        return c
        
