"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
import Queue
class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def __init__(self):
        self.pmap = {}

    def helper(self, root, k, parent):
        if root is None:
            return None
        self.pmap[root] = parent
        if root.val == k:
            return root
        left = self.helper(root.left, k, root)
        if left:
            return left
        right = self.helper(root.right, k, root)
        if right:
            return right
        
    
    def findClosestLeaf(self, root, k):
        # Write your code here
        target = self.helper(root, k, None)
        node = self.bfs(target)
        return node.val if node else -1

    def bfs(self, root):
        if root.left is None and root.right is None:
            return root
        
        queue = Queue.Queue()
        queue.put(root)
        visited = set([])
        visited.add(root)
        
        while not queue.empty():
            size = queue.qsize()
            for i in xrange(size):
                cur = queue.get()
                if cur.left is None and cur.right is None:
                    return cur
                if cur.left and cur.left not in visited:
                    queue.put(cur.left)
                    visited.add(cur.left)
                if cur.right and cur.right not in visited:
                    queue.put(cur.right)
                    visited.add(cur.right)
                if self.pmap.get(cur) and self.pmap[cur] not in visited:
                    queue.put(self.pmap[cur])
                    visited.add(self.pmap[cur])
        
        return None
                    
        
        
        
        
