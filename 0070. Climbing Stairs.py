#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Fib, DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1: 1, 2: 2}
        def fib(n):
            if n in dp:
                return dp[n]
            else:
                dp[n] = fib(n-1) + fib(n-2) 
                return dp[n]
        fib(n)
        return dp[n]
