import copy
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    
    def __init__(self):
        self.ans = []
    
    def combine(self, n, k):
        # write your code here
        seq = [x + 1 for x in xrange(n)]
        self.helper(seq, k, [])
        return self.ans
    
    
    def helper(self, seq, k, buf):
        if len(seq) < k:
            return
        if k == 0:
            self.ans.append(buf)
            
        for i in xrange(len(seq)):
            tmp = copy.deepcopy(buf)
            tmp.append(seq[i])
            self.helper(seq[i+1:], k-1, tmp)
        
