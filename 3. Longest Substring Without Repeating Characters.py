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
