#Time Compexity: O(1)
#Space Complexity: O(1)
#Approach: Is
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
