#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: 1-pointer
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_counter = 0
        for i in s:
            if i == t[t_counter]:
                t_counter+=1
                if(t_counter >= len(t)):
                    return 0
        return len(t)-t_counter
