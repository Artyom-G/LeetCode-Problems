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
    forest = []
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.forest.clear()
        to_delete = set(to_delete)
        def dfs(root=root):
            if root:
                if root.val in to_delete:
                    if root.left and root.left.val not in to_delete: self.forest.append(root.left)
                    dfs(root.left)
                    root.left = None
                    if root.right and root.right.val not in to_delete: self.forest.append(root.right)
                    dfs(root.right)
                    root.right = None
                    del root
                else:
                    if root.left and root.left.val not in to_delete: dfs(root.left)
                    else:
                        dfs(root.left)
                        root.left = None
                    if root.right and root.right.val not in to_delete: dfs(root.right)
                    else:
                        dfs(root.right)
                        root.right = None
        
        if root.val not in to_delete: 
            self.forest.append(root)
            dfs(root)
        else:
            dfs(root)
            del root

        for tree in self.forest:
            print(tree)
        return self.forest
            
