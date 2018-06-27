class Solution:
    
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = set([])
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
    
        return list(ans)
                
