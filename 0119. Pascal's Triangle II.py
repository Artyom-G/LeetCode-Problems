# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: DP, Math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        fact_dp = [1, 1]
        for i in range(2, rowIndex+1):
            fact_dp.append(fact_dp[i-1] * i)
        
        res = []
        # Using the fact that the function is symmetric 
        for i in range((rowIndex+2)//2):
            res.append(fact_dp[rowIndex] // fact_dp[i] // fact_dp[rowIndex-i])
        if rowIndex % 2 == 1: 
            return res + res[::-1]
        else: 
            return res[:-1] + res[::-1]
