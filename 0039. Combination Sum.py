#Time Complexity: O(n!)
#Space Complexity: O(n!)
#Approach: Recursion, Backtracking
class Solution:
    res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res.clear()
        def recursion(arr, small, S):
            arr = arr.copy()
            if S == target:
                self.res.append(arr)
            elif S < target:
                for i in range(small, len(candidates)):
                    if candidates[i] + S <= target:
                        recursion(arr + [candidates[i]], i, S + candidates[i])
        recursion([], 0, 0)
        return self.res
