#Time Complexity: O(n!)
#Space Complexity: O(n!)
#Approach: Recursion, Backtracking
class Solution:
    res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res.clear()
        def recursion(arr, m):
            arr = arr.copy()
            if len(arr) < k:
                for i in range(m, n+1):
                    recursion(arr + [i], i+1)
            else:
                self.res.append(arr)
        recursion([], 1)
        return self.res
