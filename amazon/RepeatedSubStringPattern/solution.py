class Solution:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeatedSubstringPattern(self, s):
        # write your code here
        
        if len(s) % 2 > 0:
            return False
        
        high = len(s)/2
        cur = high
        while cur > 0:
            if len(s) % cur == 0:
                pat = s[:cur]
                ok = True
                for j in xrange(cur, len(s), cur):
                    if s[j: j+cur] != pat:
                        ok = False
                        break
                if ok:
                    return True
            cur -= 1
        
        return False

