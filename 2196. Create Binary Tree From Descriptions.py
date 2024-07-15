#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Map, Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        map = {}
        possible_roots = set()
        for des in descriptions:
            parent = des[0]
            child = des[1]
            isLeft = des[2]
            
            if parent not in map:
                map[parent] = TreeNode(parent, None, None)
                possible_roots.add(parent)
            
            if child not in map:
                map[child] = TreeNode(child, None, None)

            if isLeft:
                map[parent].left = map[child]
            else:
                map[parent].right = map[child]
        
        for des in descriptions:
            if des[1] in possible_roots:
                possible_roots.remove(des[1])
        
        for i in possible_roots:
            return map[i]
        
