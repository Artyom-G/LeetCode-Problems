# Time Complexity: O(n*m) = O(|V|)
# Space Complexity: O(n*m) = O(|V|) (can be done in place for O(1) solution)
# Approach: DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if n == 0: return 0
        m = len(obstacleGrid[0])
        if m == 0: return 0

        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[-1 for j in range(m)] for i in range(n)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                val1 = dp[i-1][j] if i-1 >= 0 and obstacleGrid[i-1][j] != 1 else 0
                val2 = dp[i][j-1] if j-1 >= 0 and obstacleGrid[i][j-1] != 1 else 0
                dp[i][j] = val1 + val2 if obstacleGrid[i][j] != 1 else 0
        return dp[n-1][m-1]
