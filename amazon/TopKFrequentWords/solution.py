import heapq

class minHeap:
    def __init__(self):
        self.h = []
    
    def push(self, item):
        heapq.heappush(self.h, item)
        
    def pop(self):
        return heapq.heappop(self.h)
    
    def size(self):
        return len(self.h)
    
    def empty(self):
        return len(self.h) == 0

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        m = {}
        for word in words:
            f = m.get(word, 0)
            f += 1
            m[word] = f
        mh = minHeap()
        for key, v in m.items():
            mh.push((v, key))
        
        ans = []
        cnt, size = 0, mh.size()
        while cnt < (size - k) and not mh.empty():
            mh.pop()
            cnt += 1
        while not mh.empty():
            ans.append(mh.pop()[-1])
        return ans
            
        
