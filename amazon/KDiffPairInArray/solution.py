class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        k = abs(k)
        mapper = {}
        for num in nums:
            p = mapper.get(num, 0)
            mapper[num] = p + 1
        
        keyset = mapper.keys()
        keyset.sort()
        count = 0
        for key in keyset:
            if k == 0 and mapper[key] > 1:
                count += 1
            elif k > 0 and key + k in keyset:
                count += 1
        
        return count
