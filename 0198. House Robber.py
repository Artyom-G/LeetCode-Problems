#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
#Approach: Dynamic Programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.M = 0
        self.sums = {}
        
        S = 0
        _nums = []
        for i in range(0, len(nums)):
            if i % 2 == 0:
                S += nums[i]
                _nums.append(True)
            else:
                _nums.append(False)
        self.sums[tuple(_nums)] = S

        def recursion(i, changed, path):
            if i < len(self.nums):
                recursion(i + 2, changed, path + [False, True])
                recursion(i + 3, i, path + [False, False, True])
                path.pop()
            else:
                while i >= len(self.nums):
                    path.pop()
                    i-=1
                if changed != None:
                    S = self.sums[tuple(path)]
                    path[changed] = not path[changed]
                    S -= self.nums[changed]
                    if changed + 1 < len(self.nums): 
                        path[changed + 1] = not path[changed]
                        S+= self.nums[changed+1]
                    self.sums[tuple(path)] = S
                else:
                    S = self.sums[tuple(path)]
                self.M = max(self.M, S)

        recursion(0, None, [True])
        recursion(1, 0, [False, True])
        return self.M
