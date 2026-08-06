# Time Complexity: O(|V|)
# Space Complexity: O(|V|)
# Approach: DP
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0: return 0
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        dp = [[triangle[0][0]]]
        for row in range(1, n):
            dp.append([])
            for col in range(len(triangle[row])):
                val = float("inf")
                if col < len(triangle[row-1]): val = dp[row-1][col]
                if col-1 >= 0: val = min(val, dp[row-1][col-1])
                dp[-1].append(val + triangle[row][col])
            print(dp[row])
        return min(dp[n-1])
