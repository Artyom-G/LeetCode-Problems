#Approach: Sliding Window
#Time Complexity O(n) Space Complexity O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        iLeft = 0
        iRight = 0
        maxLength = 0
        while(iRight < len(s)):
            substring = s[iLeft: iRight]
            if s[iRight] in substring:
                iLeft += substring.index(s[iRight]) + 1
            else:
                maxLength = max(maxLength, len(substring) + 1)
            iRight += 1
        return maxLength


"""
#Approach: Sliding Window
#Time Complexity O(n^2) Space Complexity O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = len(set(s))
        D = dict()
        while(maxWindow >= 0):
            for i in range(len(s) - maxWindow + 1):
                substring = s[i:i + maxWindow]
                if(substring not in D):
                    if len(set(substring)) == len(substring):
                        return maxWindow
                    D[substring] = 0
            maxWindow -= 1
"""


"""
#Time Complexity O(n^3) Space Complexity O(n^3)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global M
        M = 0
        D = dict()
        Max_Substring = len(set(s))
        def substtring(s):
            global M
            if(len(s) == 1):
                M = max(M, 1)
            else:
                if s not in D:
                    if len(s) > Max_Substring:
                        D[s] = 0
                    else:
                        L = len(s) if len(set(s)) == len(s) else 0
                        D[s] = L
                        M = max(M, L)                    
                    substtring(s[1:])
                    substtring(s[:-1])

        substtring(s)
        return M
"""
