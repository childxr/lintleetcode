class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.ids = [i for i in xrange(n+1)]
        self.sz = [1 for i in xrange(n+1)]
        
    def root(self, i):
        while self.ids[i] != i:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i
        
    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)
        if self.sz[pid] < self.sz[qid]:
            self.ids[pid] = qid
            self.sz[qid] += self.sz[pid]
        else:
            self.ids[qid] = pid
            self.sz[pid] += self.sz[qid]
        
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        return self.union(a, b)

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.root(a) == self.root(b)

