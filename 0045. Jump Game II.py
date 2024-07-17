#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Greedy, Sliding Window
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums)-1:
            return 1
        res = 1
        i = 0
        while i < len(nums):
            j = i + nums[i]
            max_dist = 0
            next = j
            if j >= len(nums) - 1: return res + 1
            while j > i:
                if max_dist < j + nums[j]:
                    max_dist = j + nums[j]
                    next = j
                    if max_dist >= len(nums) - 1: return res + 1
                j-=1
            i = next
            res += 1
        return res
