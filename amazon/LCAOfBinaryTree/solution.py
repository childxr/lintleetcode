"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
        
    def findNodes(self, root, A, B):
        if root is None:
            return root
        if root == A or root == B:
            return root
        left = self.findNodes(root.left, A, B)
        right = self.findNodes(root.right, A, B)
        if left is not None and right is not None:
            return root
        return left if left is not None else right
        
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return self.findNodes(root, A, B)
        

