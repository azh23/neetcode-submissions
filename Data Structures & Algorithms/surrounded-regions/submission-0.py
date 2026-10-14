class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def safe(r, c):
            board[r][c] = "S"

            if r > 0 and board[r-1][c] == "O": safe(r-1, c)
            if c > 0 and board[r][c-1] == "O": safe(r, c-1)
            if r < len(board) - 1 and board[r+1][c] == "O": safe(r+1, c)
            if c < len(board[0]) - 1 and board[r][c+1] == "O": safe(r, c+1)
        
        for c in range(len(board[0])):
            if board[0][c] == "O":
                safe(0, c)
            if board[-1][c] == "O":
                safe(len(board) - 1, c)

        for r in range(len(board)):
            if board[r][0] == "O":
                safe(r, 0)
            if board[r][-1] == "O":
                safe(r, len(board[0]) - 1)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'