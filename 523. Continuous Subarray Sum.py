#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Prefix Sum, Hash Table
class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_index_map = {0: -1}
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum %= k
            
            if sum in remainder_index_map:
                if i - remainder_index_map[sum] > 1:  
                    return True
            else:  
                remainder_index_map[sum] = i
        
        return False
        

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
