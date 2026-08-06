# Time Complexity: O(n*m)
# Space Complexity: O(1)
# Approach: Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])
        if m == 0: return []
        v_moves, h_moves = n-1, m-1

        d = "r"
        i_start, j_start = 0, 0
        i, j = 0, 0
        sol = [matrix[0][0]]
        first_time = True # first time we switch direction is an edge case
        moved = True
        while v_moves > 0 or h_moves > 0:
            print(i, j, matrix[i][j])
            if d == "r":
                if j - j_start >= h_moves:
                    if not moved: break
                    if not first_time:
                        h_moves -= 1
                    first_time = False
                    d = "d"
                    i_start, j_start = i, j
                    moved = False
                    continue
                j += 1
            if d == "l":
                if j_start - j >= h_moves:
                    if not moved: break
                    h_moves -= 1
                    d = "u"
                    i_start, j_start = i, j
                    moved = False
                    continue
                j -= 1
            if d == "d":
                if i - i_start >= v_moves:
                    if not moved: break
                    v_moves -= 1
                    d = "l"
                    i_start, j_start = i, j
                    moved = False
                    continue
                i += 1
            if d == "u":
                if i_start - i >= v_moves:
                    if not moved: break
                    v_moves -= 1
                    d = "r"
                    i_start, j_start = i, j
                    moved = False
                    continue
                i -= 1
            moved = True
            sol.append(matrix[i][j])
        return sol
