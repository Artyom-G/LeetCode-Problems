#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
#Approach: DP1
#Time Limit Exceeded
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        mem = []
        for i in range(0, 4):
            mem.append([])
            for j in range(i,len(b)-3+i):
                mem[i].append(a[i]*b[j])
        self.mem = mem
        self.S = -inf

        def dfs(i, j, s):
            if i >= len(self.mem):
                if s > self.S: self.S = s
            else:
                for _j in range(j, len(self.mem[i])):
                    dfs(i+1, _j, s + self.mem[i][_j])
        dfs(0, 0, 0)
                
        return self.S
