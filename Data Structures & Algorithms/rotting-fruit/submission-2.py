from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rot = deque()

        def rot_orange(r, c, mins):
            nonlocal fresh, rot
            if grid[r][c] == 1:
                fresh -= 1
                grid[r][c] = 2
                rot.append((r, c, mins + 1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rot.append((r,c,0))
        minutes = 0
        while rot:
            r, c, mins = rot.popleft()
            minutes=mins

            if r > 0: rot_orange(r-1, c, mins)
            if c > 0: rot_orange(r, c-1, mins)
            if r < len(grid) - 1: rot_orange(r+1, c, mins)
            if c < len(grid[0]) - 1: rot_orange(r, c + 1, mins)

        return -1 if fresh != 0 else minutes

