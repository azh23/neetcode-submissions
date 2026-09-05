class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        counts = dict()
        maxf = 0
        ln = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(maxf, counts[s[r]])
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            ln = max(ln, r - l + 1)

        return ln


