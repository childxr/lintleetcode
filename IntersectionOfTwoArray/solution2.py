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
        s1 = set(nums1)
        ans = set([])
        for elem in nums2:
            if elem in s1 and elem not in ans:
                ans.add(elem)
        return list(ans)
