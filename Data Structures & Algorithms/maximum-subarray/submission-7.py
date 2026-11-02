#nums=[-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        max_sum = -float('inf')
        sm = 0

        for right in range(len(nums)):
            sm += nums[right]
            max_sum = max(sm, max_sum)
            if sm < 0:
                left = right
                sm = 0
        return max_sum
