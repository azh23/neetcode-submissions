class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        curr = 0
        triplets = []

        # -4 -1 -1 0 1 2 
        for curr in range(len(nums) - 2):
            if curr and nums[curr - 1] == nums[curr]:
                continue
            left = curr + 1
            right = len(nums) - 1
            while left < right:
                sm = nums[curr] + nums[left] + nums[right]
                if sm == 0:
                    triplets.append([nums[curr], nums[left], nums[right]])
                    leftprev = nums[left]
                    rightprev = nums[right]
                    while left < len(nums) - 2 and nums[left] == leftprev:
                        left += 1
                    while right > 1 and nums[right] == rightprev:
                        right -=1
                elif sm < 0:
                    left += 1
                else:
                    right -= 1
        return triplets
