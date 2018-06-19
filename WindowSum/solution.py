class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if not nums:
            return []
        if len(nums) < k:
            return [sum(nums)]
        
        window_sum = sum(nums[:k])
        ans = [window_sum]
        i = k
        while i < len(nums):
            window_sum = window_sum - nums[i-k] + nums[i]
            ans.append(window_sum)
            i += 1
        return ans
        

