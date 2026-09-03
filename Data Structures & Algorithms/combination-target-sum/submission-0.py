class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        combo = []

        def backtrack(idx, sm):
            if sm > target:
                return
            if sm == target:
                sums.append(combo[:])
                return
            for j in range(idx, len(nums)):
                combo.append(nums[j])
                backtrack(j, sm + nums[j])
                combo.pop()
        backtrack(0, 0)
        return sums