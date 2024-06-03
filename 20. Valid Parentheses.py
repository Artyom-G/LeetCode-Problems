#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Stacks
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if stack != []: element = stack.pop()
                else: return False
                if not ((element == '(' and i == ')') or (element == '{' and i == '}') or (element == '[' and i == ']')):
                    return False
        if stack == []: return True
