# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: BFS 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root: return []
        q = deque([(root, 0)])
        level = 0
        solution = []
        last = None
        while q:
            cur, l = q.popleft()
            if l != level:
                solution.append(last.val)
                level = l
            if cur.left: q.append((cur.left, l+1))
            if cur.right: q.append((cur.right, l+1))
            last = cur
        solution.append(last.val)
        return solution 
