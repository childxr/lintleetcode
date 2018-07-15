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
    @return: a list of integer
    """
    def __init__(self):
        self.ans = []
    
    def leftBoundary(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        self.ans.append(root.val)
        if root.left is None:
            self.leftBoundary(root.right)
        else:
            self.leftBoundary(root.left)
    
    def rightBoundary(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        if root.right is None:
            self.rightBoundary(root.left)
        else:
            self.rightBoundary(root.right)
        self.ans.append(root.val)
    
    def leaves(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.ans.append(root.val)
            return
        self.leaves(root.left)
        self.leaves(root.right)
        
    def boundaryOfBinaryTree(self, root):
        # write your code here
        if not root:
            return []
        self.ans.append(root.val)
        self.leftBoundary(root.left)
        self.leaves(root.left)
        self.leaves(root.right)
        self.rightBoundary(root.right)
        return self.ans
        
