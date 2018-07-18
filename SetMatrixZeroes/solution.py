class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        m = len(matrix)
        if m == 0:
            return 
        n = len(matrix[0])
        if n == 0:
            return 
        
        row = [False for _ in xrange(m)]
        col = [False for _ in xrange(n)]
        
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in xrange(m):
            for j in xrange(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
                    

