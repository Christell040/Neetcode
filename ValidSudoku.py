from collections import defaultdict

class Solution():
    def validSudoku(self,board):       
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in grid[r//3,c//3]:
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grid[r//3,c//3].add(board[r][c])
        return True
