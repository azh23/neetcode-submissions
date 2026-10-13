class Solution:
    def jump(self, nums: List[int]) -> int:
        idx = 0
        steps = 0
        while idx < len(nums) - 1:
            steps += 1
            if idx + nums[idx] >= len(nums) - 1:
                break
            best_jump = [idx,idx]
            for i in range(nums[idx]):
                curr_jump = idx + i + 1
                best_jump = max([nums[curr_jump] + curr_jump, curr_jump], best_jump)
            idx = best_jump[1]
        return steps
# idx = 0
# steps = 1
# check if 0 + 2 >= 5
# best_jump = (0, 0)
# for i in range(2)
# check idx 1 & 2
# best jump => [4, 1] or [1, 2]
# idx = 1
# steps = 2
# 