"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        # Write your code here
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        return self.helper(t1, t2)
        
    def helper(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        if t1 is not None and t2 is not None:
            cur = TreeNode(t1.val + t2.val)
            cur.left = self.helper(t1.left, t2.left)
            cur.right = self.helper(t1.right, t2.right)
        elif t1 is None:
            cur = TreeNode(t2.val)
            cur.left = self.helper(t1, t2.left)
            cur.right = self.helper(t1, t2.right)
        elif t2 is None:
            cur = TreeNode(t1.val)
            cur.left = self.helper(t1.left, t2)
            cur.right = self.helper(t1.right, t2)
        return cur
            
            
            
            
