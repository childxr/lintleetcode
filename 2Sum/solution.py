class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return []
        visited = {nums[0]: [0]}
        for i in xrange(1, len(nums)):
            if target - nums[i] in visited.keys():
                return [visited[target-nums[i]][0] + 1, i + 1]
            if not visited.has_key(nums[i]):
                visited[nums[i]] = [i]
            else:
                visited[nums[i]].append(i)
        return []
                

