#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: List
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
