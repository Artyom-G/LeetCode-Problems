# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
# Approach: BFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = [[] for i in range(n)]
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        q = deque()
        visited = [False for i in range(n)]
        dist = [math.inf for i in range(n)]
        parents = [None for i in range(n)]
        q.append(source)
        dist[source] = 0
        v = None
        while q:
            prev = v
            v = q.popleft()
            visited[v] = True
            parents[v] = prev
            if v == destination:
                return True
                # Comment the above to find the shortest path
                break
            for nv in adj_list[v]:
                if visited[nv]:
                    continue
                q.append(nv)
        
        return False
        # Comment the above to find the shortest path

        # Logic for finding the shortest path

        path = []
        v = destination
        while v != None:
            path.append(v)
            v = parents[v]
        return path[::-1]
