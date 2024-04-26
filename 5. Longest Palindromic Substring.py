#Time Complexity: O(n^2) but the average time is roughly linear
#Space Complexity: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        Max = ""
        
        def maxSubstringAboutChar(char, offset = 0):
            if char - offset < 0 or char + offset >= len(s):
                return s[char - (offset - 1): char + (offset - 1) + 1]
            elif s[char - offset] == s[char + offset]:
                return maxSubstringAboutChar(char, offset + 1)
            else:
                return s[char - (offset - 1): char + (offset - 1) + 1]
            
        def maxSubstringAboutTwoChar(char, offset = 0):
            if char - offset < 0 or (char + 1) + offset >= len(s):
                return s[char - (offset - 1): (char + 1) + (offset - 1) + 1]
            elif s[char - offset] == s[(char + 1) + offset]:
                return maxSubstringAboutTwoChar(char, offset + 1)
            else:
                return s[char - (offset - 1): (char + 1) + (offset - 1) + 1]
        
        for i in range(len(s)):
            _max = maxSubstringAboutChar(i)
            Max = _max if len(Max) < len(_max) else Max
        for i in range(len(s)):
            _max = maxSubstringAboutTwoChar(i)
            Max = _max if len(Max) < len(_max) else Max
        
        return Max
