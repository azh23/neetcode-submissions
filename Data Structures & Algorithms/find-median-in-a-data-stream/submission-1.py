class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            if len(self.small) == 0:
                heapq.heappush(self.small, -num)
            elif num >= self.large[0]:
                heapq.heappush(self.large, num)
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -val)
            else:
                heapq.heappush(self.small, -num)
        else:
            if num > -self.small[0]:
                heapq.heappush(self.large, num)
            else:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]
        
        