# Time Complexity: O(n)
# Space Complexity: O(1) Auxilary
# Approach: DP, Math
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        # ans[i] = 1 + dp[i-dom_bit]
        ans = [0, 1]
        dom_bit = 1
        for i in range(2,n+1):
            if(i >= dom_bit):
                dom_bit *= 2
            ans.append(ans[i-dom_bit] + 1)
        return ans
