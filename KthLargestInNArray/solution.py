import heapq
import sys

class MaxObject:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val
    def __lt__(self, other):
        return self.val > other.val
    def __str__(self):
        return str(self.val)

class MaxHeap:
    def __init__(self):
        self.h = []
    def push(self, val, index):
        heapq.heappush(self.h, (MaxObject(val), index))
    def pop(self):
        item_v, index = heapq.heappop(self.h)
        return item_v.val, index
    def empty(self):
        return len(self.h) == 0
    def size(self):
        return len(self.h)


class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        
        for array in arrays:
            array.sort()
        
        pts = [len(arrays[i])-1 for i in xrange(len(arrays))]
        maxheap = MaxHeap()
        for i, val in enumerate(pts):
            if val >= 0:
                maxheap.push(arrays[i][val], i)
                pts[i] -= 1
        
        count = 0
        val, index = None, None
        while count < k:
            count += 1
            if maxheap.empty():
                sys.exit(1)
            val, index = maxheap.pop()
            if pts[index] >= 0:
                maxheap.push(arrays[index][pts[index]], index)
                pts[index] -= 1
        
        return val
            
                
        
            
        
