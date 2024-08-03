#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Freq Map
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = {}
        for i in target:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        
        for i in arr:
            if i not in counter:
                return False
            counter[i] -= 1
            if counter[i] < 0: return False
        
        for i in counter:
            if counter[i] != 0:
                return False
        return True
