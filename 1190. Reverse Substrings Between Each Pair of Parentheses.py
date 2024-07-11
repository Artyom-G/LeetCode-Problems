#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Index Stack
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        n = len(s)
        while i < len(s): 
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")" and len(stack) > 0:
                last = stack.pop()
                s = s[:last] + s[i-1: last: -1] + s[i+1:]
                i-=2
            i+=1
        return s
