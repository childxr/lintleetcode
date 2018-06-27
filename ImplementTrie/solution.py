class TrieNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.alpha_list = [None for i in xrange(256)]
        
class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        cur = self.root
        for ch in word:
            alpha_list = cur.alpha_list
            if alpha_list[ord(ch)] is None:
                alpha_list[ord(ch)] = TrieNode()
            cur = alpha_list[ord(ch)]
        cur.is_word = True
    

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        cur = self.root
        for ch in word:
            alpha_list = cur.alpha_list
            if alpha_list[ord(ch)]:
                cur = alpha_list[ord(ch)]
            else:
                return False
        return cur.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        cur = self.root
        for ch in prefix:
            alpha_list = cur.alpha_list
            if alpha_list[ord(ch)]:
                cur = alpha_list[ord(ch)]
            else:
                return False
        return True

