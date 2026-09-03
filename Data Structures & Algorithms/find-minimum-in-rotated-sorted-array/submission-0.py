class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # the pivot is in the right section
            if nums[mid] > nums[right]:
                left = mid + 1
            # the pivot is in the left section
            else:
                right = mid

        return nums[left]
