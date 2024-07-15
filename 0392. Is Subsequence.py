#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Array
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        si = 0
        for ti in t:
            if s[si] == ti:
                si+=1
                if si >= len(s):
                    return True
        return False
