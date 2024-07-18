#Time Complexity: O(n)
#Space Complexity: O(logn)
#Approach: Binary Search, Recursion, DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nums = []
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        def recursion(L, H):
            if L <= H:
                M = (L + H) // 2
                root = TreeNode(nums[M], None, None)
                root.left = recursion(L, M-1)
                root.right = recursion(M+1, H)
                return root
        return recursion(0, len(nums)-1)
