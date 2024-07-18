#Time Complexity: O(n)
#Space Complexity: O(logn)
#Approach: DFS, Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
        def dfs(root, S):
            if self.res or (targetSum == S and (not root.left and not root.right)): 
                    self.res = True
                    return
            if root.left: dfs(root.left, S+root.left.val)
            if root.right: dfs(root.right, S+root.right.val)
        dfs(root, root.val)
        return self.res
