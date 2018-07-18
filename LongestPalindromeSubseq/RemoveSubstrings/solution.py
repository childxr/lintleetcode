import Queue
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        if not s:
            return 0
        visited = set([])
        queue = Queue.Queue()
        visited.add(s)
        ans = len(s)
        queue.put(s)
        
        while not queue.empty():
            cur = queue.get()
            ans = min(ans, len(cur))
            for st in dict:
                start = 0
                idx = cur.find(st, start)
                while idx != -1:
                    nx = cur[0: idx] + cur[idx+len(st):]
                    #print nx
                    #print "***"
                    if nx in visited:
                        break
                    queue.put(nx)
                    visited.add(nx)
                    start = idx + 1
                    idx = cur.find(st, start)
                    
        return ans

