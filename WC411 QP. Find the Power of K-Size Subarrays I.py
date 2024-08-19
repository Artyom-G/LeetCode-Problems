#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            if k == 1: return [nums[0]]
            else: return [-1]
        if len(nums) == 0:
            return []
        cons = 1
        cons_arr = []
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                cons +=1 
            else:
                cons_arr += list(range(cons, 0, -1))
                cons = 1
        if cons > 1: cons_arr += list(range(cons, 0, -1))
        cons_arr.append(1)

        res = []
        for i in range(len(nums)-k+1):
            if cons_arr[i] >= k:
                res.append(nums[i + k - 1])
            else:
                res.append(-1)

        return res


