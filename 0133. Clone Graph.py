# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
# Approach: BFS, Hashmap

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        v = node
        q = deque([v])
        new_map = {}
        new_map[v] = Node(v.val, [])

        while q:
            v = q.popleft()
            v_new = new_map[v]
            for u in v.neighbors:
                if u not in new_map:
                    new_map[u] = Node(u.val, [])
                    q.append(u)
                u_new = new_map[u]
                v_new.neighbors.append(u_new)

        return new_map[node]
