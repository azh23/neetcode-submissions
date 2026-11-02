from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        sm = 0
        subarrays = 0

        for num in nums:
            sm += num
            if sm - k in sums:
                subarrays += sums[sm - k]
            sums[sm] += 1
        print(sums)
        return subarrays