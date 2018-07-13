class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverse(self, str, i, j):
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
    
    def reverseWords(self, str):
        # write your code here
        if not str:
            return str
        str = list(str)
        
        self.reverse(str, 0, len(str)-1)
        #print ''.join(str)
        left, right = 0, 0
        while True:
            if right == len(str):
                self.reverse(str, left, right-1)
                break
            if str[right] != ' ':
                right += 1
                continue
            self.reverse(str, left, right-1)
            right += 1
            left = right
        
        return ''.join(str)
        
        
