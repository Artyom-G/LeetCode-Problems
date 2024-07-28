#Time Complexity: O(n^2*m)
#Space Complexity: O(n*m)
#Approach: Dijkstra's 
#Time Limit Exceeded, Could Implement DP
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        source_set = set(list(source))
        target_set = set(list(target))
        element_set = source_set.union(target_set, set(original), set(changed))
        adj = dict()
        for i in range(len(original)):
            if original[i] not in adj:
                adj[original[i]] = [(changed[i], cost[i])]
            else:
                adj[original[i]].append((changed[i], cost[i]))

        distances = {}
        for i in element_set:
            _dict = {}
            for j in element_set:
                _dict[j] = math.inf
            distances[i] = _dict

        res = 0
        for i in range(len(source)):
            explored = set()
            start = source[i]
            destination = target[i]
            distances[start][start] = 0
            heap = [(0, start)]
            heapq.heapify(heap)
            if start in adj:
                for n in adj[start]:
                    heapq.heappush(heap, (n[1], n[0]))
            while destination not in explored:
                if len(heap) <= 0:
                    return -1
                v = heapq.heappop(heap)[1]
                if v in explored: continue
                explored.add(v)
                if v not in adj: continue
                for n in adj[v]:
                    heapq.heappush(heap, (distances[start][v] + n[1], n[0]))
                    if distances[start][v] + n[1] < distances[start][n[0]]:
                        distances[start][n[0]] = distances[start][v] + n[1]
            res += distances[start][destination]

        return res
