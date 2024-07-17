#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Index Map
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = dict()
        for i in range(len(nums)):
            if nums[i] not in index_map:
                index_map[nums[i]] = i
            else:
                if i - index_map[nums[i]] <= k: return True
                index_map[nums[i]] = i
        return False
                
