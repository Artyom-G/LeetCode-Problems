# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Approach: DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] = max profit while selling on ith day
        # dp[i] = max(dp[j] + prices[i] - minPrice[j][i]) for 0 <= j < i - 1

        n = len(prices)
        if n < 2: return 0

        minPrices = [[float("inf") for j in range(n)] for i in range(n)]
        for i in range(n):
            m = float("inf")
            for j in range(i, n):
                m = min(m, prices[j])
                minPrices[i][j] = m

        dp = [0 for i in range(n)]
        dp[0] = 0
        maximum = 0
        for i in range(1, n):
            for j in range(0, i):
                dp[i] = max(dp[i], dp[j] + prices[i] - minPrices[j][i])
                #print(dp[i], dp[j], prices[i], minPrices[j][i])
            maximum = max(maximum, dp[i])
        #print(dp)
        return maximum
