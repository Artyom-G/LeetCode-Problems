#Time Complexity: O(n!)
#Space Complexity: O(n!)
#Approach: Recursion, Backtracking
class Solution:
    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        def recursion(arr, used):
            if len(arr) == len(nums):
                self.res.append(arr)
            else:
                for i in nums:
                    if i not in used:
                        _arr = arr.copy()
                        _arr.append(i)
                        _used = used.copy()
                        _used.add(i)
                        recursion(_arr, _used)
                del arr
                del used
        recursion([], set())
        return self.res
