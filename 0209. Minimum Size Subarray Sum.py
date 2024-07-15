#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = len(nums)+1
        L = 0
        R = 0
        S = nums[L]
        while R < len(nums):
            if S >= target:
                m = R - L + 1
                S -= nums[L]
                L += 1
            if S < target:
                R += 1
                if R < len(nums): S += nums[R]
                if R - L + 1 > m:
                    S -= nums[L]
                    L += 1
        if m > len(nums):
            return 0
        return m
                
