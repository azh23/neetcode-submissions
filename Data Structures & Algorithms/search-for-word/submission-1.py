class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[idx]:
                return False
            
            saved = board[r][c]
            board[r][c]="#"
            res = backtrack(r+1,c,idx+1) or backtrack(r-1,c,idx+1) or backtrack(r,c+1,idx+1) or backtrack(r,c-1,idx+1)
            board[r][c]=saved
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True
        return False
