import Queue

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    
    
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        cnt = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 1:
                    cnt += 1
                    self.visit(grid, i, j, row, col)
                    
        return cnt
        
    def visit(self, grid, i, j, row, col):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        grid[i][j] = -1
        queue = Queue.Queue()
        queue.put((i, j))
        while not queue.empty():
            cur_x, cur_y = queue.get()
            for n in xrange(len(dx)):
                next_x, next_y = dx[n] + cur_x, dy[n] + cur_y
                if next_x < 0 or next_x >= row or next_y < 0 or next_y >= col:
                    continue
                if grid[next_x][next_y] == 1:
                    grid[next_x][next_y] = -1
                    queue.put((next_x, next_y))
        
