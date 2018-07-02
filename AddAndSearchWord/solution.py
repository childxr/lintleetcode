class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None for i in xrange(26)]

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        # write your code here
        self.addWordHelper(word, 0, self.root)
        
    def addWordHelper(self, word, index, cur):
        if index == len(word):
            cur.is_word = True
        else:
            char = word[index]
            char_index = ord(char) - ord('a')
            cur_node = cur.children[char_index]
            if not cur_node:
                cur.children[char_index] = TrieNode()
                cur_node = cur.children[char_index]
            self.addWordHelper(word, index+1, cur_node)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        if not word:
            return False
        return self.searchHelper(word, 0, self.root)
        
    def searchHelper(self, word, index, cur):
        if not cur:
            return False
        if index == len(word):
            return cur.is_word
        else:
            char = word[index]
            if char == '.':
                rs = False
                for i in xrange(26):
                    rs = self.searchHelper(word, index+1, cur.children[i])
                    if rs:
                        break
                return rs
            else:
                char_index = ord(char) - ord('a')
                char_node = cur.children[char_index]
                return self.searchHelper(word, index+1, char_node)

