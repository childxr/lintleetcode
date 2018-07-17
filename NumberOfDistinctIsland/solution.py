class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        ans = set([])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    buf = []
                    self.visit(grid, i, j, m, n, buf)
                    self.addIsland(buf, ans)
        
        return len(ans)
    
    def visit(self, grid, i, j, m, n, buf):
        grid[i][j] = 0
        buf.append([i, j])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for k in xrange(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] > 0:
                self.visit(grid, nx, ny, m, n, buf)
    
    def addIsland(self, buf, ans):
        
        def compare(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return a[1] - b[1]
        
        buf.sort(cmp=compare)
        
        code = " ".join(["{} {}".format(buf[i][0]-buf[0][0], buf[i][1]-buf[0][1]) for i in xrange(1, len(buf))])
        #print buf
        #print code
        ans.add(code)
