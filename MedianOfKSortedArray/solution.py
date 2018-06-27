import heapq

class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        if not nums:
            return 0.0
        cnt = 0
        for num in nums:
            cnt += len(num)
        
        if cnt == 0:
            return 0.0
        
        targets = []
        if cnt % 2 > 0:
            targets.append(cnt/2)
        else:
            targets.append(cnt/2)
            targets.append(cnt/2 - 1)
        ans = []
        indexes = [0 for i in xrange(len(nums))]
        
        heap = []
        for i in xrange(len(nums)):
            j = indexes[i]
            if j < len(nums[i]):
                heapq.heappush(heap, (nums[i][j], i))
                indexes[i] += 1
        
        cnt = 0
        while heap:
            if len(ans) == len(targets):
                break
            n, i = heapq.heappop(heap)
            if cnt in targets:
                ans.append(n)
            j = indexes[i]
            if j < len(nums[i]):
                heapq.heappush(heap, (nums[i][j], i))
                indexes[i] += 1
            cnt += 1
        
        s = sum(ans)
        medium = s * 1.0 / len(ans)
        return medium
        
