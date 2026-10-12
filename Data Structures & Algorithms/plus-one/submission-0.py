class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits) - 1, -1, -1):
            new = digits[idx] + 1
            digits[idx] = new % 10
            if new != 10:
                return digits
        return [1] + digits