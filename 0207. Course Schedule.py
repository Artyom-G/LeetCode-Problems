# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
# Approach: Topological Ordering, BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Return isAcyclic
        # Acyclic iff there is a topological ordering
        adjList = [set() for i in range(numCourses)]
        adjReversedList = [set() for i in range(numCourses)]
        for e in prerequisites:
            to, frm = e
            adjList[frm].add(to)
            adjReversedList[to].add(frm)

        # Remove a root, the resulting subgraph G' will have a new root if acyclic
        q = deque()
        for i, hood in enumerate(adjReversedList):
            if len(hood) == 0:
                q.append(i)
        if not q: 
            return False

        # Topological order can be created by appending the popped v's
        # topological_order = []
        num_removed = 0
        while q:
            v = q.popleft()
            # topological_order.append(v)
            num_removed+=1

            neighbors = adjList[v].copy()
            for u in neighbors:
                adjList[v].remove(u)
                adjReversedList[u].remove(v)
                
                # This is a new root in G'
                if(len(adjReversedList[u]) == 0):
                    q.append(u)
        
        # We removed all possible 'roots', now we have to check if the graph is empty
        if num_removed != numCourses:
            return False

        return True
