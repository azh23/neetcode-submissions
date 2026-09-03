"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        if len(intervals) < 2:
            return True

        for i in range(len(intervals) - 1):
            curr = intervals[i]
            next = intervals[i + 1]
            if next.start < curr.end:
                return False
        return True