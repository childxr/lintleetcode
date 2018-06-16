class Solution:

	def max_number_mountain_sequence(self, nums):
		if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            # make sure left is always to the left of right 
            # while preserving right inbound
            mid = left + (right - left) / 2
            if (nums[mid] < nums[mid + 1]):
                # perform adjacent step by step climbing
                left = mid + 1
            else:
                right = mid
        if nums[left] < nums[right]:
            return nums[right]
        else:
            return nums[left]
