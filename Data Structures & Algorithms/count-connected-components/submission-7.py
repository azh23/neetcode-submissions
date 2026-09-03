from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect = dict()
        visited = [False for _ in range(n)]
        for edge in edges:
            if edge[0] not in connect:
                connect[edge[0]] = []
            if edge[1] not in connect:
                connect[edge[1]] =[]
            connect[edge[0]].append(edge[1])
            connect[edge[1]].append(edge[0])

        count = 0
        for i in range(n):
            if visited[i]:
                continue
            count += 1
            if i not in connect:
                continue
            q = deque()
            q.append(i)

            while q:
                current = q.pop()
                if visited[current]:
                    continue
                visited[current] = True
                if current not in connect:
                    continue
                for neighbor in connect[current]:
                    q.append(neighbor)

        return count