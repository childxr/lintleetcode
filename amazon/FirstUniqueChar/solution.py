class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        m = [0 for _ in xrange(256)]
        for s in str:
            m[ord(s)] += 1
        ans = None
        for s in str:
            if m[ord(s)] == 1:
                ans = s
                break
        return ans

