# Time Complexity: O(nm)
# Space Complexity: O(nm)
# Approach: BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        global_visited = set()
        def BFS(source, mode="touches_edge"):
            q = deque([source])
            visited = set()
            while q:
                v = q.popleft()
                r, c = v
 
                if(mode == "touches_edge" and (r == 0 or c == 0 or r == n-1 or c == m-1)):
                    return True
                elif(mode == "replace"):
                    board[r][c] = "X"

                us = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for u in us:
                    r, c = u
                    if(r < 0 or c < 0 or r >= n or c >= m):
                        continue
                    if((r, c) in visited):
                        continue
                    if(board[r][c]=="X"):
                        continue
                    q.append(u)
                    visited.add((r,c))
                    global_visited.add((r,c))
            if mode == "touches_edge":
                return False
            return
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "X":
                    continue
                if (r, c) in global_visited:
                    continue
                touches_edge = BFS([r, c])
                if(not touches_edge):
                    BFS([r,c], "replace")
