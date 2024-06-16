#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Partial Sort
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            while x>=1 and x<= len(nums) and x!=i+1 and nums[x-1] != x:
                nums[x-1], nums[i] = nums[i], nums[x-1]
                x = nums[i]

        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j + 1
        return len(nums) + 1



#Time Complexity: O(n^2) but O(n) on average
#Space Complexity: O(n)
#Approach: Sets
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        nums = set(nums)
        while True:
            if i not in nums:
                return i
            i+=1
