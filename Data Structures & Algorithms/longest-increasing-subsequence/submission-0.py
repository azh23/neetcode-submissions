class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        sequence = []

        for num in nums:
            if not sequence or sequence[-1] < num:
                sequence.append(num)
            else:
                idx = binary_search(sequence, num)
                sequence[idx] = num

        return len(sequence)


        