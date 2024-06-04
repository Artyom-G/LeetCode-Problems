#Time Complexity: O(2^n)
#Space Complexity: O(2^n)
#Approach: Recursion

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def recursion(string, opened, closed):
            if(n == opened == closed):
                output.append(string)
            else:
                if opened < n:
                    recursion(string + "(", opened + 1, closed)
                if closed < n and opened > closed:
                    recursion(string + ")", opened, closed + 1)
        
        recursion("", 0, 0)
        return output
