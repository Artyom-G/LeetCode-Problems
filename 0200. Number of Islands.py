# Time Complexity: O(mn)
# Space Complexity: O(mn)
# Approach: BFS
class Solution:
    def printGrid(self, grid):
        print("Grid Start")
        for r in grid:
            print(r)
        print("Grid End")
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        dq = deque()
        res = 0
        for r in range(n):
            for c in range(m):
                dq.append([r, c])
                while(len(dq) != 0):
                    cur = dq.popleft()
                    if(grid[cur[0]][cur[1]] == "2" or grid[cur[0]][cur[1]] == "0"):
                        continue
                    connected = False
                    for d in dirs:
                        nr, nc = d[0] + cur[0], d[1] + cur[1]
                        if(nr < 0 or nr >= n or nc < 0 or nc >= m):
                            continue
                        if(grid[nr][nc] == "2"):
                            connected = True
                            continue
                        if(grid[nr][nc] == "0"):
                            continue
                        dq.append([nr, nc])
                    if not connected:
                        res += 1
                    grid[cur[0]][cur[1]] = "2"
        return res
