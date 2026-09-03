import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(rate):
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / rate)
                if curr_h > h:
                    return False
            return True
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            can_eat = eat(mid)
            if can_eat:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
                