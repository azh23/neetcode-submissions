class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        xor = (a ^ b) & mask
        carry = ((a & b) << 1) & mask

        while carry:
            new = (xor ^ carry) & mask
            carry = ((xor & carry) << 1) & mask
            xor = new

        return xor if xor <= 0x7FFFFFFF else ~(xor ^ mask)