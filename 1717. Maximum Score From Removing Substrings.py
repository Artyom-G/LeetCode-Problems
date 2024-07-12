#Time Complexity: O(n^2)
#Space Complexity: O(n)
#Approach: Greedy
#This can be optimized to O(n) Time Complexity with a Stack implemintion instead of s = s[:i-1] + s[i+1:]
class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
        first_remove = 'ab'
        second_remove = 'ba'
        if y > x:
            x, y = y, x
            first_remove, second_remove = second_remove, first_remove

        res = 0
        i = 1
        while i < len(s):
            if s[i-1: i + 1] == first_remove:
                res += x
                s = s[:i-1] + s[i+1:]
                i-=1
            else:
                i+=1
        
        i = 1
        while i < len(s):
            if s[i-1: i + 1] == second_remove:
                res += y
                s = s[:i-1] + s[i+1:]
                i-=1
            else:
                i+=1
        
        return res
