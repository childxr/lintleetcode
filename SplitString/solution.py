import copy

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    
    def __init__(self):
        self.ans = []
        

    def splitString(self, s):
        # write your code here
        self.helper(s, [])
        return self.ans
    
    def helper(self, s, buf):
        if not s:
            self.ans.append(buf)
            return
        cur1 = copy.deepcopy(buf)
        cur1.append(s[:1])
        self.helper(s[1:], cur1)
        if len(s) > 1:
            cur2 = copy.deepcopy(buf)
            cur2.append(s[:2])
            self.helper(s[2:], cur2)
        
        
        
        
