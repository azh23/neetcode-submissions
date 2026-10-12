class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def backtrack(idx, arr):
            subsets.append(arr[:])

            for i in range(idx + 1, len(nums)):
                if i > idx + 1 and nums[i] == nums[i - 1]:
                    continue

                arr.append(nums[i])
                backtrack(i, arr)
                arr.pop()
        backtrack(-1, [])
        return subsets