class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        n = len(words)
        if n == 0:
            return True
        
        for word in words:
            if len(word) != n:
                return False
            
        for i in xrange(n):
            for j in xrange(i, n):
                if words[i][j] != words[j][i]:
                    return False
        
        return True
                
