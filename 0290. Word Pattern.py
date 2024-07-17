#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Hash Map
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern): return False
        dic_p = dict()
        dic_s = dict()
        for i in range(len(pattern)):
            if pattern[i] in dic_p and s[i] in dic_s:
                if dic_p[pattern[i]] != s[i] or dic_s[s[i]] != pattern[i]: return False
            elif pattern[i] not in dic_p and s[i] not in dic_s:
                dic_p[pattern[i]] = s[i] 
                dic_s[s[i]] = pattern[i]
            else: return False
        return True
