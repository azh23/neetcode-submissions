class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(bucket_idx, current_sum, start_idx):
            if bucket_idx == k:
                return True
            if current_sum == target:
                return backtrack(bucket_idx + 1, 0, 0)

            for i in range(start_idx, len(nums)):
                if used[i] or current_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(bucket_idx, current_sum + nums[i], i + 1):
                    return True
                used[i] = False
                if current_sum == 0:  # this number failed as a fresh bucket's first pick — no bucket works
                    break

            return False

        return backtrack(0, 0, 0)