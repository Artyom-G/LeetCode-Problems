#Time Complexity: O(n*m)
#Space Complexity: O(n)
#Approach: Sort
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def jumble(num):
            s = str(num)
            res = ""
            for i in s:
                res += str(mapping[int(i)])
            return int(res)
        arr = []
        for i in range(len(nums)):
            arr.append([jumble(nums[i]), i, nums[i]])
        arr.sort()
        return [i[2] for i in arr]
