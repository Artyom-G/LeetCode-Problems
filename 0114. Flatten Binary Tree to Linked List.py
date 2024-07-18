#Time Complexity: O(n)
#Space Complexity: O(logn)
#Approach: Recursion, DFS, Backtracking

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cur = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if root:
                left = root.left
                right = root.right
                if self.cur:
                    self.cur.right = root
                    self.cur.left = None
                self.cur = root
                dfs(left)
                dfs(right)

        dfs(root)
        
