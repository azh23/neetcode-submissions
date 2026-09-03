class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_street(houses):
            if len(houses) == 1:
                return houses[0]
            dp = [0 for _ in range(len(houses))]
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2,len(houses)):
                dp[i] = max(dp[i-1],dp[i-2]+houses[i])
            
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(rob_street(nums[1:]), rob_street(nums[:-1]))