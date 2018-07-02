import Queue

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if not board or not board[0]:
            return board
            
        r = len(board)
        c = len(board[0])
        
        for i in xrange(c):
            self.visit(board, 0, i)
            self.visit(board, r-1, i)
        
        for i in xrange(r):
            self.visit(board, i, 0)
            self.visit(board, i, c-1)
        
        for i in xrange(r):
            for j in xrange(c):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def visit(self, board, r, c):
        if board[r][c] != 'O':
            return 
        queue = Queue.Queue()
        queue.put((r, c))
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while not queue.empty():
            cur_r, cur_c = queue.get()
            board[cur_r][cur_c] = 'E'
            for i in xrange(4):
                next_r = cur_r + dx[i]
                next_c = cur_c + dy[i]
                if next_r >= 0 and next_r < len(board) and next_c >= 0 and next_c < len(board[0]) and board[next_r][next_c] == 'O':
                    queue.put((next_r, next_c))
