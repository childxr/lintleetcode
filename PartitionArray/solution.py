class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
        
        lo, hi = 0, len(nums) - 1
        i, j = -1, len(nums)
        while True:
            i += 1
            j -= 1
            while i < hi and nums[i] < k:
                i += 1
            while j > lo and nums[j] >= k:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        
        if nums[j] >= k:
            return j
        if nums[i] >= k:
            return i
        return i + 1
