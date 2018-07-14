"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: all the values with the highest frequency in any order
    """
    def __init__(self):
        self.m = {}
        
    def subTreeSum(self, root):
        if root is None:
            return 0
        left = self.subTreeSum(root.left)
        right = self.subTreeSum(root.right)
        sm = left + right + root.val
        sv = self.m.get(sm, 0)
        self.m[sm] = sv + 1
        return sm
        
    def findFrequentTreeSum(self, root):
        # Write your code here
        if not root:
            return []
        self.subTreeSum(root)
        max_f = max(self.m.values())
        ans = []
        for k, v in self.m.items():
            if v == max_f:
                ans.append(k)
        return ans
            
        
        
