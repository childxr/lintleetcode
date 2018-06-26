import copy

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def __init__(self):
        self.ans = []
        
    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
        nums.sort()
        #print nums
        self.helper(nums, 0)
        return self.ans
    
    def helper(self, nums, start_index):
        if start_index == len(nums):
            res = copy.deepcopy(nums)
            self.ans.append(res)
        else:
            for i in xrange(start_index, len(nums)):
                if self.noswap(start_index, i, nums):
                    continue
                nums[i], nums[start_index] = nums[start_index], nums[i]
                self.helper(nums, start_index+1)
                nums[i], nums[start_index] = nums[start_index], nums[i]

    def noswap(self, start_index, i, nums):
        for j in xrange(start_index, i):
            if nums[j] == nums[i]:
                return True
        return False
        
