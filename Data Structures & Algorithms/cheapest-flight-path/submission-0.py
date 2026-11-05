from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp = dist.copy()
            for frm, to, price in flights:
                if dist[frm] == float('inf'):
                    continue
                if dist[frm] + price < tmp[to]:
                    tmp[to] = dist[frm] + price
            dist = tmp
        return dist[dst] if dist[dst] != float('inf') else -1