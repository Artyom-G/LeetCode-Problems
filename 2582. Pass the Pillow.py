#Time Complexity: O(1)
#Space Complexity: O(1)
#Approach: Modular Arithmetic, Math
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycles = time // (n - 1) 
        position = time % (n - 1) 
        
        if cycles % 2 == 0:
            return position + 1
        else:
            return n - position
