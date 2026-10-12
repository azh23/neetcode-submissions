from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter(t)
        not_covered = len(t)
        left = 0
        right = 0
        res = None

        while right < len(s):
            curr_ch = s[right]
            if curr_ch in counts:
                if counts[curr_ch] > 0:
                    not_covered -= 1
                counts[curr_ch] -= 1

            while not_covered == 0:
                if not res or right - left + 1 < len(res):
                    res = s[left:(right+1)]
                
                if s[left] in counts:
                    counts[s[left]] += 1
                    if counts[s[left]] > 0:
                        not_covered += 1

                left += 1
            right += 1

        return "" if res is None else res