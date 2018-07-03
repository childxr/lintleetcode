class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def indexOf(self, ch):
        return ord(ch)

    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s:
            return 0
        
        left, right = -1, 0
        m = [0 for i in xrange(256)]
        violate = 0
        ans = 0
        while right < len(s):
            m[self.indexOf(s[right])] += 1
            if m[self.indexOf(s[right])] > 1:
                violate += 1
                ans = max(ans, right-1-left)
                while True:
                    left += 1
                    m[self.indexOf(s[left])] -= 1
                    if m[self.indexOf(s[left])] == 1:
                        violate -= 1
                        break
            right += 1
        
        ans = max(ans, right - 1 - left)
        return ans
            

