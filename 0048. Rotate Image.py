# Time Complexity: O(n^2)
# Space Complexity: O(1) Auxiliary
# Approach: Math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip horizontally
        for i in range(n):
            matrix[i].reverse()
