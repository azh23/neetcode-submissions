#nums=[-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        sm = 0

        for num in nums:
            if sm < 0:
                sm = 0
            sm += num
            max_sum = max(max_sum, sm)
        return max_sum
