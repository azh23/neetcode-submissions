class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(n):
            num = 0
            while n != 0:
                num += (n % 10) * (n % 10)
                n //= 10
            return num
        cycle = set()

        while n not in cycle:
            if n == 1:
                return True
            cycle.add(n)
            n = calc(n)

        return False
