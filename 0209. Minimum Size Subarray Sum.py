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



# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        current_sum = nums[l]
        res = float(inf)
        if(current_sum >= target):
            return 1
        m = 1
        while(l < n):
            #print(nums[l:r+1], m, current_sum, res)
            if(current_sum < target and m < res and r < n-1):
                r+=1
                current_sum += nums[r]
                m+=1
            elif(l < r or r == n-1):
                current_sum -= nums[l]
                l+=1
                m-=1
            else:
                current_sum -= nums[l]
                l+=1
                r+=1
                current_sum += nums[r]
                if(current_sum >= target):
                    return 1
            if(current_sum >= target):
                res = min(m, res)
        if(res == float(inf)):
            return 0
        return res
