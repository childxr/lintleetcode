class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        last0 = -1
        for index, num in enumerate(nums):
            if num != 0:
                last0 += 1
                nums[last0] = num
        
        for i in xrange(last0 + 1, len(nums)):
            nums[i] = 0

