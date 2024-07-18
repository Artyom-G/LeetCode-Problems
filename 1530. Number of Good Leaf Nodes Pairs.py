#Time Complexity: O(n^2)
#Space Complexity: O(n)
#Approach: LCA, DFS, Backtracking, Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    reachedFirst = False
    def countPairs(self, root: TreeNode, distance: int) -> int:
        #self.leaves = []
        self.depths = []
        self.anc_depths = []
        self.seen = set()
        def dfs(root=root, depth=0, ad=0):
            if self.reachedFirst: ad += 1
            if root.left:
                dfs(root.left, depth+1, ad)
            if root.right:
                dfs(root.right, depth+1, ad)
            if not root.left and not root.right and root not in self.seen:
                self.depths.append(depth)
                self.anc_depths.append(depth-ad)
                #self.leaves.append(root.val)
                if not self.reachedFirst: self.seen.add(root)
                self.reachedFirst = True
        
        res = 0
        while True:
            #This gives all the solutions with the left-most leaf as one of the fixed nodes
            #We add the left-most leaf to seen and pretend it doesnt exist the next time we do this
            #self.leaves.clear()
            self.depths.clear()
            self.anc_depths.clear()
            self.reachedFirst = False

            dfs()

            if not self.reachedFirst: break

            for i in range(1, len(self.depths)):
                if self.depths[0] - self.anc_depths[i] + self.depths[i] - self.anc_depths[i] <= distance:
                    res += 1

        return res
