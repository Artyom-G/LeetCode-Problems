from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(lambda: None) 
        for i in range(len(nums)):
            second = target - nums[i]
            if dic[second] != None:
                return [i, dic[second]]
            dic[nums[i]] = i

