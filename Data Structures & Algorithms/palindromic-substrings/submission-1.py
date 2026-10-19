class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [[False] * len(s) for _ in range(len(s))]
        ct = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                    memo[i][j] = True
                    ct += 1

        return ct
"""
class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
"""