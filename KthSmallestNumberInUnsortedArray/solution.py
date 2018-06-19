class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if not nums:
            return []
        if len(nums) < k:
            return nums
        return self.innerSmallest(k-1, nums, 0, len(nums))
        
    def innerSmallest(self, k, nums, lo, hi):
        pivot = self.partition(lo, hi, nums)
        print pivot
        if pivot == k:
            return nums[k]
        elif pivot < k:
            return self.innerSmallest(k, nums, pivot + 1, hi)
        else:
            return self.innerSmallest(k, nums, lo, pivot)
    
    def partition(self, lo, hi, nums):
        #print nums
        #print lo, hi
        if lo >= hi:
            return lo
        i, j = lo, hi
        
        while True:
            i += 1
            j -= 1
            while i < hi and nums[i] < nums[lo]:
                i += 1
            while j > lo and nums[j] > nums[lo]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[lo], nums[j] = nums[j], nums[lo]
        #print nums
        return j

