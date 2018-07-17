"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def __init__(self):
        self.total = 0
        self.allsum = set([])
    def checkEqualTree(self, root):
        # write your code here
        if root is None:
            return False
        self.getSum(root)
        if self.total % 2 != 0:
            return False
        
        return self.total/2 in self.allsum
    
    def getSum(self, root):
        if root is None:
            return 0
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        localSum = left + right + root.val
        self.total += localSum
        self.allsum.add(localSum)
        return localSum
    
        
        
