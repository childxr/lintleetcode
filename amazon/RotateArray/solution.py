class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        
        k = k % len(nums)
        #for i in xrange(1, k+1):
        #    last = nums[-1]
        #    start_index = len(nums) - 1
        #    while start_index > 0:
        #        nums[start_index] = nums[start_index-1]
        #        start_index -= 1
        #    nums[0] = last
        #    
        #return nums
        from collections import deque
        a = deque(nums)
        a.rotate(k)
        return list(a)

