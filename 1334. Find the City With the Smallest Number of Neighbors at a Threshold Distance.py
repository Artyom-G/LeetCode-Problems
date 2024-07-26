#Time Complexity: O(n*m)
#Space Comlpexity: O(n^2)
#Approach: DFS, Graph, Dynamic Programming 
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for i in range(n)]
        for edge in edges:
            if edge[2] <= distanceThreshold:
                adj[edge[0]].append([edge[1], edge[2]])
                adj[edge[1]].append([edge[0], edge[2]])

        self.adjThresh = [set() for i in range(n)]
        self.adjThresholds = [[math.inf for i in range(n)] for j in range(n)]

        def dfs(cityOrig, city, thresh):
            for nei in adj[city]:
                if nei[0] != cityOrig and (nei[0] not in self.adjThresh[cityOrig] or self.adjThresholds[cityOrig][nei[0]] < thresh - nei[1]) and thresh - nei[1] >= 0:
                    self.adjThresholds[cityOrig][nei[0]] = thresh - nei[1]
                    self.adjThresh[cityOrig].add(nei[0])
                    dfs(cityOrig, nei[0], thresh - nei[1])

        m = math.inf
        res = 0
        for city in range(n):
            dfs(city, city, distanceThreshold)
            if m >= len(self.adjThresh[city]):
                res = city
                m = len(self.adjThresh[city])
        
        return res
