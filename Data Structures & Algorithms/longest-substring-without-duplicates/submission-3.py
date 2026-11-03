class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = set()
        ln = 0
        for right in range(len(s)):
            if s[right] in chars:
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                left += 1
            chars.add(s[right])
            ln = max(ln, right - left + 1)
        return ln