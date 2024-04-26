#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        matrix = ["" for i in range(numRows)]
        i = 0
        matrix_i = 0
        matrix_i_dir = 1
        while(i < len(s)):
            matrix[matrix_i] += s[i]
            i += 1
            if matrix_i_dir == 1 and matrix_i == numRows - 1:
                matrix_i_dir = -1
            elif matrix_i_dir == -1 and matrix_i == 0:
                matrix_i_dir = 1
            
            if matrix_i_dir == 1:
                matrix_i += 1
            if matrix_i_dir == -1:
                matrix_i -= 1

        s = ""        
        for i in matrix:
            s += i
        
        return s
