class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrences = {char: index for index, char in enumerate(s)}
        i = 0
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_occurrences[c])
            if i == end:
                res.append(size)
                size = 0
        return res
