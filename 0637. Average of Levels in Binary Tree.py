#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: BFS, Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum / level_count)

        return res


# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        level = 0
        next_level_node = root
        sol = []
        running_average = 0
        running_count = 0
        while len(q) != 0:
            node = q.popleft()
            if next_level_node == node:
                level += 1
                next_level_node = None
                sol.append(running_average) 
                running_average = 0
                running_count = 0
            running_average = (running_average * running_count + float(node.val)) / (running_count + 1)
            running_count += 1
            if node.left != None:
                if next_level_node == None: next_level_node = node.left
                q.append(node.left)
            if node.right != None:
                if next_level_node == None: next_level_node = node.right
                q.append(node.right)
        sol.append(running_average)
        return sol[1:]
