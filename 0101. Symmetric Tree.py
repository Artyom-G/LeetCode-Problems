#Time Complexity: O(n)
#Space Complexity: O(logn) because Recursion Stack
#Approach: Same Tree, Binary Tree, DFS, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    equal = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if root1 and root2 and root1.val == root2.val:
                dfs(root1.left, root2.right)
                dfs(root1.right, root2.left)
            elif not root1 and not root2: 1
            else: self.equal = False
        dfs(root.left, root.right)
        return self.equal
