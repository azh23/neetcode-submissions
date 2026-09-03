class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        removals = 0
        latest_end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= latest_end:
                latest_end = interval[1]
            else:
                removals += 1

        return removals