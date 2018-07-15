"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    
    def __init__(self):
        self.cur = 0
        
    def str2tree(self, s):
        # write your code here
        if not s:
            return None
    
        return self.helper(s)
        
    
    def helper(self, s):

        sign = 1
        if s[self.cur] == "-":
            sign = -1
            self.cur += 1
        num = 0
        
        while self.cur < len(s) and s[self.cur].isdigit():
            num = num * 10 + int(s[self.cur])
            self.cur += 1
        
        root = TreeNode(num * sign)
        if self.cur < len(s) and s[self.cur] == "(":
            self.cur += 1
            root.left = self.helper(s)
        
        if self.cur < len(s) and s[self.cur] == "(":
            self.cur += 1
            root.right = self.helper(s)
        
        if self.cur < len(s) and s[self.cur] == ")":
            self.cur += 1
        
        return root
        
        

