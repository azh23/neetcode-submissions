import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(x * x + y * y)

            if len(closest) < k:
                heapq.heappush(closest, (-distance, point))
            elif -closest[0][0] > distance:
                heapq.heappop(closest)
                heapq.heappush(closest, (-distance, point))

        return [item[1] for item in closest]