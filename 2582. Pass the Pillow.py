#Time Complexity: O(1)
#Space Complexity: O(0)
#Approach: Modular Arithmetic, Math
#One Line Solution Lol
class Solution:
    def passThePillow(self, n: int, time: int) -> int:    
        return (time % (n - 1)) + 1 if time // (n - 1) % 2 == 0 else n - (time % (n - 1))

#Time Complexity: O(1)
#Space Complexity: O(0)
#Approach: Modular Arithmetic, Math
class Solution:
    def passThePillow(self, n: int, time: int) -> int:    
        if (time // (n - 1)) % 2 == 0:
            return (time % (n - 1)) + 1
        else:
            return n - (time % (n - 1))

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
