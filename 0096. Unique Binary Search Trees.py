# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Approach: DP
class Solution:
    def numTrees(self, n: int) -> int:
        # Notice that given [1..n] (think of each element as a tree with one node), 
        # to make a BST you can take adjacent pairs (there two ways to arrange them) 
        # and collapse them into one (small tree), this can be done repeatedly until a BST is formed 
        # dp[i] number of unique BST of size i
        # dp[i] is pairing i with [j..i-1] trees
        # dp[i] = (dp[i-1]*dp[0]) + (dp[i-2]*dp[1]) + ... + (dp[2]*dp[i-2]) + (dp[0]*dp[i-1])

        dp = [-1] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = 0
            for left_size in range(i):
                right_size = i - 1 - left_size
                dp[i] += dp[left_size] * dp[right_size]
        return dp[n]
        
