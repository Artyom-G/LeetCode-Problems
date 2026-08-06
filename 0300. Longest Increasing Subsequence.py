# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Approach: DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] = longest increasing subsequence from 0..i
        # dp[i] = 1 + max{dp[j]} st j < i and nums[j] < nums[i]
        dp = [-1 for i in range(n)]
        dp[0] = 1
        for i in range(n):
            temp = 0
            for j in range(0, i):
                if dp[j] > temp and nums[j] < nums[i]:
                    temp = dp[j]
            dp[i] = 1 + temp
        
        M = 0
        for i in range(n):
            M = max(M, dp[i])
        return M
