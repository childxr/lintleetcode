class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def swap(self, a, b, nums):
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b -= 1
        
    def rotate(self, nums, k):
        # Write your code here
        k = k % len(nums)
        
        # 1, 2, 3, 4, 5, 6, 7
        # 4, 3, 2, 1, 7, 6, 5
        # 5, 6, 7, 1, 2, 3, 4
        
        self.swap(0, len(nums)-k-1, nums)
        self.swap(len(nums)-k, len(nums)-1, nums)
        self.swap(0, len(nums)-1, nums)
        return nums
        
