class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def getRow(self, rowIndex):
        # write your code here
        
        # 1
        # 1, 1
        # 1, 2, 1
        # 1, 3, 3, 1
        
        if rowIndex < 0:
            return 0
        
        arr = [0 for i in xrange(34)]
        arr[0] = 1
        ans = None
        for i in xrange(1, 34):
            prev, cur = arr[0], arr[1]
            for j in xrange(1, i):
                tmp = cur
                arr[j] = prev + cur
                prev = tmp
                cur = arr[j+1]
            arr[i] = 1
            if i == rowIndex:
                ans = [i for i in arr if i > 0]
        return ans
            
