class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        longest = 0

        while right < len(s):
            print(left, right, seen)
            if s[right] in seen:
                longest = max(longest, right - left)
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
                right += 1
            else:
                seen.add(s[right])
                right += 1
        return max(longest, right - left)

        