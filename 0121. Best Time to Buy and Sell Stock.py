# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Prefix Min, Suffix Max

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        m = [prices[0]]
        for p in prices[1:]:
            m.append(min(p, m[-1]))
        
        M = [0 for i in prices]
        M[-1] = prices[-1]
        for p in range(len(prices)-2, -1, -1):
            M[p] = max(prices[p], M[p+1])

        res = -float(inf)
        for i in range(len(prices)):
            res = max(res, M[i] - m[i])
        return res
