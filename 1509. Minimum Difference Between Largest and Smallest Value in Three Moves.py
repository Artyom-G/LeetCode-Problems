#Time Complexity: O(nlogn)
#Space Complexity: O(n) because of Tim-Sort, O(1) with other sorting algorithms
#Approach: Greedy, Sort
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        res = nums[-4] - nums[0]
        res = min(res, nums[-3] - nums[1])
        res = min(res, nums[-2] - nums[2])
        res = min(res, nums[-1] - nums[3])
        return res
