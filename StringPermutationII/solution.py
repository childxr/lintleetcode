class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def __init__(self):
        self.ans = []
    
    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [str]
        chars = sorted(str)
        #print chars
        self.dfs(chars, 0)
        return sorted(self.ans)
    
    def dfs(self, chars, start_index):
        if start_index == len(chars):
            self.ans.append(''.join(chars))
        else:
            for i in xrange(start_index, len(chars)):
                if self.noswap(start_index, i, chars):
                    continue
                chars[start_index], chars[i] = chars[i], chars[start_index]
                self.dfs(chars, start_index+1)
                chars[start_index], chars[i] = chars[i], chars[start_index]
                
    def noswap(self, start_index, i, chars):
        for j in xrange(start_index, i):
            if chars[j] == chars[i]:
                return True
        return False
                

