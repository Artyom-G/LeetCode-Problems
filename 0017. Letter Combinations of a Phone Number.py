#Time Complexity: O(2^n)
#Space Complexity: O(2^n)
#Approach: Recursion
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        output = []
        def recursion(i, current):
            if i >= len(digits):
                output.append(current)
            else:
                for j in mapping[int(digits[i]) - 2]:
                    recursion(i + 1, current + j)
        recursion(0, "")
        if output == [""]: return []
        return output
