class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(subset, idx):
            output.append(subset[:])
            for new_idx in range(idx + 1, len(nums)):
                subset.append(nums[new_idx])
                backtrack(subset, new_idx)
                subset.pop()
        backtrack([], -1)
        return output

            