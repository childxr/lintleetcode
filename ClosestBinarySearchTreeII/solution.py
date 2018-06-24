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
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def __init__(self):
        self.seq = []
        self.start_index = -1
        self.count = -1

    def closestKValues(self, root, target, k):
        # write your code here
        
        self.helper(root, target)

        if self.start_index < 0:
            return self.seq[len(self.seq)-k:]

        ans = []
        left, right = self.start_index, self.start_index + 1
        for i in xrange(k):
            #if left < 0 and right >= len(self.seq):
            #    break
            if left >= 0 and right < len(self.seq):
                left_diff = abs(self.seq[left] - target)
                right_diff = abs(self.seq[right] - target)
                if left_diff < right_diff:
                    ans.append(self.seq[left])
                    left -= 1
                else:
                    ans.append(self.seq[right])
                    right += 1
            elif left >= 0:
                ans.append(self.seq[left])
                left -= 1
            else:
                ans.append(self.seq[right])
                right += 1
        return ans
        
    def helper(self, root, target):
        if not root:
            return 
        self.helper(root.left, target)
        self.seq.append(root.val)
        self.count += 1

        if root.val >= target and self.start_index == -1:
            self.start_index = self.count
        self.helper(root.right, target)
