import bisect
class TimeMap:

    def __init__(self):
        self.times = {}
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times.setdefault(key, []).append(timestamp)
        self.values.setdefault(key, []).append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        times, values = self.times[key], self.values[key]
        idx = bisect.bisect_right(times, timestamp)
        return values[idx - 1] if idx != 0 else ""
        
"""
from bisect import bisect_right

class BidHistory:
    def __init__(self):
        self.times = {}    # auction_id -> increasing timestamps
        self.amounts = {}  # auction_id -> amounts, same indices

    def record(self, auction_id, timestamp, amount):
        self.times.setdefault(auction_id, []).append(timestamp)
        self.amounts.setdefault(auction_id, []).append(amount)

    def price_at(self, auction_id, timestamp):
        if auction_id not in self.times:
            return -1
        i = bisect_right(self.times[auction_id], timestamp) - 1
        return self.amounts[auction_id][i] if i >= 0 else -1
"""