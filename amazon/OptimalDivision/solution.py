class Solution:
    """
    @param nums: an array
    @return: the corresponding expression in string format
    """
    def optimalDivision(self, nums):
        # Write your code here
        if not nums:
            return ""
        
        if len(nums) == 1:
            return str(nums[0])
        
        if len(nums) == 2:
            return "/".join(str(n) for n in nums)
        
        p1 = "{}/(".format(nums[0])
        for i in xrange(1, len(nums)-1):
            p1 += str(nums[i]) + "/"
        
        p1 += str(nums[len(nums)-1]) + ")"
        
        return p1
