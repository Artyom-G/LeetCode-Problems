#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = sorted(list(set(nums)))
        for i in range(len(output)):
            nums[i] = output[i]
        return len(output)
