#Time Complexity: O(k + rowCond.Length + colCond.Length)
#Space Comlpexity: O(k)
#Approach: Topological Sort, DFS, Recursion, Backtracking, Directed Graph, Matrix
class Solution:
    def topologicalSortUtil(self, v, adj, visited, stack):
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, adj, visited, stack)
        stack.append(v)

    def topologicalSort(self, adj, V):
        stack = []
        visited = [False] * V
        for i in range(1, V):
            if not visited[i]:
                self.topologicalSortUtil(i, adj, visited, stack)
        return stack
          
    def checkCycles(self, V, adj):
        self.visited_outer = [False] * V
        self.cycle = False

        def dfs(v, visited):
            visited[v] = True
            for n in adj[v]:
                if visited[n]: self.cycle = True
                elif not self.visited_outer[n]: dfs(n, visited.copy())
            self.visited_outer[v] = True

        for v in range(1, V):
            if not self.visited_outer[v]:
                dfs(v, [False] * V)
                if self.cycle: return True
            self.visited_outer[v] = True
        return False

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        V = k + 1

        #Checking if Cyclic
        adjRow = [[] for _ in range(V)]
        for i in rowConditions:
            adjRow[i[0]].append(i[1])
        if self.checkCycles(V, adjRow): return []

        #Checking if Cyclic
        adjCol = [[] for _ in range(V)]
        for i in colConditions:
            adjCol[i[0]].append(i[1])
        if self.checkCycles(V, adjCol): return []

        #Topologically Sort
        rowSorted = self.topologicalSort(adjRow, V)
        colSorted = self.topologicalSort(adjCol, V)

        #Building Matrix
        res = [[0 for i1 in range(k)] for i2 in range(k)]
        row_index_map = {}
        for i in range(k):
            row_index_map[rowSorted[i]] = i
        
        for j in range(k):
            val = colSorted[j]
            i = row_index_map[val]
            res[k-i-1][k-j-1] = val
        return res
