class Solution:
    '''
     * @param nums: the given k sorted arrays
     * @return: the median of the given k sorted arrays
    '''
    def findMedian(self, nums):
        if not nums:
            return 0.
            
        n = 0
        for row in nums:
            n += len(row)
        
        if n == 0:
            return 0.
        
        if n % 2 == 0:
            return (self.findKth(nums, n/2) + 
                    self.findKth(nums, n/2+1))/2.
        
        return self.findKth(nums, n/2+1)/1.
    
    # k is not zero-based, it starts from 1
    def findKth(self, nums, k):
        import sys
        start, end = 0, sys.maxint

        # find first x that >= k numbers is smaller or equal to x
        while start + 1 < end:
            mid = start+(end-start)/2
            if self.countSmallerOrEqual_2D(nums, mid) < k:
                start = mid
            else:
                end = mid

        if self.countSmallerOrEqual_2D(nums, start) >= k:
            return start 
        else:
            return end
    
    def countSmallerOrEqual_2D(self, nums, target):
        res = 0
        for row in nums:
            if row:
                res += self.countSmallerOrEqual(row, target)
        return res 
    
    def countSmallerOrEqual(self, arr, target):
        start = 0
        end = len(arr)-1
        
        # find first index that arr[index] > target
        while start + 1 < end:
            mid = start+(end-start)/2
            if arr[mid] <= target:
                start = mid
            else:
                end = mid
        
        if arr[start] > target:
            return start
        
        if arr[end] > target:
            return end
        
        return len(arr)
