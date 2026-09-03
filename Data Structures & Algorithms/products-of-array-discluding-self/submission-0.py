class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        pf = 1
        sf = 1
        for i, num in enumerate(nums):
            prefix[i] = pf
            pf *= num

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            suffix[i] = sf
            sf *= num

        return [prefix[i] * suffix[i] for i in range(len(nums))]
        