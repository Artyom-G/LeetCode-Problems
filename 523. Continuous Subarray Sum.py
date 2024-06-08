#Time Complexity: O(n^2), Exceeds Time Limit
#Space Complexity: O(1)
#Approach: Brute Force
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if sum(nums[i:j+1]) % k == 0:
                    return True
        return False
