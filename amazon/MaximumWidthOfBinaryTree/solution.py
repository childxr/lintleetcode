"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import Queue
import sys

class Node:
    def __init__(self, root, index):
        self.root = root
        self.index = index

class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree(self, root):
        # Write your code here
        if not root:
            return 0
        queue = Queue.Queue()
        queue.put(Node(root, 0))
        
        ans = 0
        
        while not queue.empty():
            size = queue.qsize()
            minl = sys.maxint
            maxl = 0
            for _ in xrange(size):
                cur = queue.get()
                minl = min(minl, cur.index)
                maxl = max(maxl, cur.index)
                width = maxl - minl + 1
                ans = max(ans, width)
                if cur.root.left:
                    queue.put(Node(cur.root.left, cur.index * 2))
                if cur.root.right:
                    queue.put(Node(cur.root.right, cur.index * 2 + 1))
        
        return ans
                
        
        
