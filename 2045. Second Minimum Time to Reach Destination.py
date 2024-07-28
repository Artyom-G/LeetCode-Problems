class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for i in range(n+1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        print(adj)

        dist = [math.inf for i in range(n+1)]
        prev = [None for i in range(n+1)]

        min_heap = [(0, 1, None)]

        while min_heap:
            w1, n1, p1 = heapq.heappop(min_heap)
            if dist[n1] != math.inf:
                continue
            dist[n1] = w1
            prev[n1] = p1

            for n2 in adj[n1]:
                if n2 not in dist:
                    heapq.heappush(min_heap, (w1 + 1, n2, n1))
        
        print(dist)
        print(prev)

        return 0
