class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ln = 0

        for num in st:
            if (num - 1) not in st:
                curr_ln = 1
                while (num + curr_ln) in st:
                    curr_ln += 1
                ln = max(ln,curr_ln)

        return ln