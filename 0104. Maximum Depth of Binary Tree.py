#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: DFS, Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    M = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root=root, path=1):
            if root:
                self.M = max(self.M, path)
                dfs(root.left, path + 1)
                dfs(root.right, path + 1)
        dfs()
        return self.M
