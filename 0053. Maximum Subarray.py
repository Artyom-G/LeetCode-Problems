# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        # dp[i] largest subarray sum ending at i
        # dp[i] = max(dp[i-1] + nums[i], nums[i]), we only need to keep track of dp[i-1]
        prev, res = nums[0], nums[0]
        for num in nums[1:]:
            prev = max(prev + num, num)
            res = max(res, prev)
        return res
