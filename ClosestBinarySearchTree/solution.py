"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def __init__(self):
        self.closest = None
        self.min_diff = None
    
    def closestValue(self, root, target):
        # write your code here
        self.closest = root.val
        self.min_diff = abs(root.val - target)
        self.helper(root, target)
        return self.closest
    
    def helper(self, root, target):
        if not root:
            return
        if root.val == target:
            self.closest = root.val
            self.min_diff = 0
            return
        
        diff = abs(root.val - target)
        if diff < self.min_diff:
            self.min_diff = diff
            self.closest = root.val
        if root.val < target:
            self.helper(root.right, target)
        else:
            self.helper(root.left, target)
            
        
