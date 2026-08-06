# Time Complexity: O(n*m) = O(|V|)
# Space Complexity: O(n*m) = O(|V|)
# Approach: DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        dp = [[-1 for j in range(m)] for i in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                val = float("inf")
                if i-1 >= 0: val = dp[i-1][j]
                if j-1 >= 0: val = min(val, dp[i][j-1])
                dp[i][j] = val + grid[i][j]
            
        return dp[n-1][m-1]
