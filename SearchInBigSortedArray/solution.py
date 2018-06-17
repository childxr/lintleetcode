class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 1
        while reader.get(index-1) < target:
            index *= 2
        
        left, right = 0, index - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1