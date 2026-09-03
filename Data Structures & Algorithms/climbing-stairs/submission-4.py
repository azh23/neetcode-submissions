class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        memo = [0 for _ in range(n)]
        memo[0] = 1
        memo[1] = 2

        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[-1]

"""
def climbStairs(n, memo={}):
    if n <= 1: return 1
    if n in memo: return memo[n]
    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)
    return memo[n]
"""