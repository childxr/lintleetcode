class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        m = len(grid)
        if m == 0:
            return 0
        
        n = len(grid[0])
        if n == 0:
            return 0
        print "m = {} n = {}".format(m, n)
        ans = set([])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    buf = []
                    self.dfs(grid, i, j, buf)
                    ans.add(self.getcode(buf, m, n))
        
        return len(ans)
    
    def dfs(self, grid, i, j, buf):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        grid[i][j] = 0
        buf.append([i, j])
        for k in xrange(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] > 0:
                self.dfs(grid, nx, ny, buf)
                
    def getcode(self, buf, m , n):
        def cm(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return a[1] - b[1]
        

        tmp = [[] for _ in xrange(8)]
        
        for b in buf:
            tmp[0].append(b)
            tmp[1].append([m-1-b[0], b[1]])
            tmp[2].append([b[0], n-1-b[1]])
            tmp[3].append([m-1-b[0], n-1-b[1]])
            tmp[4].append([b[1], b[0]])
            tmp[5].append([n-1-b[1], b[0]])
            tmp[6].append([b[1], m-1-b[0]])
            tmp[7].append([n-1-b[1], m-1-b[0]])
        
        ans = []
        
        for t in tmp:
            code = ""
            t.sort(cmp=cm)
            code += " ".join( ["{} {}".format(t[i][0]-t[0][0], t[i][1]-t[0][1]) for i in xrange(1, len(t))])
            ans.append(code)
        
        ans.sort()
        return ans[0]
            

