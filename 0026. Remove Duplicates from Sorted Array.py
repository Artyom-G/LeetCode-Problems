# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Maps
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        output = []

        #This is a huge time saver
        seen_add = seen.add
        
        for i in nums:
            if(i not in seen):
                output.append(i)
            seen_add(i)
        for i in range(len(seen)):
            nums[i] = output[i]
        return len(seen)


# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Sliding Window
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 1
        
        for right in range(1, len(nums)):
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
        
        return left
                
