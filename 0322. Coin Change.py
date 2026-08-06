# Time Complexity: O(nk)
# Space Complexity: O(nk)
# Approach: 2D DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        # dp[k][i] is the min coins[0..i] required to get a value k
        # dp[k][i] = min{dp[k][i-1], dp[k-a_i][i-1]+1}
        m = min(coins)
        n = len(coins)
        dp = [[float("inf") for i in range(n)] for k in range(amount+1)]
        for k in range(amount+1):
            if k == 0: dp[0] = [0 for i in range(n)]
            if k < m:
                continue
            for i in range(n):
                if coins[i] == k: dp[k][i] = 1
                if k-coins[i] < 0: 
                    dp[k][i] = dp[k][i-1]
                else:
                    dp[k][i] = min(dp[k][i-1], dp[k-coins[i]][n-1] + 1)
        if dp[amount][n-1] == float("inf"): return -1
        return dp[amount][n-1]
