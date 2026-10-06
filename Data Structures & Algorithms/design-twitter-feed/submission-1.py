class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.follow(userId, userId) # follow self
        for followeeId in self.follows[userId]:
            if len(self.posts[followeeId]) > 0:
                idx = len(self.posts[followeeId]) - 1
                count, tweetId = self.posts[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx - 1])
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.posts[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
