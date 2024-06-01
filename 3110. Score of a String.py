#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Iteration
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i-1]) - ord(s[i]))
        return score
