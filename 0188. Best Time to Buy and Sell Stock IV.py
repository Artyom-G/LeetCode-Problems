# Time Complexity: O(k*n^2)
# Space Complexity: O(k*n)
# Approach: 2D DP
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0

        # dp[k][i] max profit with k transactions with last sell at i
        # dp[k][i] = for all j<=i-2, j+1 <= j2 <= i-1, max{dp[k-1][j] + prices[i] - prices[j2]}
        dp = [[float("-inf") for i in range(n)] for _k in range(k+1)]
        dp[0][0], dp[1][0] = 0, float("-inf")
        minimum = prices[0]
        res = float("-inf")
        for i in range(1, n):
            dp[0][i] = 0
            dp[1][i] = prices[i] - minimum
            minimum = min(minimum, prices[i])
            res = max(res, dp[1][i], dp[0][i])
        
        #print(dp[0])
        #print(dp[1])
        for t in range(2, k+1):
            earliest_i = t*2-1
            for i in range(earliest_i, n):
                earliest_j = earliest_i - 2
                minimum = float("inf")
                for j in range(i - 2, -1, -1):
                    minimum = min(minimum, prices[j + 1])
                    dp[t][i] = max(dp[t][i], dp[t-1][j] + prices[i] - minimum)
                res = max(res, dp[t][i])
            #print(dp[t], earliest_i)
        return res
