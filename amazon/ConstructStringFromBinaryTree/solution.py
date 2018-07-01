"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        ans = []
        self.helper(t, ans)
        return "".join(ans)
        
    def helper(self, t, buf):
        if t == None:
            return
        if t.left is None and t.right is None:
            buf.append(str(t.val))
            return
        if t.right is None:
            buf.append(str(t.val))
            buf.append("(")
            self.helper(t.left, buf)
            buf.append(")")
        elif t.left is None:
            buf.append(str(t.val))
            buf.append("(")
            buf.append(")")
            buf.append("(")
            self.helper(t.right, buf)
            buf.append(")")
        else:
            buf.append(str(t.val))
            buf.append("(")
            self.helper(t.left, buf)
            buf.append(")")
            buf.append("(")
            self.helper(t.right, buf)
            buf.append(")")
            
        
        
