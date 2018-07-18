class Solution:
    """
    @param nums: An array of integers.
    @return: nothing
    """
    def arrayReplaceWithGreatestFromRight(self, nums):
        # Write your code here.
        if not nums:
            return []
            
        n = len(nums)
        val = nums[n-1]
        for i in xrange(n-2, -1, -1):
            tmp = nums[i]
            nums[i] = val
            val = max(nums[i], tmp)
        
        nums[n-1] = -1
        return nums
