class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = []
        atlantic = []
        
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        
        def dfs(nodes):
            nonlocal rows, cols
            node_set = set()
            while nodes:
                r,c = nodes.pop()
                node_set.add((r,c))
                val = heights[r][c]
                if r > 0 and (r-1,c) not in node_set and heights[r-1][c] >= val: nodes.append((r-1,c))
                if c > 0 and (r,c-1) not in node_set and heights[r][c-1] >= val: nodes.append((r,c-1))
                if r < rows-1 and (r+1,c) not in node_set and heights[r+1][c] >= val: nodes.append((r+1,c))
                if c < cols-1 and (r,c+1) not in node_set and heights[r][c+1] >= val: nodes.append((r,c+1))
            return node_set

        return list(dfs(pacific) & dfs(atlantic))
        