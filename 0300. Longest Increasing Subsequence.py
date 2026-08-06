# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Approach: DP, Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        # dp[i] = longest increasing subsequence from 0..i
        # dp[i] = 1 + max{dp[j]} st j < i and nums[j] < nums[i]
        dp = [-1 for i in range(n)]
        dp[0] = 1

        # Somehow need to keep track of the smallest ending element for each length
        # Smallest element before i for the length k
        # smallest[k] at step i = min{nums[j]} such that j < i and dp[j] = k
        smallest = [float("inf") for i in range(n+1)]
        smallest[1] = nums[0]

        # Go through each element, identify which length it belongs to via bin-search, update smallest[] and dp[]
        res = 0
        for i in range(n):
            # gotta find the correct length, k, could be done with bin search
            l = 1
            h = n
            k = -1
            while l < h:
                k = (l+h)//2
                if smallest[k] >= nums[i]: # m too high
                    h = k
                else: # m too low or just right
                    l = k + 1
            k = l
            
            smallest[k] = min(smallest[k], nums[i])
            dp[i] = k
            res = max(res, k)
        return res



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
