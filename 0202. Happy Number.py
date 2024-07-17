#Time Complexity: O(m)
#Space Complexity: O(m)
#Approach: Set, Math
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNewN(n):
            n = str(n)
            res = 0
            for i in n:
                res += int(i) * int(i)
            return res
        seen = set()
        while n not in seen:
            seen.add(n)
            n = getNewN(n)
            if n == 1:
                return True
        return False
