import sys

class item:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        
        if not nums:
            return []
        
        if len(nums) == 1:
            return [0, 0]
        
        sums = [None for i in xrange(len(nums))]
        prev = 0
        for i, val in enumerate(nums):
            sums[i] = item(prev + val, i)
            prev = sums[i].val
        
        sums.sort()

        diff = sys.maxint
        ans = None
        
        for i in xrange(1, len(sums)):
            if sums[i].val - sums[i-1].val < diff:
                diff = sums[i].val - sums[i-1].val
                ans = [sums[i].index, sums[i-1].index]

        ans.sort()
        ans[0] += 1
        return ans
        
        
