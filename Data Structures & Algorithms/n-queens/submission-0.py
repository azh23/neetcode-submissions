import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pdiag, ndiag, res = set(), set(), set(), []
        grid = [["."] * n for _ in range(n)] 
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in grid])
            for c in range(n):
                if c not in cols and r + c not in pdiag and r - c not in ndiag:
                    cols.add(c)
                    pdiag.add(r + c)
                    ndiag.add(r - c)
                    grid[r][c] = "Q"
                    backtrack(r + 1)
                    grid[r][c] = "."
                    cols.remove(c)
                    pdiag.remove(r + c)
                    ndiag.remove(r - c)
        backtrack(0)
        return res

