# Time Complexity: O(k*n)
# Space Complexity: O(k*n)
# Approach: 2D DP
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # dp[t][i] = max profit with at most t transactions
        # using days 0..i
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]

        for t in range(1, k + 1):
            best = -prices[0]

            for i in range(1, n):
                # Either don't sell today,
                # or buy earlier and sell today.
                dp[t][i] = max(dp[t][i - 1], best + prices[i])
                best = max(best, dp[t - 1][i] - prices[i])
        return dp[k][n - 1]


# Time Complexity: O(k*n^2) (barely Time Limit Exceeded)
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

        for t in range(2, k+1):
            earliest_i = t*2-1
            for i in range(earliest_i, n):
                earliest_j = earliest_i - 2
                minimum = float("inf")
                for j in range(i - 2, -1, -1):
                    minimum = min(minimum, prices[j + 1])
                    dp[t][i] = max(dp[t][i], dp[t-1][j] + prices[i] - minimum)
                res = max(res, dp[t][i])
        return res
