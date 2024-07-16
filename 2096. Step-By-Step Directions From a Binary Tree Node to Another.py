#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: DFS, Recursion, Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        global startPath
        global destPath
        startPath = []
        destPath = []
        def recursion(root=root, path=[]):
            global startPath
            global destPath
            if root:
                path.append(root)
                if root.val == startValue:
                    startPath = path.copy()
                    if destPath: return
                if root.val == destValue:
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
        
        res = "U" * (len(startPath) - parent_order - 1)

        current = parent
        i = parent_order + 1
        while current.val != destValue:
            if(current.left and destPath[i].val == current.left.val):
                current = current.left
                res += "L"
            else:
                current = current.right
                res += "R"
            i+=1
        return res

#Time Complexity: O(n)
#Space Complexity: O(2^n)
#Approach: DFS, Recursion, Binary Tree
#Time and Memory Limit Exceeded

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath = []
        destPath = []
        
        stack = [(root, [root])]

        while stack:
            node, path = stack.pop()

            # If the node is a leaf, add the path to the result
            if node.val == startValue:
                startPath = path.copy()
                if destPath: break
            if node.val == destValue:
                destPath = path.copy()
                if startPath: break

            # If the node has a right child, add it to the stack
            if node.right:
                stack.append((node.right, path + [node.right]))

            # If the node has a left child, add it to the stack
            if node.left:
                stack.append((node.left, path + [node.left]))
        
        #print(startPath, destPath)

        parent = None
        parent_order = None
        for i in range(min(len(startPath), len(destPath))):
            if startPath[i] == destPath[i]:
                parent = startPath[i]
                parent_order = i
            else:
                break
        
        res = "U" * (len(startPath) - parent_order - 1)

        current = parent
        i = parent_order + 1
        while current.val != destValue:
            if(current.left and destPath[i].val == current.left.val):
                current = current.left
                res += "L"
            else:
                current = current.right
                res += "R"
            i+=1
        return res
