# Time Complexity: O(n)
# Space Complexity: O()
# Approach: Math
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        highest_bit = 1

        for i in range(1, n + 1):
            if i == highest_bit * 2:
                highest_bit *= 2

            ans.append(1 + ans[i - highest_bit])

        return ans
