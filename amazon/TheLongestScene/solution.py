class UnionFind:
    def __init__(self):
        self.ids = [i for i in xrange(26)]
        self.size = [1 for _ in xrange(26)]
    
    def root(self, a):
        while a != self.ids[a]:
            self.ids[a] = self.ids[self.ids[a]]
            a = self.ids[a]
        return a
    
    def connected(self, p, q):
        pid = self.root(p)
        qid = self.root(q)
        return pid == qid
    
    def connect(self, p, q):
        pid = self.root(p)
        qid = self.root(q)
        if pid != qid:
            if self.size[pid] < self.size[qid]:
                self.ids[pid] = qid
                self.size[qid] += self.size[pid]
            else:
                self.ids[qid] = pid
                self.size[pid] += self.size[qid]
    
class Solution:
    """
    @param str: The scene string
    @return: Return the length longest scene
    """
    def getLongestScene(self, str):
        # Write your code here
        if not str:
            return 0
        
        last = [-1 for _ in xrange(26)]
        
        i = 0
        uf = UnionFind()
        while i < len(str):
            od = ord(str[i]) - ord('a')
            if last[od] != -1:
                start = last[od] + 1
                for j in xrange(start, i):
                    c_od = ord(str[j]) - ord('a')
                    uf.connect(od, c_od)
            last[od] = i
            i += 1

        ans = 1
        start = 0
        end = 1
        while end < len(str):
            start_od = ord(str[start]) - ord('a')
            end_od = ord(str[end]) - ord('a')
            if not uf.connected(start_od, end_od):
                ans = max(ans, end-start)
                start = end
            end += 1
        ans = max(ans, len(str)-start)
        
        return ans
