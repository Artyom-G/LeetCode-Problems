# Time Complexity: O(1) for all ops
# Space Complexity: O(n)
# Approch: Stack
class MinStack:
    def __init__(self):
        self.stack = []

    # Every element keeps tracks of the min element up to that point
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(val, self.stack[-1][1])])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
