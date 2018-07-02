class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = [None for i in xrange(26)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        if not word:
            return
        self.add_word_handler(word, 0, self.root)
    
    def add_word_handler(self, word, index, cur):
        if index == len(word):
            cur.word = word
        else:
            char = word[index]
            char_index = ord(char) - ord('a')
            char_node = cur.children[char_index]
            if not char_node:
                cur.children[char_index] = TrieNode()
                char_node = cur.children[char_index]
            self.add_word_handler(word, index+1, char_node)
    
    def wordSearchII(self, board, words):
        # write your code here
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        if n == 0:
            return []
            
        for word in words:
            self.add_word(word)
        
        ans = set([])
        for i in xrange(m):
            for j in xrange(n):
                self.search(board, i, j, ans, self.root)
        
        return list(ans)
    
    def search(self, board, i, j, ans, cur):
        
        if not cur:
            return
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == '#':
            return
        
        char = board[i][j]
        char_index = ord(char) - ord('a')
        child = cur.children[char_index]
        if child and child.word:
            ans.add(child.word)
        # dad and daddy are both valid words, so continue search even if we found a word
        
        tmp, board[i][j] = board[i][j], '#'
        
        res = self.search(board, i+1, j, ans, child) or self.search(board, i, j+1, ans, child) or self.search(board, i-1, j, ans, child) or self.search(board, i, j-1, ans, child)
        
        board[i][j] = tmp
        

