import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []

        for num in nums:
            if len(hp) < k:
                heapq.heappush(hp, num)
            elif num > hp[0]:
                heapq.heappush(hp, num)
                heapq.heappop(hp)

        return hp[0]