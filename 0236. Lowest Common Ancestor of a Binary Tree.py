#Time Complexity: O(n)
#Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global startPath
        global destPath
        startPath = []
        destPath = []
        def recursion(root=root, path=[]):
            global startPath
            global destPath
            if root:
                path.append(root)
                if root.val == p.val:
                    startPath = path.copy()
                    if destPath: return
                if root.val == q.val:
                    destPath = path.copy()
                    if startPath: return
                recursion(root.left, path)
                recursion(root.right, path)
                path.pop()
        
        recursion()

        parent = None
        parent_order = None
        for i in range(min(len(startPath), len(destPath))):
            if startPath[i] == destPath[i]:
                parent = startPath[i]
                parent_order = i
            else:
                break
        return parent
