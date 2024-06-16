#Time Complexity: O(n^2)
#Space Complexity: O(n) but could even be O(1) if different sort is used
#Approach: 2 Pointer, Two-Sum
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 999999999
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                S = nums[i] + nums[j] + nums[k]
                if S < target:
                    j+=1
                elif S > target:
                    k -= 1
                else:
                    return target
                if abs(closest - target) > abs(S - target):
                    closest = S
        return closest
                
