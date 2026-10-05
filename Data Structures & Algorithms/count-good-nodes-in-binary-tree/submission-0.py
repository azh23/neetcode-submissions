# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, mx):
            if node is None:
                return 0
            return traverse(node.left, max(mx, node.val)) + traverse(node.right, max(mx, node.val)) + (1 if node.val >= mx else 0)
        return traverse(root, -101)