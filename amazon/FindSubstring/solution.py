class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        # Write your code here
        if len(str) < k:
            return 0
        i = 0
        m = [0 for _ in xrange(256)]
        sub = {}
        rp = 0
        while i < k:
            cur = str[i]
            m[ord(cur)] += 1
            if m[ord(cur)] > 1:
                rp += 1
            i += 1
        if rp == 0:
            sub[str[0:k]] = 1
        while i < len(str):
            m[ord(str[i])] += 1
            m[ord(str[i-k])] -= 1
            if str[i] != str[i-k]:
                if m[ord(str[i])] > 1:
                    rp += 1
                if m[ord(str[i-k])] >= 1:
                    rp -= 1
            if rp == 0:
                sub[str[i-k+1:i+1]] = 1
            i += 1
        
        return len(sub)
            
