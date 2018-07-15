class Solution:
    """
    @param nums: the original array
    @param req: the direction each time
    @return: the final folded array 
    """
    def folding(self, nums, req):
        # write your code here
        if not nums or not req:
            return nums
        row, col = 1, len(nums)
        for r in req:
            if r == 0:
                nums = self.foldleft(nums, row, col)
            else:
                nums = self.foldright(nums, row, col)
            row *= 2
            col /=2
        
        return nums
        
    def foldleft(self, nums, row, col):
        n = col/2
        stack = []
        for i in xrange(row):
            for j in xrange(n):
                index = i * col + j
                stack.append(nums[index])
        
        ans = []
        while len(stack) > 0:
            ans.append(stack.pop())
        
        for i in xrange(row):
            for j in xrange(n, 2*n):
                index = i * col + j
                ans.append(nums[index])
        
        return ans
        
    def foldright(self, nums, row, col):
        n = col/2
        stack = []
        for i in xrange(row):
            for j in xrange(n, 2*n):
                index = i * col + j
                stack.append(nums[index])
        ans = []
        while len(stack) > 0:
            ans.append(stack.pop())
        
        for i in xrange(row):
            for j in xrange(n):
                index = i * col + j
                ans.append(nums[index])
        
        return ans
        

