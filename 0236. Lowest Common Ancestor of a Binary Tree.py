#Time Complexity: O(n)
#Space Complexity: O(logn)
#Approach: DFS, Recursion, Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    p_found = False
    q_found = False
    ancestor = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(root=root, ancestor=root):
            if root:
                if root.val == p.val:
                    self.p_found = True
                    if self.q_found: self.ancestor = ancestor
                if root.val == q.val:
                    self.q_found = True
                    if self.p_found: self.ancestor = ancestor
                if not (self.p_found or self.q_found): recursion(root.left, root.left)
                else: recursion(root.left, ancestor)
                if not (self.p_found or self.q_found): recursion(root.right, root.right)
                else: recursion(root.right, ancestor)
        recursion()
        return self.ancestor


#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: DFS, Recursion, Tree, Intersection, Array

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
