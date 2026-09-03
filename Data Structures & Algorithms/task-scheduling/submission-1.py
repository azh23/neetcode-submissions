import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = []
        cooldown = deque()
        for task, count in counts.items():
            heapq.heappush(heap, (-count, task))

        time = 0

        while heap or cooldown:
            if cooldown and time - cooldown[0][0] == n + 1:
                _, task_info = cooldown.popleft()
                heapq.heappush(heap, task_info)
            if heap:
                count, task = heapq.heappop(heap)
                if count + 1 != 0:
                    cooldown.append((time, (count + 1, task)))
            time += 1

        return time

        

