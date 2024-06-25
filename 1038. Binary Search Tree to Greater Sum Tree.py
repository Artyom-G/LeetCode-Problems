#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Depth-First Search, Suffix Sum, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        dfs_list = []
        def recursion(root=root):
            if root.left:
                recursion(root.left)
            dfs_list.append(root.val)
            if root.right:
                recursion(root.right)
        recursion()
        #print(dfs_list)

        suffix_sum = [0]
        for i in range(1, len(dfs_list)):
            suffix_sum.append(suffix_sum[i-1] + dfs_list[len(dfs_list) - i])
        #print(suffix_sum)

        global index
        index = len(suffix_sum) - 1
        def recursion2(root=root):
            global index
            if root.left:
                recursion2(root.left)
            root.val += suffix_sum[index]
            index-=1
            if root.right:
                recursion2(root.right)
        recursion2()
        return root
