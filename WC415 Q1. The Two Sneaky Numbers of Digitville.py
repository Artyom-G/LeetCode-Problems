#Time Complexity: O(n)
#Space Complexity: O(1) Extra
#Approach: Hash Set
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for i in nums:
            if i in seen: res.append(i)
            else: seen.add(i)
        return res
