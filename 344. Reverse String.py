class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s)/2)): s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
