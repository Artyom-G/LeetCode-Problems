#Time Complexity: O(n)
#Space Complexity: O(0)
#Approach: String Slicing
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
