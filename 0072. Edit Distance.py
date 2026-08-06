# Time Complexity: O(n*m)
# Space Complexity: O(n*m)
# Approach: 2D DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] edit dist between w1[0..i] and w2[0..j] (one-indexed)
        # insert: s1 = dp[i][j-1] + 1 
        # delete: s2 = dp[i-1][j] + 1 (same as insert on w2) 
        # swap: s3 = dp[i-1][j-1] + 1
        # match: s4 = dp[i-1][j-1] if w1[i]=w2[j]
        # dp[i][j] = min{s1, s2, s3, s4}

        n, m = len(word1), len(word2)
        dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        dp[0][0] = 0 # empty strings match
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if word1[i-1] == word2[j-1]: dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        return dp[n][m]
