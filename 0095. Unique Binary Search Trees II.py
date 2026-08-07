# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Approach: Recursion, Binary Tree
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def deepcopy_tree(node):
            if node is None:
                return None

            new_node = TreeNode(node.val)
            new_node.left = deepcopy_tree(node.left)
            new_node.right = deepcopy_tree(node.right)
            return new_node

        def deepcopy_list(roots):
            return [deepcopy_tree(root) for root in roots]

        def serialize(node):
            if node is None:
                return "#"
            return f"{node.val},{serialize(node.left)},{serialize(node.right)}"

        solutions = []

        def rec(roots):
            if len(roots) == 1:
                solutions.append(roots[0])
                return

            m = len(roots)
            for i in range(m - 1):
                # merge roots[i] as left tree with roots[i+1] as right tree
                roots1 = deepcopy_list(roots)
                cur = roots1[i]
                while cur.right:
                    cur = cur.right
                cur.right = roots1[i + 1]
                roots1.pop(i + 1)
                rec(roots1)

                # merge roots[i+1] as right tree with roots[i] as left tree
                roots2 = deepcopy_list(roots)
                cur = roots2[i + 1]
                while cur.left:
                    cur = cur.left
                cur.left = roots2[i]
                roots2.pop(i)
                rec(roots2)

        roots = []
        for i in range(1, n + 1):
            roots.append(TreeNode(i))
        rec(roots)

        # remove duplicate trees
        seen = set()
        unique = []
        for tree in solutions:
            key = serialize(tree)
            if key not in seen:
                seen.add(key)
                unique.append(tree)

        return unique
