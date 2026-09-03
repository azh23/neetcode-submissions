class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        size = 0
        max_area = 0
        def consume(r, c):
            nonlocal size
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            size += 1
            if r > 0: consume(r - 1, c)
            if r < len(grid) - 1: consume(r + 1, c)
            if c > 0: consume(r, c - 1)
            if c < len(grid[0]) - 1: consume(r, c+ 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = 0
                consume(r,c)
                max_area = max(max_area, size)
        
        return max_area

