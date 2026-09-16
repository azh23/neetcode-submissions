class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target = Counter(s1)
        left = 0
        right = len(s1)
        curr = Counter(s2[left:right])

        while right < len(s2):
            print(target,curr)
            if target == curr:
                return True
            
            curr[s2[left]] -= 1
            if curr[s2[left]] == 0:
                del curr[s2[left]]
            curr[s2[right]] = curr.get(s2[right], 0) + 1
            left += 1
            right += 1
        return target == curr
            


