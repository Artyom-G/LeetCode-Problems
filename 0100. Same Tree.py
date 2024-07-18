#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Binary Tree, DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    equal = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if root1 and root2 and root1.val == root2.val:
                dfs(root1.left, root2.left)
                dfs(root1.right, root2.right)
            elif not root1 and not root2: 1
            else: self.equal = False
        dfs(p, q)
        return self.equal
                
