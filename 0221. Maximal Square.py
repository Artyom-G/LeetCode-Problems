# Time Complexity: O(n*m)
# Space Complexity: O(n*m)
# Approach: 2D DP
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        if n == 0 or m == 0: return 0
        # dp[i][j] largest square ending at (i,j)
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        dp = [[int(matrix[i][j]) if i == 0 or j == 0 else 0 for j in range(m)] for i in range(n)]
        M = 0
        for i in range(0, n):
            for j in range(0, m):
                if i != 0 and j != 0: 
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    if matrix[i][j] == "0": dp[i][j] = 0
                M = max(M, dp[i][j])
        return M*M
