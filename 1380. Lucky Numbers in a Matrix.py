#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Matrix, Set
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = set()
        for row in matrix:
            m = row[0]
            for i in row[1:]:
                m = min(m, i)
            mins.add(m)
        
        res = []
        for column in range(len(matrix[0])):
            M = matrix[0][column]
            for i in range(1, len(matrix)): 
                M = max(M, matrix[i][column])
            if M in mins: res.append(M)
        return res
        
