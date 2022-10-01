class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        
        for coin in coins:
            for i in range(amount+1):
                if coin <= i:
                    dp[i] = min(dp[i],1+dp[i-coin])
        
        if dp[amount] == sys.maxsize:
            return -1
        
        return dp[amount] if dp[amount] != float("inf") else -1