class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        
        m = len(board)
        if not m:
            return False
            
        n = len(board[0])
        if not n:
            return False
            
        for i in xrange(m):
            for j in xrange(n):
                ans = self.find(board, word, i, j, 0)
                if ans:
                    return ans
        
        return False
        
    def find(self, board, word, r, c, index):
        if index == len(word):
            return True
        
        m, n = len(board), len(board[0])
        
        if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[index]:
            return False
        
        tmp, board[r][c] = board[r][c], '#'
        
        ans = self.find(board, word, r-1, c, index+1) or self.find(board, word, r, c-1, index+1) or self.find(board, word, r+1, c, index+1) or self.find(board, word, r, c+1, index+1)
        board[r][c] = tmp
        
        return ans

