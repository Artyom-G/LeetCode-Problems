#Time Complexity: O(sqrt(n))
#Space Complexity: O(1)
#Approach: Iteration
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i * i <= x:
            i += 1
        return i - 1


#A faster approach would be with bit manipulation
