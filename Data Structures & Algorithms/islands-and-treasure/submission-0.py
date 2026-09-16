class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        visited = set(q)
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows and 0 <= nc < cols 
                    and (nr, nc) not in visited 
                    and grid[nr][nc] != -1):
                    grid[nr][nc] = grid[r][c] + 1
                    visited.add((nr, nc))
                    q.append((nr, nc))