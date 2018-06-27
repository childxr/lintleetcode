class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
        left, right = 0, 0
        
        ans = sys.maxint
        
        csum = 0
        
        while True:
            if right == len(nums) and csum < s:
                break
            if csum < s and right < len(nums):
                csum += nums[right]
                right += 1
            else:
                while left <= right and csum >= s:
                    l = right-left
                    ans = min(l, ans)
                    csum -= nums[left]
                    left += 1
                    
        if ans == sys.maxint:
            return -1
        
        return ans


