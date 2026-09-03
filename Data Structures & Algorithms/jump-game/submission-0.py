class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_step = 0
        for i, num in enumerate(nums):
            if farthest_step < i:
                return False
            farthest_step = max(farthest_step, i + num)
        return farthest_step >= len(nums) - 1