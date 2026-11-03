from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rot.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        mins = 0
        while rot and fresh:
            mins += 1
            to_rot = len(rot)
            for _ in range(len(rot)):
                r, c = rot.popleft()
                di = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for r_add, c_add in di:
                    r_new, c_new = r + r_add, c + c_add
                    if not 0 <= r_new < rows or not 0 <= c_new < cols:
                        continue
                    if grid[r_new][c_new] == 1:
                        fresh -= 1
                        grid[r_new][c_new] = 2
                        rot.append((r_new, c_new))
        return mins if fresh == 0 else -1
