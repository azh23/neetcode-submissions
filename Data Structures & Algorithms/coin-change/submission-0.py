class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf') for _ in range(amount + 1)]

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]