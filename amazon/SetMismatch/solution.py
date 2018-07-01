class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        max_v = max(nums)
        mapper = [0 for i in xrange(max_v + 1)]
        for num in nums:
            mapper[num]+=1
        #print mapper
        
        ans = [0, 0]
        for i in xrange(1, max_v + 1):
            if mapper[i] > 1:
                ans[0] = i
            if mapper[i] == 0:
                ans[1] = i
        if ans[1] == 0:
            ans[1] = max_v + 1
        return ans
