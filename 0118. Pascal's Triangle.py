# Time Complexity: O(n^2)
# Space Complexity: O(n) auxiliry but O(n^2) 
# Approach: Math, DP
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        row = [1]
        for r in range(numRows-1):
            new_row = [1]
            for i in range(len(row)-1):
                if i + 1 == len(row):
                    new_row.append(row[i] + 0)
                else: 
                    new_row.append(row[i] + row[i+1])
            new_row.append(1)
            res.append(new_row)
            row = new_row
        return res
        
