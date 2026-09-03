class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurred = dict()
        for i, num in enumerate(nums):
            if target - num in occurred:
                return [occurred[target - num], i]

            occurred[num] = i