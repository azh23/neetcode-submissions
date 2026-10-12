from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,t in times:
            edges[u].append((v,t))

        hp = [(0, k)]
        visit = set()
        time = 0

        while hp:
            t, node = heapq.heappop(hp)
            if node in visit:
                continue
            visit.add(node)
            time = t
            for v2, t2 in edges[node]:
                if v2 not in visit:
                    heapq.heappush(hp, (t + t2, v2))

        return time if len(visit) == n else -1