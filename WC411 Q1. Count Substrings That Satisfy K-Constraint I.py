#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Sliding Window
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        L = 0
        R = 0
        ones = 0
        zeroes = 0
        res = 0

        while R < len(s):
            if s[R] == '1':
                ones += 1
            else:
                zeroes += 1

            while ones > k and zeroes > k:
                if s[L] == '1':
                    ones -= 1
                else:
                    zeroes -= 1
                L += 1

            res += (R - L + 1)

            R += 1

        return res
