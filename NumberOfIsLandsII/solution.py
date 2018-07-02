class UnionFind:
    
    def __init__(self, n, m):
        self.m = m
        self.n = n
        self.ids = [-1 for i in xrange(m * n)]
        self.sz = [0 for i in xrange(m * n)]
        self.count = 0
    
    def indexOf(self, point):
        return point.x * self.m + point.y
    
    def add(self, point):
        index = self.indexOf(point)
        if self.ids[index] == -1:
            self.ids[index] = index
            self.sz[index] = 1
            self.count += 1
    
    def isConnectedComponent(self, point):
        index = self.indexOf(point)
        return self.ids[index] != -1
    
    def isConnected(self, p1, p2):
        # consider connect, is connected
        p1_index = self.indexOf(p1)
        p2_index = self.indexOf(p2)
        p1_root = self.root(p1_index)
        p2_root = self.root(p2_index)
        return p1_root == p2_root
    
    def root(self, a):
        while self.ids[a] != a:
            self.ids[a] = self.ids[self.ids[a]]
            a = self.ids[a]
        return a
        
    def connect(self, p1, p2):
        p1_index = self.indexOf(p1)
        p2_index = self.indexOf(p2)
        p1_root = self.root(p1_index)
        p2_root = self.root(p2_index)
        
        if p1_root == p2_root:
            return
        
        if self.sz[p1_root] < self.sz[p2_root]:
            self.ids[p1_root] = p2_root
            self.sz[p2_root] += self.sz[p1_root]
        else:
            self.ids[p2_root] = p1_root
            self.sz[p1_root] += self.sz[p2_root]
    
        self.count -= 1

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    
    def numIslands2(self, n, m, operators):
        # write your code here
        if n == 0 or m == 0:
            return []
        unionfind = UnionFind(n, m)
        ans = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visited = set([])
        
        for operator in operators:
            unionfind.add(operator)
            for i in xrange(4):
                nx = operator.x + dx[i]
                ny = operator.y + dy[i]
                point = Point(nx, ny)
                if nx >= 0 and nx < n and ny >= 0 and ny < m and unionfind.isConnectedComponent(point):
                    if not unionfind.isConnected(operator, point):
                        unionfind.connect(operator, point)
            ans.append(unionfind.count)
    
        return ans
