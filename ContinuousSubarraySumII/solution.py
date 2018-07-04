import sys
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        if not A:
            return []
        
        start, end = 0, 0
        sm = 0
        total = 0
        result = None
        ans = -1 * sys.maxint
        
        for i, val in enumerate(A):
            total += val
            if sm < 0:
                sm = val
                start = end = i
            else:
                sm += val
                end = i
            if ans < sm:
                ans = sm
                result = [start, end]
        
        sm = 0
        start, end = 0, 0
        
        for i, val in enumerate(A):
            
            if sm > 0:
                sm = val
                start = end = i
            else:
                sm += val
                end = i
            if start == 0 and end == len(A) - 1:
                continue
            if total - sm >= ans:
                ans = total - sm
                result = [(end+1)%len(A), (start-1+len(A))%len(A)]
        
        return result
