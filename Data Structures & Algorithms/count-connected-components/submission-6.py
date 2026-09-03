from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect = dict()
        nodes = set(range(n))
        for edge in edges:
            if edge[0] not in connect:
                connect[edge[0]] = []
            if edge[1] not in connect:
                connect[edge[1]] =[]
            connect[edge[0]].append(edge[1])
            connect[edge[1]].append(edge[0])
            nodes.discard(edge[0])
            nodes.discard(edge[1])
        print(nodes)
        count = 0
        while connect:
            print(connect)
            q = deque()
            q.append(next(iter(connect)))

            while q:
                current = q.pop()
                if current not in connect:
                    continue
                for neighbor in connect[current]:
                    q.append(neighbor)
                connect.pop(current, None)

            count += 1

        return count + len(nodes)