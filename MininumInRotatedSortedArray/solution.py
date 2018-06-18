class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        target = nums[right]
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] <= target:
                right = mid
                target = nums[right]
            else:
                left = mid
        
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
