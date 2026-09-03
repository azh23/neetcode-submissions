class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        merged = [intervals[0]]

        for interval in intervals:
            last_interval = merged[-1]
            if interval[0] <= last_interval[1]:
                last_interval[1] = max(interval[1], last_interval[1])
            else:
                merged.append(interval)

        return merged
