#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Math, Modular Arithmetic
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        facts = [1,1,2,6,24,120,720,5040,40320,362880]
        perm = ""
        used = [False] * (n + 1)
        while n > 0:
            #This is the current perm group 
            #Groups are definied to share the first i characters
            m = ceil(float(k)/facts[n-1])
            
            #Figuring out what the perm group's char is
            #In the simple case where i = 0 then char = m
            count = 0
            char = 0
            for i in range(1, len(used)):
                if not used[i]:
                    count += 1
                if count == m:
                    char = i
                    break
            
            #adding char to perm
            perm += str(char)
            used[char] = True

            #Setting up the next loop
            k = k - (m-1) * facts[n-1]
            n -= 1
        return perm
