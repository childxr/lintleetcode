class Solution:

	def last_position_target(self, nums, target):

		if not nums:
            return -1
        left, right = 0, len(nums) - 1
        
        while left + 1 <  right:
        	# make sure left pointer is to the left of right pointer and right pointer always inbound
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
        
        if not nums:
			return -1
		if not nums:
			return -1
