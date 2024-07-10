#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Stack
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if len(stack) > 0:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)
