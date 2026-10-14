class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = [n for n in range(n + 1)]

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for a, b in edges:
            parent_a, parent_b = find(a), find(b)
            if parent_a == parent_b:
                return False
            parent[parent_a] = parent_b
        return True
            