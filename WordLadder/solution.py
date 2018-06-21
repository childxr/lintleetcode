import collections

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        word_len = len(start)
        queue = collections.deque([(start, 1)])
        
        while queue:
            cur_word, path_len = queue.popleft()
            if cur_word == end:
                return path_len
            for i in xrange(word_len):
                p1 = cur_word[:i]
                p2 = cur_word[i+1:]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch != cur_word[i]:
                        new_word = p1 + ch + p2
                        if new_word in dict:
                            queue.append((new_word, path_len + 1))
                            dict.remove(new_word)
        
        return 0
