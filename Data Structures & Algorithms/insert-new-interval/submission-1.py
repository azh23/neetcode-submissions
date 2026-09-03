class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        new_intervals = []
        is_added = False
        while idx < len(intervals):
            curr = intervals[idx]
            if curr[1] < newInterval[0]:
                new_intervals.append(curr)
                idx += 1
            elif curr[0] > newInterval[1]:
                if not is_added:
                    new_intervals.append(newInterval)
                    is_added = True
                new_intervals.append(curr)
                idx += 1
            else:
                start = min(curr[0], newInterval[0])
                end = newInterval[1]
                while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
                    end = max(end, intervals[idx][1])
                    idx += 1
                new_intervals.append([start, end])
                is_added = True
        if not is_added:
            new_intervals.append(newInterval)
        return new_intervals
                
                