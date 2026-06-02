# Time Complexity: O(n)
# Space Complexity: O(logn)
# Approach: Divide and Conquer, BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            m = float(inf)
            M = -float(inf)
            if not root:
                return [True, m, M]

            if root.left:
                [Lb, Lm, LM] = helper(root.left)
                if not (LM < root.val) or not Lb:
                    return [False, -1, -1]
                m = Lm
            else:
                m = root.val
            
            if root.right:
                [Rb, Rm, RM] = helper(root.right)
                if not (Rm > root.val) or not Rb:
                    return [False, -1, -1]
                M = RM
            else:
                M = root.val
            return [True, m, M]
            
        return helper(root)[0]
                
        
