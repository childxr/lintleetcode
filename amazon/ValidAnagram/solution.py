class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        a = [0 for _ in xrange(256)]
        b = [0 for _ in xrange(256)]
        for ss in s:
            a[ord(ss)] += 1
        for tt in t:
            b[ord(tt)] += 1
        
        return a == b

