class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        cnt = 0
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s <= target:
                i += 1
            else:
                cnt += j - i  # from i, i + 1, ..., to j, total j - i 
                j -= 1
        return cnt
