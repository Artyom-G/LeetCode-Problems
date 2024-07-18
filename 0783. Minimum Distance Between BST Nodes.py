#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: DFS, Binary Search Tree, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    order = []
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.order.clear()
        def dfs(root=root):
            if root:
                dfs(root.left)
                self.order.append(root.val)
                dfs(root.right)
        dfs(root)
        res = self.order[1] - self.order[0]
        for i in range(1, len(self.order)):
            res = min(res, self.order[i] - self.order[i-1])
        return res
