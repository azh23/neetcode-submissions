class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = []
        candidates.sort()

        def traverse(sum, arr, idx):
            if sum == target:
                sums.append(arr[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if sum + candidates[i] > target:
                    break
                arr.append(candidates[i])
                traverse(sum + candidates[i], arr, i + 1)
                arr.pop()

        traverse(0, [], 0)
        return sums