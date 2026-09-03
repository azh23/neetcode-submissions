class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def consume(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            consume(r-1,c)
            consume(r+1,c)
            consume(r,c-1)
            consume(r,c+1)

        num = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    print(row,col)
                    for row_pr in grid:
                        print(row_pr)
                    consume(row,col)
                    num += 1
                    print()

        return num
