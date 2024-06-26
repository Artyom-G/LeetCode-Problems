#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Depth First Search, Recursion, Binary Search, Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def recursion(root):
            if(root.left):
                recursion(root.left)
            nodes.append(root)
            if(root.right):
                recursion(root.right)
            root.left = None
            root.right = None

        recursion(root)

        left = 0
        right = len(nodes) - 1
        def recursion2(left = left, right = right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = nodes[mid]
            node.left = recursion2(left, mid - 1)
            node.right = recursion2(mid + 1, right)
            return node
        return recursion2()     
