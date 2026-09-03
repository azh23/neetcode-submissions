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

"""
def isHappy(self, n: int) -> bool:
    def calc(x):
        return sum(int(d)**2 for d in str(x))
    
    slow, fast = n, calc(n)
    while fast != 1 and slow != fast:
        slow = calc(slow)
        fast = calc(calc(fast))
    return fast == 1
"""
