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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def __init__(self):
        self.count = 0
        self.ans = None
    
    def kthSmallest(self, root, k):
        # write your code here
        self.helper(root, k)
        return self.ans.val
    
    def helper(self, root, k):
        if not root:
            return
        self.helper(root.left, k)
        self.count += 1
        if self.count == k:
            self.ans = root
        self.helper(root.right, k)
        
        
