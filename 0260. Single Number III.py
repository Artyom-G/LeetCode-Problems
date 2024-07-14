#Time Complexity: O(n^2) but O(n) on average
#Space Complexity: O(n)
#Approach: Sets
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output_nums = set()
        for i in nums:
            if i not in output_nums:
                output_nums.add(i)
            else:
                output_nums.remove(i)
        return list(output_nums)
