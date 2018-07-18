class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        m = {}
        for s in strs:
            chs = list(s)
            k = "".join(sorted(chs))
            mp = m.get(k, [])
            mp.append(s)
            m[k] = mp
        
        return m.values()

