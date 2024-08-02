#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Sliding Window
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = 0
        for i in nums:
            if i == 1: total_ones += 1

        ones = 0
        for i in range(total_ones):
            if nums[i] == 1: ones += 1

        max_ones = ones
        for i in range(0, total_ones + 1 + len(nums)):
            if nums[(i+total_ones)%len(nums)] == 1: ones += 1
            if nums[(i)%len(nums)] == 1: ones -= 1
            max_ones = max(max_ones, ones)
        
        return total_ones - max_ones
        
