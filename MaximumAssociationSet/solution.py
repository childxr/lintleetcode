class UnionFind:
    def __init__(self, n):
        self.ids = [i for i in xrange(n)]
        self.size = [1 for _ in xrange(n)]
    
    def root(self, a):
        while self.ids[a] != a:
            self.ids[a] = self.ids[self.ids[a]]
            a = self.ids[a]
        return a
    
    def connect(self, p, q):
        
        pid = self.root(p)
        qid = self.root(q)
        
        if pid != qid:
            if self.size[pid] < self.size[qid]:
                self.size[qid] += self.size[pid]
                self.ids[pid] = qid
            else:
                self.size[pid] += self.size[qid]
                self.ids[qid] = pid
    
    def isConnected(self, p, q):
        return self.root(p) == self.root(q)
    
    def getLargestComponent(self):
        maxSize = 0
        maxID = -1
        for i in xrange(len(self.size)):
            if self.ids[i] == i:
                if self.size[i] > maxSize:
                    maxSize = self.size[i]
                    maxID = i
        
        ans = []
        for i in xrange(len(self.ids)):
            if self.root(i) == maxID:
                ans.append(i)
        
        return ans

        
    
class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        nmap = {}
        rmap = {}
        cnt = 0
        
        for a in ListA:
            if a not in nmap.keys():
                nmap[a] = cnt
                rmap[cnt] = a
                cnt += 1
        
        for b in ListB:
            if b not in nmap.keys():
                nmap[b] = cnt
                rmap[cnt] = b
                cnt += 1
        
        uf = UnionFind(cnt)
        n = len(ListA)

        for i in xrange(n):
            uf.connect(nmap[ListA[i]], nmap[ListB[i]])
        
        l = uf.getLargestComponent()
        return [rmap[i] for i in l]


