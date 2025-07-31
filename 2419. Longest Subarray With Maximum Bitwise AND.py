# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Math
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        elif len(nums) == 1: 
            return 1
        res = 1
        max_val = -math.inf
        max_dupes = 1
        previous = -math.inf
        for i in nums:
            if max_val < i: res = 1
            max_val = max(max_val, i)
            if i == previous:
                max_dupes+=1
                if max_val == i: 
                    res = max(max_dupes, res)
            else:
                max_dupes=1
            previous = i
        return res
