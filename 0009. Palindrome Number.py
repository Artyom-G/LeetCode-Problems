#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        while(i < len(x)/2):
            if(x[i] != x[-i-1]):
                return False
            i += 1
        return True
