# Time Complexity: O(n)
# Space Complexity: O(n) but could be made O(1)
# Approach: DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        if n == 3: return max(nums[0], nums[1], nums[2])

        # dp[i] most money stollen with ith being the last house
        # dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        dp_wo_1 = [0 for i in range(n)]
        dp_wo_1[0], dp_wo_1[1], dp_wo_1[2] = 0, nums[1], nums[2]
        dp_w_1 = [0 for i in range(n)]
        dp_w_1[0], dp_w_1[1], dp_w_1[2] = nums[0], nums[1], nums[2] + nums[0]
        for i in range(2, n):
            dp_wo_1[i] = max(dp_wo_1[i-2], dp_wo_1[i-3]) + nums[i]
            dp_w_1[i] = max(dp_w_1[i-2], dp_w_1[i-3]) + nums[i]
        return max(dp_wo_1[n-1], dp_wo_1[n-2], dp_w_1[n-2], dp_w_1[n-3])
