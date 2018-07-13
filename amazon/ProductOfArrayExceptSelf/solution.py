class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        rs = 1
        for n in nums:
            rs *= n
        
        ans = []
        for n in nums:
            if n != 0:
                ans.append(rs/n)
            else:
                ans.append(0)
        
        return ans
